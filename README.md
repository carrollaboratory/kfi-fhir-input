# kfi-fhir-input
KF/INCLUDE FHIR Source Schema. 

# Reusing Local Capabilities
This repo is intended to automatically build the models that will be used for 
transformation into FHIR. However, if there is interest in accessing the 
data from DBT using SQL Alchemy, you could incorporate this into the repo to 
generate the models as part of the release. 

## GitHub Action - release.yaml
In addition to zipping up your project directory, it will also build the 
package up the SQL Alchemy files and add them to the release downloads. 

Basically, just drop [TBD](The github action) into your 
.github/workflows directory. 

If you don't care about the SQL Alchemy files, you probably can get away with
just removing the two lines below from the workflow file to get an otherwise 
functional release: 

```
      dist/*.whl
      dist/*.tar.gz
```

## Scripts
The scripts directory provides two scripts: gen_harmony.py and hatch_build.py

The gen_harmony.py file generates a MD style harmony file mapping enumerated 
values in the model to their expected forms for use in FHIR (such as OMB Race, 
etc). This assumes that your incoming data complies with those enumerated 
values. 

hatch_build.py builds preps the SQL Alchemy file for packaging by twine/build, 
which linkml provides tooling. For this script to work, you must configure the 
toml and just files as described below. 

## pyproject.toml
### Build System
My build assumes we are using hatchling for the build. If your template used
something other than hatchling, then this may not work at all. I believe the
only addition I made was adding "tomli" to the end, which is necessary for the
python script to dynamically determine the project's name (to make this more
portable across models.)

```toml
[build-system]
requires = ["hatchling", "uv-dynamic-versioning", "tomli"]
build-backend = "hatchling.build"
```

### dependency-groups
Add the last two lines to your dev value in [dependency-groups]:

```toml
[dependency-groups]
dev = [
    "linkml>=1.9.3",
    "mkdocs-material>=8.2.8",
    "mkdocs-mermaid2-plugin>=1.1.1",
    "jupyter>=1.0.0",
    "mknotebooks>= 0.8.0",
    "ftd-dd @ git+https://github.com/carrollaboratory/ftd-dd",
    "hatchling>=1.27.0",
    "tomli>=2.0.0"
]
```
Please note that third from the last line is what we use to build data 
dictionaries that are used for our DBT pipeline. So, you may or may not need
that line. The others were populated by the template copy. 

### hatch_build.py
To tie the script into the 'uv build' system, you have to add the following
lines

```toml
# Release the SQL Alchemy files
[tool.hatch.build.hooks.custom]
path = "scripts/hatch_build.py"
```

### [optional excludes]
I found this to be helpful to avoid warnings from uv
```toml
[tool.hatch.build.targets.sdist]
exclude = [
  ".direnv",
  ".venv",
  "scratch"
]
```
## project.justfile
I would recommend just grabbing a copy from this repo and editing as desired. 

## justfile
I recommend adding our dependencies project specific stuff to gen-project, 
since that is a depdency for site. 

```
site: gen-project lint gen-doc _gen_ftddd _gen_sqla _gen_harmony
```

Use whichever makes sense for your needs.
