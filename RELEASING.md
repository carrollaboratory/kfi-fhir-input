# Publishing a Model Release

This document describes how to publish a versioned release of the ACR Harmonized
Data Model. Releases produce a Python wheel (containing the SQLAlchemy model and
harmony CSV) and a zip of all generated project artifacts, attached to a GitHub
Release.

---

## Prerequisites

Before tagging a release, make sure:

- Your changes are committed and pushed to `main` (or the appropriate branch)
- The model builds cleanly locally: run `just site` and confirm no errors
- You have permission to push tags to this repository

---

## Versioning Convention

Releases use [PEP 440](https://peps.python.org/pep-0440/) version numbers, derived
automatically from git tags by `uv-dynamic-versioning`. You do not set the version
manually anywhere — the tag **is** the version.

Use the following format for tags:

| Type | Tag format | Example | When to use |
|---|---|---|---|
| Full release | `vMAJOR.MINOR.PATCH` | `v1.2.0` | Stable, reviewed model changes |
| Patch / hotfix | `vMAJOR.MINOR.PATCH` | `v1.2.1` | Small corrections to a release |
| Pre-release | `vMAJOR.MINOR.PATCH-beta.N` | `v1.2.0-beta.1` | For review before a full release |

### When to increment which number

- **MAJOR** — breaking changes to the schema (removed fields, renamed enums, changed
  types) that would require updates in downstream consumers like Piper
- **MINOR** — additive changes (new tables, new enum values, new fields) that are
  backward compatible
- **PATCH** — corrections that do not change the schema structure (typo fixes,
  description updates, documentation)

---

## How to Tag and Release

### Option 1: From the command line (recommended)

```bash
# Make sure you are on main and up to date
git checkout main
git pull

# Create an annotated tag (the message appears in the release notes)
git tag -a v1.2.0 -m "Add harmonized phenotype tables and update enum definitions"

# Push the tag to GitHub — this triggers the release workflow automatically
git push origin v1.2.0
```

### Option 2: From the GitHub UI

1. Go to the repository on GitHub
2. Click **Releases** in the right sidebar
3. Click **Draft a new release**
4. Under **Choose a tag**, type your new tag (e.g. `v1.2.0`) and select
   **Create new tag on publish**
5. Fill in the release title and notes
6. Click **Publish release** — this triggers the workflow automatically

### Option 3: Manual workflow trigger

If you need to re-run a release for an existing tag without re-tagging:

1. Go to **Actions** → **Model Release**
2. Click **Run workflow**
3. Enter the tag name (e.g. `v1.2.0`) and click **Run workflow**

---

## What the Release Produces

Once the workflow completes (~3-5 minutes), the GitHub Release will contain:

| Asset | Contents | Who needs it |
|---|---|---|
| `acr_harmonized_data_model-VERSION-py3-none-any.whl` | SQLAlchemy model + harmony CSV, installable as a Python package | Downstream Python projects (Piper, cloud jobs) |
| `acr_harmonized_data_model-VERSION.tar.gz` | Source distribution | Build tooling / archival |
| `project-artifacts.zip` | All linkml-generated outputs (OWL, JSON Schema, TypeScript, Java, etc.) | Modelers, ontology tooling, downstream non-Python consumers |

---

## Installing a Released Wheel in a Downstream Project

To pin a specific version in a downstream project (e.g. Piper):

**With pip:**
```bash
pip install https://github.com/anvilproject/acr-harmonized-data-model/releases/download/v1.2.0/acr_harmonized_data_model-1.2.0-py3-none-any.whl
```

**In `requirements.txt`:**
```
acr_harmonized_data_model @ https://github.com/anvilproject/acr-harmonized-data-model/releases/download/v1.2.0/acr_harmonized_data_model-1.2.0-py3-none-any.whl
```

**In `pyproject.toml` (uv or pip):**
```toml
dependencies = [
  "acr-harmonized-data-model @ https://github.com/anvilproject/acr-harmonized-data-model/releases/download/v1.2.0/acr_harmonized_data_model-1.2.0-py3-none-any.whl",
]
```

---

## Accessing Package Data in Python

Once installed, the SQLAlchemy model and harmony CSV are accessible without
knowing the install path:

```python
from importlib.resources import files

# Access the SQLAlchemy module directly
from acr_harmonized_data_model import acr_harmonized_data_model

# Access the harmony CSV as a file
harmony_csv = files("acr_harmonized_data_model").joinpath("harmony.csv")
with harmony_csv.open("r") as f:
    content = f.read()
```

---

## Troubleshooting

**The workflow fails with `FileNotFoundError` on the SQLAlchemy file**
The `hatch_build.py` hook could not find `gen-sqla`. Make sure `uv sync --group dev`
ran successfully before the `uv build` step.

**The version shows as `0.0.0.post{N}.dev0`**
This means the build ran on a commit that is not directly tagged. Tag the exact
commit you want to release, or use the manual workflow trigger with the correct tag.

**`just site` fails in CI**
Check that your `config.public.mk` / `.env` variables (`LINKML_SCHEMA_NAME`, etc.)
are available in the runner environment. These may need to be added as repository
variables in GitHub Actions settings.
