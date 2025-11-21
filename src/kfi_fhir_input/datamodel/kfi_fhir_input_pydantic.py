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
     'imports': ['linkml:types',
                 'practitioner',
                 'associated_party',
                 'institution',
                 'period',
                 'practitioner_role',
                 'practitioner'],
     'license': 'MIT',
     'name': 'kfi-fhir-input',
     'prefixes': {'hl7_rsp_org_type': {'prefix_prefix': 'hl7_rsp_org_type',
                                       'prefix_reference': 'http://hl7.org/fhir/research-study-party-organization-type'},
                  'hl7_rsp_role': {'prefix_prefix': 'hl7_rsp_role',
                                   'prefix_reference': 'http://hl7.org/fhir/research-study-party-role'},
                  'kfi': {'prefix_prefix': 'kfi',
                          'prefix_reference': 'https://carrollaboratory.github.io/kfi-fhir-input/'},
                  'kfi_fhir_sparks': {'prefix_prefix': 'kfi_fhir_sparks',
                                      'prefix_reference': 'https://carrollaboratory.github.io/kif-fhir-input'},
                  'linkml': {'prefix_prefix': 'linkml',
                             'prefix_reference': 'https://w3id.org/linkml/'}},
     'see_also': ['https://carrollaboratory.github.io/kif-fhir-input'],
     'source_file': 'src/kfi_fhir_input/schema/kfi_fhir_input.yaml',
     'title': 'KF/Include FHIR Input Model'} )

class EnumResearchStudyPartyOrganizationType(str, Enum):
    """
    Research Study Party Organization Type
    """
    NIH = "nih"
    fda = "fda"


class EnumResearchStudyPartyRole(str, Enum):
    """
    This is a ResearchStudy's party role.
    """
    sponsor = "sponsor"
    lead_sponsor = "lead_sponsor"
    sponsor_investigator = "sponsor_investigator"
    primary_investigator = "primary_investigator"
    collaborator = "collaborator"
    funding_source = "funding_source"
    general_contact = "general_contact"
    recruitment_contact = "recruitment_contact"
    sub_investigator = "sub_investigator"
    study_director = "study_director"
    study_chair = "study_chair"
    Institutional_Review_Board = "irb"



class AssociatedParty(ConfiguredBaseModel):
    """
    Sponsors, collaborators, and other parties affiliated with a research study.
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'annotations': {'fhir_resource': {'tag': 'fhir_resource',
                                           'value': 'https://nih-ncpi.github.io/ncpi-fhir-ig-2/StructureDefinition/research-study-associated-party'}},
         'from_schema': 'https://carrollaboratory.github.io/kfi-fhir-input/associated_party',
         'slot_usage': {'period_id': {'multivalued': True, 'name': 'period_id'}},
         'title': 'Associated Party'})

    name: Optional[str] = Field(default=None, title="Name", description="""Name of the entity.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Practitioner', 'AssociatedParty', 'Institution']} })
    role: Optional[EnumResearchStudyPartyRole] = Field(default=None, title="Role", description="""Research Study Party Role""", json_schema_extra = { "linkml_meta": {'domain_of': ['AssociatedParty']} })
    period_id: Optional[list[str]] = Field(default=[], title="Period", description="""Reference to a time period which defines a Start and End datatime period.""", json_schema_extra = { "linkml_meta": {'domain_of': ['AssociatedParty', 'Period', 'PractitionerRole']} })
    classifier: Optional[list[EnumResearchStudyPartyOrganizationType]] = Field(default=[], title="Classifier", description="""Research Study Party Organization Type (what type of institution is party)""", json_schema_extra = { "linkml_meta": {'domain_of': ['AssociatedParty']} })
    party: Optional[str] = Field(default=None, title="Associated Party", description="""Individual or organization associated with study""", json_schema_extra = { "linkml_meta": {'any_of': [{'range': 'Practitioner'}, {'range': 'Institution'}],
         'domain_of': ['AssociatedParty']} })


class Period(ConfiguredBaseModel):
    """
    Time period associated with some FHIR resource
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'from_schema': 'https://carrollaboratory.github.io/kfi-fhir-input/period',
         'title': 'Period'})

    period_id: str = Field(default=..., title="Period ID", description="""Database ID for this record. This is not a global ID, is a global identifier""", json_schema_extra = { "linkml_meta": {'domain_of': ['AssociatedParty', 'Period', 'PractitionerRole']} })
    start: Optional[datetime ] = Field(default=None, title="Start", description="""Start attribute for a FHIR period data type.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Period']} })
    end: Optional[datetime ] = Field(default=None, title="End", description="""End attribute for a FHIR period data type.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Period']} })


class PractitionerRole(ConfiguredBaseModel):
    """
    PractitionerRole covers the recording of the location and types of services that Practitioners are able to provide for an organization.
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'annotations': {'fhir_resource': {'tag': 'fhir_resource',
                                           'value': 'PractitionerRole'}},
         'from_schema': 'https://carrollaboratory.github.io/kfi-fhir-input/practitioner_role',
         'title': 'Practitioner Role'})

    institution_id: Optional[str] = Field(default=None, title="Institution", description="""The institution this record is associated with.""", json_schema_extra = { "linkml_meta": {'annotations': {'target_slot': {'tag': 'target_slot',
                                         'value': 'institution_id'}},
         'domain_of': ['Practitioner', 'Institution', 'PractitionerRole']} })
    practitioner_id: Optional[str] = Field(default=None, title="Practitioner ID", description="""The Global ID for the PractitionerRole that links a Practitioner to their Institution.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Practitioner', 'PractitionerRole']} })
    period_id: Optional[str] = Field(default=None, title="Period", description="""Reference to a time period which defines a Start and End datatime period.""", json_schema_extra = { "linkml_meta": {'domain_of': ['AssociatedParty', 'Period', 'PractitionerRole']} })
    practitioner_role_id: str = Field(default=..., title="Practitioner Role ID", description="""Global ID for this record""", json_schema_extra = { "linkml_meta": {'domain_of': ['Practitioner', 'PractitionerRole']} })


class HasExternalId(ConfiguredBaseModel):
    """
    Has an external ID
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'abstract': True,
         'from_schema': 'https://carrollaboratory.github.io/kif-fhir-input',
         'title': 'Has'})

    external_id: Optional[list[str]] = Field(default=[], title="External Identifiers", description="""Other identifiers for this entity, eg, from the submitting study or in systems link dbGaP""", json_schema_extra = { "linkml_meta": {'domain_of': ['HasExternalId']} })


class Practitioner(HasExternalId):
    """
    For our purposes, this will be an investigator.
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'annotations': {'fhir_resource': {'tag': 'fhir_resource',
                                           'value': 'Practitioner'}},
         'from_schema': 'https://carrollaboratory.github.io/kfi-fhir-input/practitioner',
         'title': 'FHIR Practitioner Resource Content'})

    name: Optional[str] = Field(default=None, title="Name", description="""Name of the entity.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Practitioner', 'AssociatedParty', 'Institution']} })
    email: Optional[str] = Field(default=None, title="Email Address", description="""An email address to reach the entity.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Practitioner']} })
    institution_id: Optional[str] = Field(default=None, title="Institution", description="""The institution this record is associated with.""", json_schema_extra = { "linkml_meta": {'annotations': {'target_slot': {'tag': 'target_slot',
                                         'value': 'institution_id'}},
         'domain_of': ['Practitioner', 'Institution', 'PractitionerRole']} })
    practitioner_role_id: Optional[str] = Field(default=None, title="Practitioner Role ID", description="""Global ID for this record""", json_schema_extra = { "linkml_meta": {'annotations': {'target_slot': {'tag': 'target_slot',
                                         'value': 'practitioner_role_id'}},
         'domain_of': ['Practitioner', 'PractitionerRole']} })
    description: Optional[str] = Field(default=None, title="Description", description="""Note relating to who this person is in relation to the study""", json_schema_extra = { "linkml_meta": {'domain_of': ['Practitioner']} })
    title: Optional[str] = Field(default=None, title="Title", description="""The title of the Investigator, eg, \"Assistant Professor\"""", json_schema_extra = { "linkml_meta": {'domain_of': ['Practitioner']} })
    practitioner_id: str = Field(default=..., title="Practitioner ID", description="""The Global ID for the Practitioner.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Practitioner', 'PractitionerRole']} })
    external_id: Optional[list[str]] = Field(default=[], title="External Identifiers", description="""Other identifiers for this entity, eg, from the submitting study or in systems link dbGaP""", json_schema_extra = { "linkml_meta": {'domain_of': ['HasExternalId']} })


class Institution(HasExternalId):
    """
    Institution related to study or research personnel
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'annotations': {'fhir_resource': {'tag': 'fhir_resource',
                                           'value': 'Organization'}},
         'from_schema': 'https://carrollaboratory.github.io/kfi-fhir-input/institution',
         'title': 'Research Institution'})

    name: Optional[str] = Field(default=None, title="Name", description="""Name of the entity.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Practitioner', 'AssociatedParty', 'Institution']} })
    institution_id: str = Field(default=..., title="Institution ID", description="""Global ID for this record""", json_schema_extra = { "linkml_meta": {'domain_of': ['Practitioner', 'Institution', 'PractitionerRole']} })
    external_id: Optional[list[str]] = Field(default=[], title="External Identifiers", description="""Other identifiers for this entity, eg, from the submitting study or in systems link dbGaP""", json_schema_extra = { "linkml_meta": {'domain_of': ['HasExternalId']} })


class Record(HasExternalId):
    """
    One row / entity within the database
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'abstract': True,
         'from_schema': 'https://carrollaboratory.github.io/kif-fhir-input',
         'title': 'Record'})

    id: str = Field(default=..., title="ID", description="""Global ID for this record""", json_schema_extra = { "linkml_meta": {'domain_of': ['Record']} })
    external_id: Optional[list[str]] = Field(default=[], title="External Identifiers", description="""Other identifiers for this entity, eg, from the submitting study or in systems link dbGaP""", json_schema_extra = { "linkml_meta": {'domain_of': ['HasExternalId']} })


# Model rebuild
# see https://pydantic-docs.helpmanual.io/usage/models/#rebuilding-a-model
AssociatedParty.model_rebuild()
Period.model_rebuild()
PractitionerRole.model_rebuild()
HasExternalId.model_rebuild()
Practitioner.model_rebuild()
Institution.model_rebuild()
Record.model_rebuild()
