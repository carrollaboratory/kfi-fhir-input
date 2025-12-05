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
                 'access_policy',
                 'research_study_collection'],
     'license': 'MIT',
     'name': 'kfi-fhir-input',
     'prefixes': {'duo': {'prefix_prefix': 'duo',
                          'prefix_reference': 'http://purl.obolibrary.org/obo/duo.owl'},
                  'hl7_consent_scope': {'prefix_prefix': 'hl7_consent_scope',
                                        'prefix_reference': 'http://terminology.hl7.org/CodeSystem/consentscope'},
                  'hl7_consent_state_codes': {'prefix_prefix': 'hl7_consent_state_codes',
                                              'prefix_reference': 'http://hl7.org/fhir/consent-state-codes'},
                  'hl7_list_status': {'prefix_prefix': 'hl7_list_status',
                                      'prefix_reference': 'https://hl7.org/fhir/R4/codesystem-list-status'},
                  'hl7_rsp_org_type': {'prefix_prefix': 'hl7_rsp_org_type',
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
                                           'prefix_reference': 'https://nih-ncpi.github.io/ncpi-fhir-ig-2/CodeSystem/collection-type'},
                  'ncpi_data_access_code': {'prefix_prefix': 'ncpi_data_access_code',
                                            'prefix_reference': 'https://nih-ncpi.github.io/ncpi-fhir-ig-2/CodeSystem/research-data-access-code/'},
                  'ncpi_data_access_type': {'prefix_prefix': 'ncpi_data_access_type',
                                            'prefix_reference': 'https://nih-ncpi.github.io/ncpi-fhir-ig-2/CodeSystem-research-data-access-type'}},
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


class EnumAccessPolicyCode(str, Enum):
    """
    Type of research use case allowed
    """
    GRU = "gru"
    """
    General Research Use
    """
    HMB = "hmb"
    """
    Health/Medical/Biomedical
    """
    DS = "ds"
    """
    Disease-Specific (Disease/Trait/Exposure)
    """
    IRB = "irb"
    """
    IRB Approval Required
    """
    PUB = "pub"
    """
    Publication Required
    """
    COL = "col"
    """
    Collaboration Required
    """
    NPU = "npu"
    """
    Not-for-profit use only
    """
    MDS = "mds"
    """
    Methods
    """
    GSO = "gso"
    """
    Genetic Studies only
    """
    GSR = "gsr"
    """
    Genomic Summary Results
    """
    RD = "rd"
    """
    Related Diseases
    """
    no_restriction = "duo_0000004"
    """
    This data use permission indicates there is no restriction on use.
    """
    general_research_use = "duo_0000042"
    """
    This data use permission indicates that use is allowed for general research use for any research purpose.
    """
    health_or_medical_or_biomedical_research = "duo_0000006"
    """
    This data use permission indicates that use is allowed for health/medical/biomedical purposes; does not include the study of population origins or ancestry.
    """
    disease_specific_research = "duo_0000007"
    """
    This data use permission indicates that use is allowed provided it is related to the specified disease.
    """
    population_origins_or_ancestry_research_only = "duo_0000011"
    """
    This data use permission indicates that use of the data is limited to the study of population origins or ancestry.
    """
    research_specific_restrictions = "duo_0000012"
    """
    This data use modifier indicates that use is limited to studies of a certain research type.
    """
    no_general_methods_research = "duo_0000015"
    """
    This data use modifier indicates that use does not allow methods development research (e.g., development of software or algorithms).
    """
    genetic_studies_only = "duo_0000016"
    """
    This data use modifier indicates that use is limited to genetic studies only (i.e., studies that include genotype research alone or both genotype and phenotype research, but not phenotype research exclusively)
    """
    not_for_profit_non_commercial_use_only = "duo_0000018"
    """
    This data use modifier indicates that use of the data is limited to not-for-profit organizations and not-for-profit use, non-commercial use.
    """
    publication_required = "duo_0000019"
    """
    This data use modifier indicates that requestor agrees to make results of studies using the data available to the larger scientific community.
    """
    collaboration_required = "duo_0000020"
    """
    This data use modifier indicates that the requestor must agree to collaboration with the primary study investigator(s).
    """
    ethics_approval_required = "duo_0000021"
    """
    This data use modifier indicates that the requestor must provide documentation of local IRB/ERB approval.
    """
    geographical_restriction = "duo_0000022"
    """
    This data use modifier indicates that use is limited to within a specific geographic region.
    """
    publication_moratorium = "duo_0000024"
    """
    This data use modifier indicates that requestor agrees not to publish results of studies until a specific date.
    """
    time_limit_on_use = "duo_0000025"
    """
    This data use modifier indicates that use is approved for a specific number of months.
    """
    user_specific_restriction = "duo_0000026"
    """
    This data use modifier indicates that use is limited to use by approved users.
    """
    project_specific_restriction = "duo_0000027"
    """
    This data use modifier indicates that use is limited to use within an approved project.
    """
    institution_specific_restriction = "duo_0000028"
    """
    This data use modifier indicates that use is limited to use within an approved institution.
    """
    return_to_database_or_resource = "duo_0000029"
    """
    This data use modifier indicates that the requestor must return derived/enriched data to the database/resource.
    """
    clinical_care_use = "duo_0000043"
    """
    This data use modifier indicates that use is allowed for clinical use and care.
    """
    population_origins_or_ancestry_research_prohibited = "duo_0000044"
    """
    This data use modifier indicates use for purposes of population, origin, or ancestry research is prohibited.
    """
    not_for_profit_organisation_use_only = "duo_0000045"
    """
    This data use modifier indicates that use of the data is limited to not-for-profit organisations.
    """
    non_commercial_use_only = "duo_0000046"
    """
    This data use modifier indicates that use of the data is limited to not-for-profit use.
    """


class EnumConsentScope(str, Enum):
    """
    The four anticipated uses for the Consent Resource.
    """
    Advanced_Care_Directive = "adr"
    Research = "research"
    Patient_Privacy = "patient_privacy"
    Treatment = "treatment"


class EnumConsentStateCodes(str, Enum):
    """
    Indicates the state of the consent.
    """
    Draft = "draft"
    Proposed = "proposed"
    Active = "active"
    Rejected = "rejected"
    Inactive = "inactive"
    Entered_in_Error = "entered_in_error"


class EnumDataAccessType(str, Enum):
    """
    Enumerated list of access type codes such as 'Open Access', 'Registered Access' and 'Controlled Access'
    """
    Open_Access = "open"
    Registered = "registered"
    Controlled = "controlled"
    GSR_Restricted = "gsr_restricted"
    GSR_Allowed = "gsr_allowed"


class EnumResearchCollectionType(str, Enum):
    """
    Research Study Collection Type
    """
    Consortium = "consortium"
    Program = "program"
    User_Defined = "user_defined"


class EnumCollectionStatus(str, Enum):
    """
    The current state of the collection
    """
    Current = "current"
    Retired = "retired"



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


class AccessPolicy(ConfiguredBaseModel):
    """
    Limitations and/or requirements that define how a user may gain access to a particular set of data.
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'annotations': {'fhir_resource': {'tag': 'fhir_resource',
                                           'value': 'https://nih-ncpi.github.io/ncpi-fhir-ig-2/StructureDefinition/ncpi-research-access-policy'}},
         'from_schema': 'https://carrollaboratory.github.io/kfi-fhir-input/access-policy',
         'title': 'Access Policy'})

    description: Optional[str] = Field(default=None, title="Description", description="""More details associated with the given resource""", json_schema_extra = { "linkml_meta": {'domain_of': ['Practitioner',
                       'ResearchStudy',
                       'AccessPolicy',
                       'ResearchStudyCollection']} })
    data_access_type: EnumDataAccessType = Field(default=..., title="Access Type", description="""Type of access restrictions on file downloads ( open | registered | controlled )""", json_schema_extra = { "linkml_meta": {'domain_of': ['AccessPolicy']} })
    website: Optional[str] = Field(default=None, title="Website", description="""URL describing the entity this represents. This can include a formal website, such as the Entity's website, or to an online document describing the entity.""", json_schema_extra = { "linkml_meta": {'domain_of': ['AccessPolicy', 'ResearchStudyCollection']} })
    consent_scope: EnumConsentScope = Field(default=..., title="Consent Scope", description="""Which of the four areas this resource covers (extensible)""", json_schema_extra = { "linkml_meta": {'domain_of': ['AccessPolicy']} })
    access_policy_code: list[EnumAccessPolicyCode] = Field(default=..., title="Access Policy Code", description="""A classification of the type of consents found in a consent statement.""", json_schema_extra = { "linkml_meta": {'domain_of': ['AccessPolicy']} })
    disease_limitation: Optional[str] = Field(default=None, description="""Disease Use Limitations""", json_schema_extra = { "linkml_meta": {'domain_of': ['AccessPolicy']} })
    access_policy_id: str = Field(default=..., title="Access Policy ID", description="""Access policy communicates the limitations and/or requirements that define how a user may gain access to a particular set of data.""", json_schema_extra = { "linkml_meta": {'domain_of': ['AccessPolicy']} })
    status: EnumConsentStateCodes = Field(default=..., title="Status", description="""Indicates the state of the consent.""", json_schema_extra = { "linkml_meta": {'domain_of': ['AccessPolicy']} })


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
    description: Optional[str] = Field(default=None, title="Description", description="""More details associated with the given resource""", json_schema_extra = { "linkml_meta": {'domain_of': ['Practitioner',
                       'ResearchStudy',
                       'AccessPolicy',
                       'ResearchStudyCollection']} })
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
    description: Optional[str] = Field(default=None, title="Description", description="""More details associated with the given resource""", json_schema_extra = { "linkml_meta": {'domain_of': ['Practitioner',
                       'ResearchStudy',
                       'AccessPolicy',
                       'ResearchStudyCollection']} })
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
    website: Optional[str] = Field(default=None, title="Website", description="""URL describing the entity this represents. This can include a formal website, such as the Entity's website, or to an online document describing the entity.""", json_schema_extra = { "linkml_meta": {'domain_of': ['AccessPolicy', 'ResearchStudyCollection']} })
    collection_status: EnumCollectionStatus = Field(default=..., title="Collection Status", description="""The current state of the collection""", json_schema_extra = { "linkml_meta": {'domain_of': ['ResearchStudyCollection']} })
    research_study_collection_member_id: list[str] = Field(default=..., title="Research Study Collection Member ID", description="""ID associated with a member of the collection (Research Study, Dataset, etc)""", json_schema_extra = { "linkml_meta": {'annotations': {'target_slot': {'tag': 'target_slot',
                                         'value': 'research_study_id'}},
         'domain_of': ['ResearchStudyCollection']} })
    research_study_collection_id: str = Field(default=..., title="Research Study Collection ID", description="""Global ID for this record""", json_schema_extra = { "linkml_meta": {'domain_of': ['ResearchStudyCollection']} })
    description: Optional[str] = Field(default=None, title="Description", description="""The description of the collection.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Practitioner',
                       'ResearchStudy',
                       'AccessPolicy',
                       'ResearchStudyCollection']} })
    external_id: Optional[list[str]] = Field(default=[], title="External Identifiers", description="""Other identifiers for this entity, eg, from the submitting study or in systems link dbGaP""", json_schema_extra = { "linkml_meta": {'domain_of': ['HasExternalId']} })


# Model rebuild
# see https://pydantic-docs.helpmanual.io/usage/models/#rebuilding-a-model
PractitionerRole.model_rebuild()
AccessPolicy.model_rebuild()
HasExternalId.model_rebuild()
Practitioner.model_rebuild()
Institution.model_rebuild()
ResearchStudy.model_rebuild()
Record.model_rebuild()
AssociatedParty.model_rebuild()
Period.model_rebuild()
ResearchStudyCollection.model_rebuild()
