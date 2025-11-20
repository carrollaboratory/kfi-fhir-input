from __future__ import annotations

import re
import sys
from datetime import (
    date,
    datetime,
    time
)
from decimal import Decimal
from enum import Enum
from typing import (
    Any,
    ClassVar,
    Literal,
    Optional,
    Union
)

from pydantic import (
    BaseModel,
    ConfigDict,
    Field,
    RootModel,
    SerializationInfo,
    SerializerFunctionWrapHandler,
    field_validator,
    model_serializer
)


metamodel_version = "None"
version = "None"


class ConfiguredBaseModel(BaseModel):
    model_config = ConfigDict(
        serialize_by_alias = True,
        validate_by_name = True,
        validate_assignment = True,
        validate_default = True,
        extra = "forbid",
        arbitrary_types_allowed = True,
        use_enum_values = True,
        strict = False,
    )

    @model_serializer(mode='wrap', when_used='unless-none')
    def treat_empty_lists_as_none(
            self, handler: SerializerFunctionWrapHandler,
            info: SerializationInfo) -> dict[str, Any]:
        if info.exclude_none:
            _instance = self.model_copy()
            for field, field_info in type(_instance).model_fields.items():
                if getattr(_instance, field) == [] and not(
                        field_info.is_required()):
                    setattr(_instance, field, None)
        else:
            _instance = self
        return handler(_instance, info)



class LinkMLMeta(RootModel):
    root: dict[str, Any] = {}
    model_config = ConfigDict(frozen=True)

    def __getattr__(self, key:str):
        return getattr(self.root, key)

    def __getitem__(self, key:str):
        return self.root[key]

    def __setitem__(self, key:str, value):
        self.root[key] = value

    def __contains__(self, key:str) -> bool:
        return key in self.root


linkml_meta = LinkMLMeta({'default_prefix': 'kfi_fhir_sparks',
     'default_range': 'string',
     'description': 'DBT Output Schema for FHIR Ingest',
     'id': 'https://carrollaboratory.github.io/kif-fhir-input',
     'imports': ['linkml:types', 'practitioner'],
     'license': 'MIT',
     'name': 'kfi-fhir-input',
     'prefixes': {'PATO': {'prefix_prefix': 'PATO',
                           'prefix_reference': 'http://purl.obolibrary.org/obo/PATO_'},
                  'biolink': {'prefix_prefix': 'biolink',
                              'prefix_reference': 'https://w3id.org/biolink/vocab/'},
                  'example': {'prefix_prefix': 'example',
                              'prefix_reference': 'http://www.example.org/rdf#'},
                  'kfi_fhir_sparks': {'prefix_prefix': 'kfi_fhir_sparks',
                                      'prefix_reference': 'https://carrollaboratory.github.io/kif-fhir-input'},
                  'linkml': {'prefix_prefix': 'linkml',
                             'prefix_reference': 'https://w3id.org/linkml/'},
                  'schema': {'prefix_prefix': 'schema',
                             'prefix_reference': 'http://schema.org/'}},
     'see_also': ['https://carrollaboratory.github.io/kif-fhir-input'],
     'source_file': 'src/kfi_fhir_input/schema/kfi_fhir_input.yaml',
     'title': 'KF/Include FHIR Input Model'} )


class Record(ConfiguredBaseModel):
    """
    One row / entity within the database
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'abstract': True,
         'from_schema': 'https://carrollaboratory.github.io/kif-fhir-input',
         'title': 'Record'})

    id: str = Field(default=..., title="ID", description="""Global ID for this record""", json_schema_extra = { "linkml_meta": {'domain_of': ['Record']} })
    external_id: Optional[list[str]] = Field(default=[], title="External Identifiers", description="""Other identifiers for this entity, eg, from the submitting study or in systems link dbGaP""", json_schema_extra = { "linkml_meta": {'domain_of': ['Record']} })


class Practitioner(Record):
    """
    For our purposes, this will be an investigator.
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'annotations': {'fhir_resource': {'tag': 'fhir_resource',
                                           'value': 'Practitioner'}},
         'from_schema': 'https://carrollaboratory.github.io/kfi-fhir-input/practitioner',
         'title': 'FHIR Practitioner Resource Content'})

    name: Optional[str] = Field(default=None, title="Name", description="""Name of the entity.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Practitioner', 'Institution']} })
    email: Optional[str] = Field(default=None, title="Email Address", description="""An email address to reach the entity.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Practitioner']} })
    institution: Optional[str] = Field(default=None, title="Institution", description="""The institution this record is associated with.""", json_schema_extra = { "linkml_meta": {'annotations': {'db_column': {'tag': 'db_column', 'value': 'institution_id'},
                         'target_slot': {'tag': 'target_slot', 'value': 'id'}},
         'domain_of': ['Practitioner']} })
    description: Optional[str] = Field(default=None, title="Description", description="""Note relating to who this person is in relation to the study""", json_schema_extra = { "linkml_meta": {'domain_of': ['Practitioner']} })
    title: Optional[str] = Field(default=None, title="Title", description="""The title of the Investigator, eg, \"Assistant Professor\"""", json_schema_extra = { "linkml_meta": {'domain_of': ['Practitioner']} })
    id: str = Field(default=..., title="ID", description="""Global ID for this record""", json_schema_extra = { "linkml_meta": {'domain_of': ['Record']} })
    external_id: Optional[list[str]] = Field(default=[], title="External Identifiers", description="""Other identifiers for this entity, eg, from the submitting study or in systems link dbGaP""", json_schema_extra = { "linkml_meta": {'domain_of': ['Record']} })


class Institution(Record):
    """
    Institution related to study or research personnel
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'annotations': {'fhir_resource': {'tag': 'fhir_resource',
                                           'value': 'Institution'}},
         'from_schema': 'https://carrollaboratory.github.io/kfi-fhir-input/institution',
         'title': 'Research Institution'})

    name: Optional[str] = Field(default=None, title="Name", description="""Name of the entity.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Practitioner', 'Institution']} })
    id: str = Field(default=..., title="ID", description="""Global ID for this record""", json_schema_extra = { "linkml_meta": {'domain_of': ['Record']} })
    external_id: Optional[list[str]] = Field(default=[], title="External Identifiers", description="""Other identifiers for this entity, eg, from the submitting study or in systems link dbGaP""", json_schema_extra = { "linkml_meta": {'domain_of': ['Record']} })


# Model rebuild
# see https://pydantic-docs.helpmanual.io/usage/models/#rebuilding-a-model
Record.model_rebuild()
Practitioner.model_rebuild()
Institution.model_rebuild()
