import shutil
import subprocess
from pathlib import Path

try:
    import tomllib  # Python 3.11+
except ImportError:
    import tomli as tomllib  # Python 3.9 / 3.10

from hatchling.builders.hooks.plugin.interface import BuildHookInterface


class CustomBuildHook(BuildHookInterface):
    def initialize(self, version, build_data):
        root = Path(self.root)

        # Read project name from pyproject.toml - no hardcoding needed
        with open(root / "pyproject.toml", "rb") as f:
            pyproject = tomllib.load(f)
        schema_name = pyproject["project"]["name"]

        source_schema_path = (
            root / "src" / schema_name / "schema" / f"{schema_name}.yaml"
        )
        sqla_dir = root / "project" / "sqlalchemy"
        sqla_file = sqla_dir / f"{schema_name}.py"
        dest_file = root / schema_name / f"{schema_name}.py"

        # Dynamically configure wheel targets - avoids hardcoding project name
        # in pyproject.toml which would need updating for each new model repo
        build_data["shared_data"] = {}
        build_data["packages"] = [schema_name]
        build_data["include"] = [f"{schema_name}/*.csv", f"{schema_name}/*.py"]

        # Generate the SQLAlchemy file only if not already present.
        # When uv build runs in an isolated temp environment it cannot access
        # .venv, so we rely on just site/_gen_sqla having pre-generated the
        # file in the working directory before uv build is called.
        sqla_dir.mkdir(parents=True, exist_ok=True)
        if not sqla_file.exists():
            # Find gen-sqla: prefer the project .venv, fall back to PATH
            gen_sqla = root / ".venv" / "bin" / "gen-sqla"
            if not gen_sqla.exists():
                found = shutil.which("gen-sqla")
                if not found:
                    raise RuntimeError(
                        "gen-sqla not found. Either run `uv sync --group dev` "
                        "first, or pre-generate the SQLAlchemy file by running "
                        "`just _gen_sqla` before `uv build`."
                    )
                gen_sqla = Path(found)

            with open(sqla_file, "w") as out:
                subprocess.run(
                    [str(gen_sqla), str(source_schema_path), "--declarative"],
                    stdout=out,
                    check=True,
                )

        # Copy into the package directory so hatchling can bundle it
        dest_file.parent.mkdir(parents=True, exist_ok=True)
        shutil.copy(sqla_file, dest_file)

        # Register SQLAlchemy file with hatchling
        build_data["artifacts"].append(str(dest_file))
        build_data["force_include"][str(dest_file)] = f"{schema_name}/{schema_name}.py"

        # Bundle harmony CSVs if present (not all models will have these)
        harmony_src = root / "project" / "harmony"
        if harmony_src.exists():
            for csv_file in harmony_src.glob("*.csv"):
                dest_csv = root / schema_name / csv_file.name
                shutil.copy(csv_file, dest_csv)
                build_data["artifacts"].append(str(dest_csv))
                build_data["force_include"][str(dest_csv)] = (
                    f"{schema_name}/{csv_file.name}"
                )
