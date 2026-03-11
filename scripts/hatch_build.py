import shutil
import subprocess
from pathlib import Path

try:
    import tomllib  # Python 3.11+
except ImportError:
    import tomli as tomllib  # Python 3.10

from hatchling.builders.hooks.plugin.interface import BuildHookInterface


class CustomBuildHook(BuildHookInterface):
    def initialize(self, version, build_data):
        root = Path(self.root)
        with open(root / "pyproject.toml", "rb") as f:
            pyproject = tomllib.load(f)
        schema_name = pyproject["project"]["name"]
        source_schema_path = (
            f"src/{schema_name}/schema/{schema_name}.yaml"  # adjust if needed
        )
        sqla_dir = root / "project" / "sqlalchemy"
        sqla_file = sqla_dir / f"{schema_name}.py"
        dest_file = root / schema_name / f"{schema_name}.py"

        # Dynamically configure wheel targets instead of hardcoding in pyproject.toml
        build_data["shared_data"] = {}
        build_data["packages"] = [schema_name]
        build_data["include"] = [f"{schema_name}/*.csv", f"{schema_name}/*.py"]

        # Find gen-sqla: prefer the project .venv, fall back to PATH
        gen_sqla = root / ".venv" / "bin" / "gen-sqla"
        if not gen_sqla.exists():
            import shutil as sh

            found = sh.which("gen-sqla")
            if not found:
                raise RuntimeError(
                    "gen-sqla not found. Run `uv sync --group dev` first."
                )
            gen_sqla = Path(found)

        # Generate the SQLAlchemy file
        sqla_dir.mkdir(parents=True, exist_ok=True)
        with open(sqla_file, "w") as out:
            subprocess.run(
                [str(gen_sqla), str(source_schema_path), "--declarative"],
                stdout=out,
                check=True,
            )

        # Copy it into the package directory for the wheel
        dest_file.parent.mkdir(parents=True, exist_ok=True)
        shutil.copy(sqla_file, dest_file)

        # Tell hatchling to include it
        build_data["artifacts"].append(str(dest_file))
        build_data["force_include"][str(dest_file)] = f"{schema_name}/{schema_name}.py"

        # Harmony files
        harmony_src = root / "project" / "harmony"
        for csv_file in harmony_src.glob("*.csv"):
            dest_csv = root / schema_name / csv_file.name
            shutil.copy(csv_file, dest_csv)
            build_data["artifacts"].append(str(dest_csv))
            build_data["force_include"][str(dest_csv)] = (
                f"{schema_name}/{csv_file.name}"
            )
