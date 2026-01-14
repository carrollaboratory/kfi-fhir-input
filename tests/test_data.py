"""Data test."""
import os
import glob
import pytest
from pathlib import Path

import kfi_fhir_input.datamodel.kfi_fhir_input
from linkml_runtime.loaders import yaml_loader
from linkml_runtime.dumpers import yaml_dumper

DATA_DIR_VALID = Path(__file__).parent / "data" / "valid"
DATA_DIR_INVALID = Path(__file__).parent / "data" / "invalid"

VALID_EXAMPLE_FILES = glob.glob(os.path.join(DATA_DIR_VALID, '*.yaml'))
INVALID_EXAMPLE_FILES = glob.glob(os.path.join(DATA_DIR_INVALID, '*.yaml'))


@pytest.mark.parametrize("filepath", VALID_EXAMPLE_FILES)
def test_valid_data_files(filepath):
    """Test loading of all valid data files."""
    target_class_name = Path(filepath).stem.split("-")[0]
    tgt_class = getattr(
        kfi_fhir_input.datamodel.kfi_fhir_input,
        target_class_name,
    )
    obj = yaml_loader.load(filepath, target_class=tgt_class)
    assert obj


@pytest.mark.parametrize("filepath", INVALID_EXAMPLE_FILES)
def test_invalid_data_files(filepath):
    """Test loading of all valid data files."""
    target_class_name = Path(filepath).stem.split("-")[0]
    tgt_class = getattr(
        kfi_fhir_input.datamodel.kfi_fhir_input,
        target_class_name,
    )
    
    # This works, but I don't how to properly handle all of the different
    # types of assertions that any given invalid resource might result in. 
    with pytest.raises(Exception):
        obj = yaml_loader.load(filepath, target_class=tgt_class)

