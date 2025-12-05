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
                 'practitioner',
                 'research_study',
                 'research_study_collection'],
     'license': 'MIT',
     'name': 'kfi-fhir-input',
     'prefixes': {'hl7_rsp_org_type': {'prefix_prefix': 'hl7_rsp_org_type',
                                       'prefix_reference': 'http://hl7.org/fhir/research-study-party-organization-type'},
                  'hl7_rsp_role': {'prefix_prefix': 'hl7_rsp_role',
                                   'prefix_reference': 'http://hl7.org/fhir/research-study-party-role'},
                  'hl7_study_design': {'prefix_prefix': 'hl7_study_design',
                                       'prefix_reference': 'https://hl7.org/fhir/codesystem-study-design'},
                  'hl7_study_status': {'prefix_prefix': 'hl7_study_status',
                                       'prefix_reference': 'https://hl7.org/fhir/R4/codesystem-research-study-status'},
                  'kfi': {'prefix_prefix': 'kfi',
                          'prefix_reference': 'https://carrollaboratory.github.io/kfi-fhir-input/'},
                  'kfi_fhir_sparks': {'prefix_prefix': 'kfi_fhir_sparks',
                                      'prefix_reference': 'https://carrollaboratory.github.io/kif-fhir-input'},
                  'linkml': {'prefix_prefix': 'linkml',
                             'prefix_reference': 'https://w3id.org/linkml/'},
                  'ncpi_collection_type': {'prefix_prefix': 'ncpi_collection_type',
                                           'prefix_reference': 'https://nih-ncpi.github.io/ncpi-fhir-ig-2/CodeSystem/collection-type'}},
     'see_also': ['https://carrollaboratory.github.io/kif-fhir-input'],
     'source_file': 'src/kfi_fhir_input/schema/kfi_fhir_input.yaml',
     'title': 'KF/Include FHIR Input Model'} )

class EnumResearchStudyPartyOrganizationType(str, Enum):
    """
    Research Study Party Organization Type
    """
    NIH = "nih"
    FDA = "fda"
    Academic = "academic"
    Government = "government"
    Nonprofit = "nonprofit"
    Industry = "industry"


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


class EnumStudyStatus(str, Enum):
    """
    Codes indicating the study's current status
    """
    Active = "active"
    """
    Study is opened for accrual.
    """
    Administratively_Completed = "administratively_completed"
    """
    Study is completed prematurely and will not resume; patients are no longer examined nor treated.
    """
    Approved = "approved"
    Closed_to_Accrual = "closed_to_accrual"
    Closed_to_Accrual_and_Intervention = "closed_to_accrual_and_intervention"
    Completed = "completed"
    Disapproved = "disapproved"
    In_Review = "in_review"
    Temporarily_Closed_to_Accrual = "temporarily_closed_to_accrual"
    Temporarily_Closed_to_Accrual_and_Intervention = "temporarily_closed_to_accrual_and_intervention"
    Withdrawn = "withdrawn"


class EnumResearchCollectionType(str, Enum):
    """
    Research Study Collection Type
    """
    Consortium = "consortium"
    Program = "program"
    User_Defined = "user_defined"



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
    period_id: Optional[str] = Field(default=None, title="Period ID", description="""Reference to a time period which defines a Start and End datatime period.""", json_schema_extra = { "linkml_meta": {'annotations': {'db_column': {'tag': 'db_column', 'value': 'period_id'},
                         'target_slot': {'tag': 'target_slot', 'value': 'id'}},
         'domain_of': ['AssociatedParty', 'PractitionerRole']} })
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
    description: Optional[str] = Field(default=None, title="Description", description="""More details associated with the given resource""", json_schema_extra = { "linkml_meta": {'domain_of': ['Practitioner', 'ResearchStudy', 'ResearchStudyCollection']} })
    practitioner_title: Optional[str] = Field(default=None, title="Title", description="""The title of the Investigator, eg, \"Assistant Professor\"""", json_schema_extra = { "linkml_meta": {'domain_of': ['Practitioner']} })
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


class ResearchStudy(HasExternalId):
    """
    The NCPI Research Study FHIR resource represents an individual research effort and acts as a grouper or “container” for that effort’s study participants and their related data files.
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'annotations': {'fhir_resource': {'tag': 'fhir_resource',
                                           'value': 'ResearchStudy'}},
         'from_schema': 'https://carrollaboratory.github.io/kfi-fhir-input/research_study',
         'title': 'Research Study'})

    study_title: Optional[str] = Field(default=None, title="Title", description="""Research Study's formal title.""", json_schema_extra = { "linkml_meta": {'domain_of': ['ResearchStudy']} })
    parent_study_id: Optional[str] = Field(default=None, title="Parent Study", description="""ID For Parent Study if this is a substudy""", json_schema_extra = { "linkml_meta": {'annotations': {'db_column': {'tag': 'db_column', 'value': 'parent_study_id'},
                         'target_slot': {'tag': 'target_slot',
                                         'value': 'research_study_id'}},
         'domain_of': ['ResearchStudy']} })
    study_focus: Optional[list[str]] = Field(default=[], title="Study Focus", description="""The primary, non-disease focus(es) of the study. This can include terms related to intervention, drug, device, or other focus.""", json_schema_extra = { "linkml_meta": {'domain_of': ['ResearchStudy']} })
    description: Optional[str] = Field(default=None, title="Description", description="""More details associated with the given resource""", json_schema_extra = { "linkml_meta": {'domain_of': ['Practitioner', 'ResearchStudy', 'ResearchStudyCollection']} })
    study_condition: Optional[list[str]] = Field(default=[], title="Study Condition", description="""The primary focus(es) of the study. This is specific to the disease. MeSH terms are preferred.""", json_schema_extra = { "linkml_meta": {'domain_of': ['ResearchStudy']} })
    study_acknowledgement: Optional[list[str]] = Field(default=[], title="Study Acknowledgement", description="""Any attribution or acknowledgements relevant to the study. This can include but is not limited to funding sources, organizational affiliations or sponsors.""", json_schema_extra = { "linkml_meta": {'domain_of': ['ResearchStudy']} })
    study_status: EnumStudyStatus = Field(default=..., title="Study Status", description="""The current state of the study.""", json_schema_extra = { "linkml_meta": {'domain_of': ['ResearchStudy']} })
    study_design: Optional[list[str]] = Field(default=[], title="Study Design", description="""Study Design and Study Type ([example ValueSet can be found here](https://hl7.org/fhir/valueset-study-design.html))""", json_schema_extra = { "linkml_meta": {'domain_of': ['ResearchStudy']} })
    study_personnel: list[str] = Field(default=..., title="Study Personnel", description="""Every study must have at least one Primary Contact defined. Additional personnel such as Primary Investigator(s), Administrator(s), Collaborator(s) or other roles may also be included. If there are no appropriate individuals who can serve as primary contact for a study, an organization may be provided.""", json_schema_extra = { "linkml_meta": {'domain_of': ['ResearchStudy']} })
    research_study_id: str = Field(default=..., title="Research Study ID", description="""The Global ID for the Research Study.""", json_schema_extra = { "linkml_meta": {'domain_of': ['ResearchStudy']} })
    external_id: Optional[list[str]] = Field(default=[], title="External Identifiers", description="""Other identifiers for this entity, eg, from the submitting study or in systems link dbGaP""", json_schema_extra = { "linkml_meta": {'domain_of': ['HasExternalId']} })


class Record(HasExternalId):
    """
    One row / entity within the database
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'abstract': True,
         'from_schema': 'https://carrollaboratory.github.io/kif-fhir-input',
         'title': 'Record'})

    id: str = Field(default=..., title="ID", description="""Unique Identifier for a table entry. This is probably not the Global ID""", json_schema_extra = { "linkml_meta": {'domain_of': ['Record']} })
    external_id: Optional[list[str]] = Field(default=[], title="External Identifiers", description="""Other identifiers for this entity, eg, from the submitting study or in systems link dbGaP""", json_schema_extra = { "linkml_meta": {'domain_of': ['HasExternalId']} })


class AssociatedParty(Record):
    """
    Sponsors, collaborators, and other parties affiliated with a research study.
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'annotations': {'fhir_resource': {'tag': 'fhir_resource',
                                           'value': 'https://nih-ncpi.github.io/ncpi-fhir-ig-2/StructureDefinition/research-study-associated-party'}},
         'from_schema': 'https://carrollaboratory.github.io/kfi-fhir-input/associated_party',
         'title': 'Associated Party'})

    name: Optional[str] = Field(default=None, title="Name", description="""Name of the entity.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Practitioner', 'AssociatedParty', 'Institution']} })
    role: Optional[EnumResearchStudyPartyRole] = Field(default=None, title="Role", description="""Research Study Party Role""", json_schema_extra = { "linkml_meta": {'domain_of': ['AssociatedParty']} })
    period_id: Optional[str] = Field(default=None, title="Period ID", description="""Reference to a time period which defines a Start and End datatime period.""", json_schema_extra = { "linkml_meta": {'annotations': {'db_column': {'tag': 'db_column', 'value': 'period_id'},
                         'target_slot': {'tag': 'target_slot', 'value': 'id'}},
         'domain_of': ['AssociatedParty', 'PractitionerRole']} })
    classifier: Optional[list[EnumResearchStudyPartyOrganizationType]] = Field(default=[], title="Classifier", description="""Research Study Party Organization Type (what type of institution is party)""", json_schema_extra = { "linkml_meta": {'domain_of': ['AssociatedParty']} })
    party: Optional[str] = Field(default=None, title="Associated Party", description="""Individual or organization associated with study""", json_schema_extra = { "linkml_meta": {'any_of': [{'range': 'PractitionerRole'}], 'domain_of': ['AssociatedParty']} })
    id: str = Field(default=..., title="ID", description="""Unique Identifier for a table entry. This is probably not the Global ID""", json_schema_extra = { "linkml_meta": {'domain_of': ['Record']} })
    external_id: Optional[list[str]] = Field(default=[], title="External Identifiers", description="""Other identifiers for this entity, eg, from the submitting study or in systems link dbGaP""", json_schema_extra = { "linkml_meta": {'domain_of': ['HasExternalId']} })


class Period(Record):
    """
    Time period associated with some FHIR resource
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'from_schema': 'https://carrollaboratory.github.io/kfi-fhir-input/period',
         'title': 'Period'})

    start: Optional[date] = Field(default=None, title="Start", description="""Start attribute for a FHIR period data type.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Period']} })
    end: Optional[date] = Field(default=None, title="End", description="""End attribute for a FHIR period data type.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Period']} })
    id: str = Field(default=..., title="ID", description="""Unique Identifier for a table entry. This is probably not the Global ID""", json_schema_extra = { "linkml_meta": {'domain_of': ['Record']} })
    external_id: Optional[list[str]] = Field(default=[], title="External Identifiers", description="""Other identifiers for this entity, eg, from the submitting study or in systems link dbGaP""", json_schema_extra = { "linkml_meta": {'domain_of': ['HasExternalId']} })


class ResearchStudyCollection(HasExternalId):
    """
    Collections of research data including, but not limited, to Consortia, Programs, adhoc collections of Studies and datasets among other types of collections.
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'annotations': {'fhir_resource': {'tag': 'fhir_resource', 'value': 'List'}},
         'from_schema': 'https://carrollaboratory.github.io/kfi-fhir-input/research-study-collection',
         'title': 'Research Study Collection'})

    collection_title: str = Field(default=..., title="Collection Title", description="""The collection's title.""", json_schema_extra = { "linkml_meta": {'domain_of': ['ResearchStudyCollection']} })
    research_study_collection_type: EnumResearchCollectionType = Field(default=..., title="Research Study Collection Type", description="""The type of collection being described.""", json_schema_extra = { "linkml_meta": {'domain_of': ['ResearchStudyCollection']} })
    label: Optional[list[str]] = Field(default=[], title="Label", description="""Alias such as acronym and alternate names.""", json_schema_extra = { "linkml_meta": {'domain_of': ['ResearchStudyCollection']} })
    website: Optional[str] = Field(default=None, title="Website", description="""URL describing the entity this represents. This can include a formal website, such as the Entity's website, or to an online document describing the entity.""", json_schema_extra = { "linkml_meta": {'domain_of': ['ResearchStudyCollection']} })
    research_study_collection_member_id: list[str] = Field(default=..., title="Research Study Collection Member ID", description="""ID associated with a member of the collection (Research Study, Dataset, etc)""", json_schema_extra = { "linkml_meta": {'annotations': {'target_slot': {'tag': 'target_slot',
                                         'value': 'research_study_id'}},
         'domain_of': ['ResearchStudyCollection']} })
    research_study_collection_id: str = Field(default=..., title="Research Study Collection ID", description="""Global ID for this record""", json_schema_extra = { "linkml_meta": {'domain_of': ['ResearchStudyCollection']} })
    description: Optional[str] = Field(default=None, title="Description", description="""The description of the collection.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Practitioner', 'ResearchStudy', 'ResearchStudyCollection']} })
    external_id: Optional[list[str]] = Field(default=[], title="External Identifiers", description="""Other identifiers for this entity, eg, from the submitting study or in systems link dbGaP""", json_schema_extra = { "linkml_meta": {'domain_of': ['HasExternalId']} })


# Model rebuild
# see https://pydantic-docs.helpmanual.io/usage/models/#rebuilding-a-model
PractitionerRole.model_rebuild()
HasExternalId.model_rebuild()
Practitioner.model_rebuild()
Institution.model_rebuild()
ResearchStudy.model_rebuild()
Record.model_rebuild()
AssociatedParty.model_rebuild()
Period.model_rebuild()
ResearchStudyCollection.model_rebuild()
