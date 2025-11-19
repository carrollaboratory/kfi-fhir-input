from pathlib import Path
from .kfi_fhir_input import *

THIS_PATH = Path(__file__).parent

SCHEMA_DIRECTORY = THIS_PATH.parent / "schema"
MAIN_SCHEMA_PATH = SCHEMA_DIRECTORY / "kfi_fhir_input.yaml"
