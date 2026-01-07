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
     'id': 'https://carrollaboratory.github.io/kfi-fhir-input',
     'imports': ['linkml:types',
                 'access_policy',
                 'relative_date_time',
                 'age_at',
                 'participant_assertion',
                 'practitioner',
                 'associated_party',
                 'institution',
                 'participant',
                 'person',
                 'period',
                 'practitioner_role',
                 'practitioner',
                 'study_membership',
                 'research_study',
                 'research_study_collection',
                 'sample',
                 'file',
                 'file_location'],
     'license': 'MIT',
     'name': 'kfi-fhir-input',
     'prefixes': {'cdc_rec': {'prefix_prefix': 'cdc_rec',
                              'prefix_reference': 'https://phinvads.cdc.gov/baseStu3/CodeSystem/PH_RaceAndEthnicity_CDC'},
                  'cdc_unk': {'prefix_prefix': 'cdc_unk',
                              'prefix_reference': 'https://vsac.nlm.nih.gov/valueset/2.16.840.1.113762.1.4.1021.103/expansion'},
                  'duo': {'prefix_prefix': 'duo',
                          'prefix_reference': 'http://purl.obolibrary.org/obo/duo.owl'},
                  'edam': {'prefix_prefix': 'edam',
                           'prefix_reference': 'https://edamontology.org'},
                  'fluff': {'prefix_prefix': 'fluff',
                            'prefix_reference': 'https://fluffy.cat.onto/terms'},
                  'hl7_consent_scope': {'prefix_prefix': 'hl7_consent_scope',
                                        'prefix_reference': 'http://terminology.hl7.org/CodeSystem/consentscope'},
                  'hl7_consent_state_codes': {'prefix_prefix': 'hl7_consent_state_codes',
                                              'prefix_reference': 'http://hl7.org/fhir/consent-state-codes'},
                  'hl7_list_status': {'prefix_prefix': 'hl7_list_status',
                                      'prefix_reference': 'https://hl7.org/fhir/R4/codesystem-list-status'},
                  'hl7_null': {'prefix_prefix': 'hl7_null',
                               'prefix_reference': 'http://terminology.hl7.org/CodeSystem/v3-NullFlavor'},
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
                  'ncpi_cond_type': {'prefix_prefix': 'ncpi_cond_type',
                                     'prefix_reference': 'https://nih-ncpi.github.io/ncpi-fhir-ig-2/CodeSystem/condition-type/'},
                  'ncpi_data_access_code': {'prefix_prefix': 'ncpi_data_access_code',
                                            'prefix_reference': 'https://nih-ncpi.github.io/ncpi-fhir-ig-2/CodeSystem/research-data-access-code/'},
                  'ncpi_data_access_type': {'prefix_prefix': 'ncpi_data_access_type',
                                            'prefix_reference': 'https://nih-ncpi.github.io/ncpi-fhir-ig-2/CodeSystem-research-data-access-type'},
                  'ncpi_dob_method': {'prefix_prefix': 'ncpi_dob_method',
                                      'prefix_reference': 'https://nih-ncpi.github.io/ncpi-fhir-ig-2/CodeSystem/research-data-date-of-birth-method'},
                  'ncpi_patient_knowledge_source': {'prefix_prefix': 'ncpi_patient_knowledge_source',
                                                    'prefix_reference': 'https://nih-ncpi.github.io/ncpi-fhir-ig-2/CodeSystem/patient-knowledge-source'},
                  'ncpi_sample_availability': {'prefix_prefix': 'ncpi_sample_availability',
                                               'prefix_reference': 'https://nih-ncpi.github.io/ncpi-fhir-ig-2/CodeSystem/biospecimen-availability'},
                  'obi': {'prefix_prefix': 'obi',
                          'prefix_reference': 'http://purl.obolibrary.org/obo/obi.owl'},
                  'ucum': {'prefix_prefix': 'ucum',
                           'prefix_reference': 'http://unitsofmeasure.org'},
                  'umls': {'prefix_prefix': 'umls',
                           'prefix_reference': 'https://uts.nlm.nih.gov/uts/umls/concept'},
                  'usc_birthsex': {'prefix_prefix': 'usc_birthsex',
                                   'prefix_reference': 'http://terminology.hl7.org/CodeSystem/v3-AdministrativeGender'},
                  'w3c': {'prefix_prefix': 'w3c',
                          'prefix_reference': 'https://w3c.github.io/N3/ns/'}},
     'see_also': ['https://carrollaboratory.github.io/kfi-fhir-input'],
     'source_file': 'src/kfi_fhir_input/schema/kfi_fhir_input.yaml',
     'title': 'KF/Include FHIR Input Model'} )

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


class EnumOffsetType(str, Enum):
    """
    Offset Type
    """
    Days = "days"
    """
    The offset is represented in days
    """
    Years = "years"
    """
    The offset is represented in Years
    """


class EnumAgeValueType(str, Enum):
    """
    Describes where to look for the data (as value, code, range, etc)
    """
    Age = "age"
    """
    Age (must also be annotated with age units)
    """
    Age_as_Code = "code"
    """
    Age as Code (ages will be provided as coded values)
    """
    Age_Range = "age_range"
    """
    Age expressed as a range (relative date/time)
    """
    Date = "date"
    """
    Rather than an age, we have an actual date for the event's occurence
    """


class EnumEntityAsserter(str, Enum):
    """
    Who recorded this assertion about the Participant? This can support understanding the differences between self-report, doctor, trained research staff.
    """
    Self_Report = "self_report"
    """
    The participant reported the assertion
    """
    Doctor = "doctor"
    """
    Physician
    """
    Trained_Research_Staff = "staff"
    """
    Trained research staff
    """


class EnumAssertionType(str, Enum):
    """
    Provides options to describe the expressed semantics of a condition.
    """
    Phenotypic_Feature = "phenotypic_feature"
    """
    This is a phenotypic feature
    """
    disease = "disease"
    """
    Disease
    """
    comorbidity = "comorbidity"
    """
    Comorbidity
    """
    histology = "histology"
    """
    Histology
    """
    clinical_finding = "clinical_finding"
    """
    Clinical Finding
    """
    EHR_Billing_Code = "ehr_billing_code"
    """
    From an EHR billing record, which may indicate only investigation into a possible diagnosis.
    """
    Measurement = "measurement"
    """
    A measurement of some feature, eg, height or glucose.
    """


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


class EnumBirthSex(str, Enum):
    """
    Codes for assigning sex at birth as specified by the Office of the National Coordinator for Health IT (ONC)
    """
    Female = "female"
    """
    Female
    """
    Male = "male"
    """
    Male
    """
    asked_but_unknown = "asku"
    """
    Information was sought but not found (e.g., patient was asked but didn't know)
    """
    other = "oth"
    """
    **Description:**The actual value is not a member of the set of permitted data values in the constrained value domain of a variable. (e.g., concept not provided by required code system).
    Usage Notes: This flavor and its specializations are most commonly used with the CD datatype and its flavors. However, it may apply to *any* datatype where the constraints of the type are tighter than can be conveyed. For example, a PQ that is for a true measured amount whose units are not supported in UCUM, a need to convey a REAL when the type has been constrained to INT, etc.
    With coded datatypes, this null flavor may only be used if the vocabulary binding has a coding strength of CNE. By definition, all local codes and original text are part of the value set if the coding strength is CWE.
    """
    Unknown = "unk"
    """
    *Description:**A proper value is applicable, but not known.
    Usage Notes: This means the actual value is not known. If the only thing that is unknown is how to properly express the value in the necessary constraints (value set, datatype, etc.), then the OTH or UNC flavor should be used. No properties should be included for a datatype with this property unless:
    Those properties themselves directly translate to a semantic of 'unknown'. (E.g. a local code sent as a translation that conveys 'unknown') Those properties further qualify the nature of what is unknown. (E.g. specifying a use code of 'H' and a URL prefix of 'tel:' to convey that it is the home phone number that is unknown.)
    """


class EnumRace(str, Enum):
    """
    OMB Codes describing race.
    """
    American_Indian_or_Alaskan_Native = "american_indian_or_alaskan_native"
    Asian = "asian"
    Black_or_African_American = "black_or_african_american"
    Native_Hawaiian_or_Other_Pacific_Islander = "native_hawaiian_or_pacific_islander"
    White = "white"
    Other_Race = "other_race"
    unknown = "unknown"
    asked_but_unknown = "asked_but_unknown"


class EnumEthnicity(str, Enum):
    """
    OMB Codes describing Hispanic or Latino ethnicity.
    """
    hispanic_or_latino = "hispanic_or_latino"
    """
    Hispanic or Latino
    """
    not_hispanic_or_latino = "not_hispanic_or_latino"
    """
    Not Hispanic or Latino
    """
    unknown = "unknown"
    """
    unknown
    """
    asked_but_unknown = "asked_but_unknown"
    """
    asked but unknown
    """


class EnumPopulation(str):
    """
    Code describing the population (CDC). This should be one of the codes from the [CDC Race codes](https://hl7.org/fhir/us/core/STU6.1/ValueSet-detailed-race.html).
    """
    pass


class EnumDobMethod(str, Enum):
    """
    Enumerations for how DOB was constructed
    """
    exact = "exact"
    """
    Exact
    """
    year_only = "year_only"
    """
    Year Only
    """
    shifted = "shifted"
    """
    Shifted
    """
    decade_only = "decade_only"
    """
    Decade Only
    """
    other = "other"
    """
    Other
    """


class EnumPatientKnowledgeSource(str, Enum):
    """
    The source of the knowledge represented in a Patient resource.
    """
    Traditional = "traditional"
    """
    The knowledge comes from traditional sources like a form filled out by a patient or information copied from an external traditional source like government records.
    """
    Inferred = "inferred"
    """
    The knowledge is inferred from indirect evidence. For example, the existence of one patient's mother can be inferred from the existence of the patient.
    """


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


class EnumCollectionStatus(str, Enum):
    """
    The current state of the collection
    """
    Current = "current"
    Retired = "retired"


class EnumSpecimenAvailability(str, Enum):
    """
    Can this sample be requested for further analysis
    """
    Available = "available"
    """
    Specimen is currently available
    """
    Unavailable = "unavailable"
    """
    Specimen is currently unavailable
    """


class EnumFileMetaDataType(str, Enum):
    """
    Identify the type of profile to use
    """
    BAMSOLIDUSCRAM = "bam_cram"
    """
    Bam or Cram file
    """
    FASTQ = "fastq"
    """
    FASTQ File
    """
    MAF_LEFT_PARENTHESISSomatic_MutationRIGHT_PARENTHESIS_file = "maf"
    """
    MAF (Somatic Mutation)
    """
    Proteomics_file = "proteomics"
    """
    Proteomics file
    """
    VCF_LEFT_PARENTHESISand_gVCFRIGHT_PARENTHESIS_file = "vcf"
    """
    GC or gVCF file
    """



class AccessPolicy(ConfiguredBaseModel):
    """
    Limitations and/or requirements that define how a user may gain access to a particular set of data.
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'annotations': {'fhir_resource': {'tag': 'fhir_resource',
                                           'value': 'https://nih-ncpi.github.io/ncpi-fhir-ig-2/StructureDefinition/ncpi-research-access-policy'}},
         'from_schema': 'https://carrollaboratory.github.io/kfi-fhir-input/access-policy',
         'title': 'Access Policy'})

    description: Optional[str] = Field(default=None, title="Description", description="""More details associated with the given resource""", json_schema_extra = { "linkml_meta": {'domain_of': ['AccessPolicy',
                       'Practitioner',
                       'ResearchStudy',
                       'ResearchStudyCollection',
                       'NCPIFile']} })
    data_access_type: EnumDataAccessType = Field(default=..., title="Access Type", description="""Type of access restrictions on file downloads ( open | registered | controlled )""", json_schema_extra = { "linkml_meta": {'annotations': {'fhir_extension': {'tag': 'fhir_extension',
                                            'value': 'https://nih-ncpi.github.io/ncpi-fhir-ig-2/StructureDefinition-access-type'},
                         'fhir_profile': {'tag': 'fhir_profile',
                                          'value': 'https://nih-ncpi.github.io/ncpi-fhir-ig-2/StructureDefinition/ncpi-research-access-policy'},
                         'fhir_resource': {'tag': 'fhir_resource', 'value': 'Consent'}},
         'domain_of': ['AccessPolicy']} })
    website: Optional[str] = Field(default=None, title="Website", description="""URL describing the entity this represents. This can include a formal website, such as the Entity's website, or to an online document describing the entity.""", json_schema_extra = { "linkml_meta": {'domain_of': ['AccessPolicy', 'ResearchStudyCollection']} })
    consent_scope: EnumConsentScope = Field(default=..., title="Consent Scope", description="""Which of the four areas this resource covers (extensible)""", json_schema_extra = { "linkml_meta": {'annotations': {'fhir_element': {'tag': 'fhir_element', 'value': 'scope'},
                         'fhir_profile': {'tag': 'fhir_profile',
                                          'value': 'https://nih-ncpi.github.io/ncpi-fhir-ig-2/StructureDefinition/ncpi-research-access-policy'},
                         'fhir_resource': {'tag': 'fhir_resource', 'value': 'Consent'}},
         'domain_of': ['AccessPolicy']} })
    access_policy_code: list[EnumAccessPolicyCode] = Field(default=..., title="Access Policy Code", description="""A classification of the type of consents found in a consent statement.""", json_schema_extra = { "linkml_meta": {'annotations': {'fhir_element': {'tag': 'fhir_element', 'value': 'category'},
                         'fhir_profile': {'tag': 'fhir_profile',
                                          'value': 'https://nih-ncpi.github.io/ncpi-fhir-ig-2/StructureDefinition/ncpi-research-access-policy'},
                         'fhir_resource': {'tag': 'fhir_resource', 'value': 'Consent'}},
         'domain_of': ['AccessPolicy']} })
    disease_limitation: Optional[str] = Field(default=None, description="""Disease Use Limitations""", json_schema_extra = { "linkml_meta": {'annotations': {'fhir_element': {'tag': 'fhir_element',
                                          'value': 'provision.purpose'},
                         'fhir_profile': {'tag': 'fhir_profile',
                                          'value': 'https://nih-ncpi.github.io/ncpi-fhir-ig-2/StructureDefinition/ncpi-research-access-policy'},
                         'fhir_resource': {'tag': 'fhir_resource', 'value': 'Consent'}},
         'domain_of': ['AccessPolicy']} })
    access_policy_id: str = Field(default=..., title="Access Policy Global ID (Consent)", description="""Access policy communicates the limitations and/or requirements that define how a user may gain access to a particular set of data.""", json_schema_extra = { "linkml_meta": {'domain_of': ['AccessPolicy', 'StudyMembership', 'FileLocation']} })
    status: EnumConsentStateCodes = Field(default=..., title="Status", description="""Indicates the state of the consent.""", json_schema_extra = { "linkml_meta": {'annotations': {'fhir_element': {'tag': 'fhir_element', 'value': 'status'},
                         'fhir_profile': {'tag': 'fhir_profile',
                                          'value': 'https://nih-ncpi.github.io/ncpi-fhir-ig-2/StructureDefinition/ncpi-research-access-policy'},
                         'fhir_resource': {'tag': 'fhir_resource', 'value': 'Consent'}},
         'domain_of': ['AccessPolicy']} })


class RelativeDateTime(ConfiguredBaseModel):
    """
    In FHIR, we can express events using relative date/times from the participant's DOB to avoid exposing sensitive information
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'from_schema': 'https://carrollaboratory.github.io/kfi-fhir-input/relative-date-time',
         'title': 'Relative Date Time'})

    id: str = Field(default=..., title="ID", description="""Unique Identifier for a table entry. This is probably not the Global ID""", json_schema_extra = { "linkml_meta": {'domain_of': ['RelativeDateTime', 'Record']} })
    offset: int = Field(default=..., title="Offset", description="""The point after the target being described. For ranges, this can be used for the starting point""", json_schema_extra = { "linkml_meta": {'domain_of': ['RelativeDateTime']} })
    offset_end: Optional[int] = Field(default=None, title="Offset End", description="""The end of a relative date/time range""", json_schema_extra = { "linkml_meta": {'domain_of': ['RelativeDateTime']} })
    offset_type: EnumOffsetType = Field(default=..., title="Offset Type", description="""What is the datatype associated with the offset (days, years, etc)""", json_schema_extra = { "linkml_meta": {'domain_of': ['RelativeDateTime']} })


class AgeAt(ConfiguredBaseModel):
    """
    These represent a flexible age value that could represent one of the following-Relative Age Offset, Age Range as Code, Date Range, DateTime
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'from_schema': 'https://carrollaboratory.github.io/kfi-fhir-input/age-at',
         'title': 'Age At'})

    value_type: EnumAgeValueType = Field(default=..., title="Value Type", description="""Age Value Type""", json_schema_extra = { "linkml_meta": {'domain_of': ['AgeAt']} })
    age: Optional[str] = Field(default=None, title="Age", description="""Age either numeric value or range""", json_schema_extra = { "linkml_meta": {'domain_of': ['AgeAt']} })
    age_code: Optional[str] = Field(default=None, title="Age Code", description="""Age expressed as an enumerated value representing an age category""", json_schema_extra = { "linkml_meta": {'domain_of': ['AgeAt']} })
    as_date: Optional[date] = Field(default=None, title="Age As Date", description="""Event Date (rather than age)""", json_schema_extra = { "linkml_meta": {'domain_of': ['AgeAt']} })


class ParticipantAssertion(ConfiguredBaseModel):
    """
    Assertion about a particular Participant. May include Conditions, Measurements, etc.
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'annotations': {'fhir_resource': {'tag': 'fhir_resource',
                                           'value': 'https://nih-ncpi.github.io/ncpi-fhir-ig-2/StructureDefinition/ncpi-participant-assertion'}},
         'from_schema': 'https://carrollaboratory.github.io/kfi-fhir-input/participant-assertion',
         'slot_usage': {'participant_id': {'annotations': {'fhir_element': {'tag': 'fhir_element',
                                                                            'value': 'category'},
                                                           'fhir_profile': {'tag': 'fhir_profile',
                                                                            'value': 'https://nih-ncpi.github.io/ncpi-fhir-ig-2/StructureDefinition/ncpi-participant-assertion'},
                                                           'fhir_resource': {'tag': 'fhir_resource',
                                                                             'value': 'Observation'}},
                                           'name': 'participant_id'}},
         'title': 'Participant Assertion'})

    participant_id: str = Field(default=..., title="Participant ID", description="""The Global ID for the Participant""", json_schema_extra = { "linkml_meta": {'annotations': {'fhir_element': {'tag': 'fhir_element', 'value': 'category'},
                         'fhir_profile': {'tag': 'fhir_profile',
                                          'value': 'https://nih-ncpi.github.io/ncpi-fhir-ig-2/StructureDefinition/ncpi-participant-assertion'},
                         'fhir_resource': {'tag': 'fhir_resource',
                                           'value': 'Observation'}},
         'domain_of': ['ParticipantAssertion',
                       'Participant',
                       'Person',
                       'StudyMembership',
                       'Sample',
                       'NCPIFile']} })
    age_at_event: Optional[AgeAt] = Field(default=None, title="Age At Event", description="""The date or age at which the event relating to this assertion occured.""", json_schema_extra = { "linkml_meta": {'annotations': {'fhir_element': {'tag': 'fhir_element',
                                          'value': 'component[ageAtEvent] or maybe '
                                                   'effectiveDateTime'},
                         'fhir_profile': {'tag': 'fhir_profile',
                                          'value': 'https://nih-ncpi.github.io/ncpi-fhir-ig-2/StructureDefinition/ncpi-participant-assertion'},
                         'fhir_resource': {'tag': 'fhir_resource',
                                           'value': 'Observation'}},
         'domain_of': ['ParticipantAssertion']} })
    age_at_assertion: Optional[AgeAt] = Field(default=None, title="Age At Assertion", description="""The date or age at which this condition is being asserted.""", json_schema_extra = { "linkml_meta": {'annotations': {'fhir_element': {'tag': 'fhir_element',
                                          'value': 'component[ageAtAssertion]'},
                         'fhir_profile': {'tag': 'fhir_profile',
                                          'value': 'https://nih-ncpi.github.io/ncpi-fhir-ig-2/StructureDefinition/ncpi-participant-assertion'},
                         'fhir_resource': {'tag': 'fhir_resource',
                                           'value': 'Observation'}},
         'domain_of': ['ParticipantAssertion']} })
    age_at_onset: Optional[AgeAt] = Field(default=None, title="Age At Onset", description="""The age of onset for this condition. Could be expressed with a term, an age, or an age range.""", json_schema_extra = { "linkml_meta": {'annotations': {'fhir_element': {'tag': 'fhir_element',
                                          'value': 'component[ageAtOnset]'},
                         'fhir_profile': {'tag': 'fhir_profile',
                                          'value': 'https://nih-ncpi.github.io/ncpi-fhir-ig-2/StructureDefinition/ncpi-participant-assertion'},
                         'fhir_resource': {'tag': 'fhir_resource',
                                           'value': 'Observation'}},
         'domain_of': ['ParticipantAssertion']} })
    age_at_resolution: Optional[AgeAt] = Field(default=None, title="Age At Resolution", description="""The age at which this condition was resolved, abated, or cured. Should be left empty in cases of current active status. Could be expressed with a term, an age, or an age range.""", json_schema_extra = { "linkml_meta": {'annotations': {'fhir_element': {'tag': 'fhir_element',
                                          'value': 'component[ageAtResolution]'},
                         'fhir_profile': {'tag': 'fhir_profile',
                                          'value': 'https://nih-ncpi.github.io/ncpi-fhir-ig-2/StructureDefinition/ncpi-participant-assertion'},
                         'fhir_resource': {'tag': 'fhir_resource',
                                           'value': 'Observation'}},
         'domain_of': ['ParticipantAssertion']} })
    entity_asserter: Optional[EnumEntityAsserter] = Field(default=None, title="Entity Asserter", description="""Who recorded this assertion about the Participant? This can support understanding the differences between self-report, doctor, trained research staff.""", json_schema_extra = { "linkml_meta": {'annotations': {'fhir_extension': {'tag': 'fhir_extension',
                                            'value': 'https://nih-ncpi.github.io/ncpi-fhir-ig-2/StructureDefinition/entity-asserter'},
                         'fhir_profile': {'tag': 'fhir_profile',
                                          'value': 'https://nih-ncpi.github.io/ncpi-fhir-ig-2/StructureDefinition/ncpi-participant-assertion'},
                         'fhir_resource': {'tag': 'fhir_resource',
                                           'value': 'Observation'}},
         'domain_of': ['ParticipantAssertion']} })
    other_condition_modifiers: Optional[str] = Field(default=None, title="Other Condition Modifiers", description="""Any additional modifiers for this condition, such as severity.""", json_schema_extra = { "linkml_meta": {'annotations': {'fhir_element': {'tag': 'fhir_element',
                                          'value': 'component[otherModifiers]'},
                         'fhir_profile': {'tag': 'fhir_profile',
                                          'value': 'https://nih-ncpi.github.io/ncpi-fhir-ig-2/StructureDefinition/ncpi-participant-assertion'},
                         'fhir_resource': {'tag': 'fhir_resource',
                                           'value': 'Observation'}},
         'domain_of': ['ParticipantAssertion']} })
    assertion_type: EnumAssertionType = Field(default=..., title="Assertion Type", description="""Describe the type of assertion being made.""", json_schema_extra = { "linkml_meta": {'annotations': {'fhir_element': {'tag': 'fhir_element', 'value': 'category'},
                         'fhir_profile': {'tag': 'fhir_profile',
                                          'value': 'https://nih-ncpi.github.io/ncpi-fhir-ig-2/StructureDefinition/ncpi-participant-assertion'},
                         'fhir_resource': {'tag': 'fhir_resource',
                                           'value': 'Observation'}},
         'domain_of': ['ParticipantAssertion']} })
    assertion_code: str = Field(default=..., title="Assertion Code", description="""The structured term defining the meaning of the assertion.""", json_schema_extra = { "linkml_meta": {'annotations': {'fhir_element': {'tag': 'fhir_element',
                                          'value': 'code.coding'},
                         'fhir_profile': {'tag': 'fhir_profile',
                                          'value': 'https://nih-ncpi.github.io/ncpi-fhir-ig-2/StructureDefinition/ncpi-participant-assertion'},
                         'fhir_resource': {'tag': 'fhir_resource',
                                           'value': 'Observation'}},
         'domain_of': ['ParticipantAssertion']} })
    assertion_text: Optional[str] = Field(default=None, title="Assertion Text", description="""Detailed description / free text about this assertion.""", json_schema_extra = { "linkml_meta": {'annotations': {'fhir_element': {'tag': 'fhir_element', 'value': 'code.text'},
                         'fhir_profile': {'tag': 'fhir_profile',
                                          'value': 'https://nih-ncpi.github.io/ncpi-fhir-ig-2/StructureDefinition/ncpi-participant-assertion'},
                         'fhir_resource': {'tag': 'fhir_resource',
                                           'value': 'Observation'}},
         'domain_of': ['ParticipantAssertion']} })
    assertion_source: Optional[str] = Field(default=None, title="Assertion Source", description="""Where or how was this this assertion about the Participant recorded? This can support understanding the differences between surveys, automated EHR extraction, manual chart abstraction, etc.""", json_schema_extra = { "linkml_meta": {'annotations': {'fhir_element': {'tag': 'fhir_element', 'value': 'method'},
                         'fhir_profile': {'tag': 'fhir_profile',
                                          'value': 'https://nih-ncpi.github.io/ncpi-fhir-ig-2/StructureDefinition/ncpi-participant-assertion'},
                         'fhir_resource': {'tag': 'fhir_resource',
                                           'value': 'Observation'}},
         'domain_of': ['ParticipantAssertion']} })
    value_code: Optional[str] = Field(default=None, title="Value Code", description="""Value as code""", json_schema_extra = { "linkml_meta": {'annotations': {'fhir_element': {'tag': 'fhir_element',
                                          'value': 'valueCodeableConcept'},
                         'fhir_profile': {'tag': 'fhir_profile',
                                          'value': 'https://nih-ncpi.github.io/ncpi-fhir-ig-2/StructureDefinition/ncpi-participant-assertion'},
                         'fhir_resource': {'tag': 'fhir_resource',
                                           'value': 'Observation'}},
         'domain_of': ['ParticipantAssertion']} })
    value_string: Optional[str] = Field(default=None, title="Value String", description="""Value as string""", json_schema_extra = { "linkml_meta": {'annotations': {'fhir_element': {'tag': 'fhir_element',
                                          'value': 'valueString'},
                         'fhir_profile': {'tag': 'fhir_profile',
                                          'value': 'https://nih-ncpi.github.io/ncpi-fhir-ig-2/StructureDefinition/ncpi-participant-assertion'},
                         'fhir_resource': {'tag': 'fhir_resource',
                                           'value': 'Observation'}},
         'domain_of': ['ParticipantAssertion']} })
    value_number: Optional[float] = Field(default=None, title="Value Number", description="""Value as numer""", json_schema_extra = { "linkml_meta": {'annotations': {'fhir_element': {'tag': 'fhir_element',
                                          'value': 'valueQuantity, valueInteger'},
                         'fhir_profile': {'tag': 'fhir_profile',
                                          'value': 'https://nih-ncpi.github.io/ncpi-fhir-ig-2/StructureDefinition/ncpi-participant-assertion'},
                         'fhir_resource': {'tag': 'fhir_resource',
                                           'value': 'Observation'}},
         'domain_of': ['ParticipantAssertion']} })
    value_units: Optional[str] = Field(default=None, title="Value Units", description="""The structured term defining the units of the value (ucum).""", json_schema_extra = { "linkml_meta": {'annotations': {'fhir_profile': {'tag': 'fhir_profile',
                                          'value': 'https://nih-ncpi.github.io/ncpi-fhir-ig-2/StructureDefinition/ncpi-participant-assertion'},
                         'fhir_resource': {'tag': 'fhir_resource',
                                           'value': 'Observation'}},
         'domain_of': ['ParticipantAssertion']} })
    body_site: Optional[str] = Field(default=None, title="Body Site", description="""Location information for the observation, including site, laterality, and other qualifiers as appropriate. Multiple observations may be required if the same assertion is made in many locations, or complete location details can be provided in an NCPI Condition Summary.""", json_schema_extra = { "linkml_meta": {'annotations': {'fhir_element': {'tag': 'fhir_element', 'value': 'bodySite'},
                         'fhir_profile': {'tag': 'fhir_profile',
                                          'value': 'https://nih-ncpi.github.io/ncpi-fhir-ig-2/StructureDefinition/ncpi-participant-assertion'},
                         'fhir_resource': {'tag': 'fhir_resource',
                                           'value': 'Observation'}},
         'domain_of': ['ParticipantAssertion']} })
    body_location: Optional[str] = Field(default=None, title="Body Location", description="""Any location qualifiers""", json_schema_extra = { "linkml_meta": {'annotations': {'fhir_extension': {'tag': 'fhir_extension',
                                            'value': 'http://hl7.org/fhir/us/mcode/StructureDefinition/mcode-body-location-qualifier'},
                         'fhir_profile': {'tag': 'fhir_profile',
                                          'value': 'https://nih-ncpi.github.io/ncpi-fhir-ig-2/StructureDefinition/ncpi-participant-assertion'},
                         'fhir_resource': {'tag': 'fhir_resource',
                                           'value': 'Observation'}},
         'domain_of': ['ParticipantAssertion']} })
    body_laterality: Optional[str] = Field(default=None, title="Laterality Qualifier", description="""Laterality information for the condition site""", json_schema_extra = { "linkml_meta": {'annotations': {'fhir_extension': {'tag': 'fhir_extension',
                                            'value': 'http://hl7.org/fhir/us/mcode/StructureDefinition/mcode-laterality-qualifier'},
                         'fhir_profile': {'tag': 'fhir_profile',
                                          'value': 'https://nih-ncpi.github.io/ncpi-fhir-ig-2/StructureDefinition/ncpi-participant-assertion'},
                         'fhir_resource': {'tag': 'fhir_resource',
                                           'value': 'Observation'}},
         'domain_of': ['ParticipantAssertion']} })
    cancer_stage: Optional[str] = Field(default=None, title="Cancer Stage", description="""Cancer staging information""", json_schema_extra = { "linkml_meta": {'annotations': {'fhir_element': {'tag': 'fhir_element',
                                          'value': 'component[stage]'},
                         'fhir_profile': {'tag': 'fhir_profile',
                                          'value': 'https://nih-ncpi.github.io/ncpi-fhir-ig-2/StructureDefinition/ncpi-participant-assertion'},
                         'fhir_resource': {'tag': 'fhir_resource',
                                           'value': 'Observation'}},
         'domain_of': ['ParticipantAssertion']} })
    participant_assertion_id: str = Field(default=..., title="Participant Assertion ID", description="""Participant Assertion Global ID""", json_schema_extra = { "linkml_meta": {'domain_of': ['ParticipantAssertion']} })


class Person(ConfiguredBaseModel):
    """
    Relate one or more participants to a single person entity
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'from_schema': 'https://carrollaboratory.github.io/kfi-fhir-input/person',
         'title': 'Person'})

    person_id: str = Field(default=..., title="Person ID", description="""Person Global ID (group)""", json_schema_extra = { "linkml_meta": {'domain_of': ['Person']} })
    participant_id: list[str] = Field(default=..., title="Participant ID", description="""The Global ID for the Participant""", json_schema_extra = { "linkml_meta": {'annotations': {'target_slot': {'tag': 'target_slot',
                                         'value': 'participant_id'}},
         'domain_of': ['ParticipantAssertion',
                       'Participant',
                       'Person',
                       'StudyMembership',
                       'Sample',
                       'NCPIFile']} })


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


class StudyMembership(ConfiguredBaseModel):
    """
    Grouping subject participation within a research study is helpful to provide definitive lists of participants that fit a specific criteria such as All Participants or Participants From a Particular Consent Group, etc.
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'from_schema': 'https://carrollaboratory.github.io/kfi-fhir-input/study-membership',
         'title': 'Study Membership'})

    access_policy_id: str = Field(default=..., title="Access Policy ID", description="""Access Policy Global ID""", json_schema_extra = { "linkml_meta": {'annotations': {'target_slot': {'tag': 'target_slot',
                                         'value': 'access_policy_id'}},
         'domain_of': ['AccessPolicy', 'StudyMembership', 'FileLocation']} })
    study_membership_id: str = Field(default=..., title="Study Membership ID", description="""Study Membership Global ID (group)""", json_schema_extra = { "linkml_meta": {'domain_of': ['StudyMembership', 'ResearchStudy']} })
    participant_id: list[str] = Field(default=..., title="Participant ID", description="""The Global ID for the Participant""", json_schema_extra = { "linkml_meta": {'annotations': {'target_slot': {'tag': 'target_slot',
                                         'value': 'participant_id'}},
         'domain_of': ['ParticipantAssertion',
                       'Participant',
                       'Person',
                       'StudyMembership',
                       'Sample',
                       'NCPIFile']} })


class HasExternalId(ConfiguredBaseModel):
    """
    Has an external ID
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'abstract': True,
         'from_schema': 'https://carrollaboratory.github.io/kfi-fhir-input',
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
    description: Optional[str] = Field(default=None, title="Description", description="""More details associated with the given resource""", json_schema_extra = { "linkml_meta": {'domain_of': ['AccessPolicy',
                       'Practitioner',
                       'ResearchStudy',
                       'ResearchStudyCollection',
                       'NCPIFile']} })
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


class Participant(HasExternalId):
    """
    Research oriented patient
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'annotations': {'fhir_resource': {'tag': 'fhir_resource',
                                           'value': 'https://nih-ncpi.github.io/ncpi-fhir-ig-2/StructureDefinition/ncpi-participant'}},
         'from_schema': 'https://carrollaboratory.github.io/kfi-fhir-input/participant',
         'title': 'Participant'})

    birthsex: Optional[EnumBirthSex] = Field(default=None, title="Birth Sex", description="""Sex assigned at birth (or pre-natal observed sex)""", json_schema_extra = { "linkml_meta": {'annotations': {'fhir_extension': {'tag': 'fhir_extension',
                                            'value': 'http://hl7.org/fhir/us/core/StructureDefinition/us-core-birthsex'},
                         'fhir_profile': {'tag': 'fhir_profile',
                                          'value': 'https://nih-ncpi.github.io/ncpi-fhir-ig-2/StructureDefinition/ncpi-participant'},
                         'fhir_resource': {'tag': 'fhir_resource', 'value': 'Consent'}},
         'domain_of': ['Participant']} })
    race: list[EnumRace] = Field(default=..., title="Race", description="""Reported race as defined by the 1997 OMB directives.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Participant']} })
    ethnicity: EnumEthnicity = Field(default=..., title="Ethnicity", description="""Reported ethnicity as defined by the 1997 OMB directives.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Participant']} })
    population: Optional[EnumPopulation] = Field(default=None, title="Population", description="""opulation, Race, and/or Ethnicity information.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Participant']} })
    dob: Optional[str] = Field(default=None, title="Date of Birth", description="""Date of Birth of the participant. Details of privacy method should be included in DOBMethod""", json_schema_extra = { "linkml_meta": {'domain_of': ['Participant']} })
    dob_method: Optional[EnumDobMethod] = Field(default=None, title="Date of Birth Method", description="""Specifies method used to alter DOB for research sharing. Details should be available in the study protocols.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Participant']} })
    age_at_last_vital: Optional[str] = Field(default=None, title="Age At Last Vital Status", description="""Age or date of last vital status""", json_schema_extra = { "linkml_meta": {'domain_of': ['Participant']} })
    is_deceased: Optional[bool] = Field(default=None, title="Is Deceased", description="""Is the participant known to be Deceased, T, or Alive, F""", json_schema_extra = { "linkml_meta": {'domain_of': ['Participant']} })
    deceased_rel: Optional[str] = Field(default=None, title="Deceased Relative Date", description="""Implementers can provide relativeDateTime if information is available.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Participant']} })
    patient_knowledge_source: Optional[EnumPatientKnowledgeSource] = Field(default=None, title="Patient Knowledge Source", description="""The source of the knowledge represented by this Patient resource.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Participant']} })
    participant_id: str = Field(default=..., title="Participant ID", description="""Participant Global ID""", json_schema_extra = { "linkml_meta": {'domain_of': ['ParticipantAssertion',
                       'Participant',
                       'Person',
                       'StudyMembership',
                       'Sample',
                       'NCPIFile']} })
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
    description: Optional[str] = Field(default=None, title="Description", description="""More details associated with the given resource""", json_schema_extra = { "linkml_meta": {'domain_of': ['AccessPolicy',
                       'Practitioner',
                       'ResearchStudy',
                       'ResearchStudyCollection',
                       'NCPIFile']} })
    study_condition: Optional[list[str]] = Field(default=[], title="Study Condition", description="""The primary focus(es) of the study. This is specific to the disease. MeSH terms are preferred.""", json_schema_extra = { "linkml_meta": {'domain_of': ['ResearchStudy']} })
    study_acknowledgement: Optional[list[str]] = Field(default=[], title="Study Acknowledgement", description="""Any attribution or acknowledgements relevant to the study. This can include but is not limited to funding sources, organizational affiliations or sponsors.""", json_schema_extra = { "linkml_meta": {'domain_of': ['ResearchStudy']} })
    study_status: EnumStudyStatus = Field(default=..., title="Study Status", description="""The current state of the study.""", json_schema_extra = { "linkml_meta": {'domain_of': ['ResearchStudy']} })
    study_design: Optional[list[str]] = Field(default=[], title="Study Design", description="""Study Design and Study Type ([example ValueSet can be found here](https://hl7.org/fhir/valueset-study-design.html))""", json_schema_extra = { "linkml_meta": {'domain_of': ['ResearchStudy']} })
    study_personnel: list[str] = Field(default=..., title="Study Personnel", description="""Every study must have at least one Primary Contact defined. Additional personnel such as Primary Investigator(s), Administrator(s), Collaborator(s) or other roles may also be included. If there are no appropriate individuals who can serve as primary contact for a study, an organization may be provided.""", json_schema_extra = { "linkml_meta": {'domain_of': ['ResearchStudy']} })
    study_membership_id: list[str] = Field(default=..., title="Study Membership ID", description="""Study Membership Global ID (group)""", json_schema_extra = { "linkml_meta": {'domain_of': ['StudyMembership', 'ResearchStudy']} })
    research_study_id: str = Field(default=..., title="Research Study ID", description="""The Global ID for the Research Study.""", json_schema_extra = { "linkml_meta": {'domain_of': ['ResearchStudy']} })
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
    description: Optional[str] = Field(default=None, title="Description", description="""The description of the collection.""", json_schema_extra = { "linkml_meta": {'domain_of': ['AccessPolicy',
                       'Practitioner',
                       'ResearchStudy',
                       'ResearchStudyCollection',
                       'NCPIFile']} })
    external_id: Optional[list[str]] = Field(default=[], title="External Identifiers", description="""Other identifiers for this entity, eg, from the submitting study or in systems link dbGaP""", json_schema_extra = { "linkml_meta": {'domain_of': ['HasExternalId']} })


class Sample(HasExternalId):
    """
    Sample encompasses biospecimen collection, sample information, and aliquot information.
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'annotations': {'fhir_profile': {'tag': 'fhir_profile',
                                          'value': 'https://nih-ncpi.github.io/ncpi-fhir-ig-2/StructureDefinition/ncpi-sample'},
                         'fhir_resource': {'tag': 'fhir_resource',
                                           'value': 'Specimen'}},
         'from_schema': 'https://carrollaboratory.github.io/kfi-fhir-input/sample',
         'title': 'Sample'})

    parent_sample_id: Optional[str] = Field(default=None, title="Parent Sample ID", description="""Sample Global ID associated with the parent sample""", json_schema_extra = { "linkml_meta": {'annotations': {'fhir_element': {'tag': 'fhir_element', 'value': 'parent'},
                         'fhir_profile': {'tag': 'fhir_profile',
                                          'value': 'https://nih-ncpi.github.io/ncpi-fhir-ig-2/StructureDefinition/ncpi-sample'},
                         'fhir_resource': {'tag': 'fhir_resource',
                                           'value': 'Specimen'}},
         'domain_of': ['Sample', 'Aliquot']} })
    participant_id: str = Field(default=..., title="Participant ID", description="""The Global ID for the Participant""", json_schema_extra = { "linkml_meta": {'annotations': {'target_slot': {'tag': 'target_slot',
                                         'value': 'participant_id'}},
         'domain_of': ['ParticipantAssertion',
                       'Participant',
                       'Person',
                       'StudyMembership',
                       'Sample',
                       'NCPIFile']} })
    sample_type: str = Field(default=..., title="Sample Type", description="""The type of material of which this Sample is comprised""", json_schema_extra = { "linkml_meta": {'annotations': {'fhir_element': {'tag': 'fhir_element', 'value': 'type'},
                         'fhir_profile': {'tag': 'fhir_profile',
                                          'value': 'https://nih-ncpi.github.io/ncpi-fhir-ig-2/StructureDefinition/ncpi-sample'},
                         'fhir_resource': {'tag': 'fhir_resource',
                                           'value': 'Specimen'}},
         'domain_of': ['Sample']} })
    age_at_collection: Optional[AgeAt] = Field(default=None, title="Age at Collection", description="""The age at which this biospecimen was collected. Could be expressed with a term, an age, or an age range.""", json_schema_extra = { "linkml_meta": {'annotations': {'fhir_element': {'tag': 'fhir_element',
                                          'value': 'collectedDateTime'},
                         'fhir_profile': {'tag': 'fhir_profile',
                                          'value': 'https://nih-ncpi.github.io/ncpi-fhir-ig-2/StructureDefinition/ncpi-sample'},
                         'fhir_resource': {'tag': 'fhir_resource',
                                           'value': 'Specimen'}},
         'domain_of': ['Sample']} })
    collection_method: Optional[str] = Field(default=None, title="Collection Method", description="""The approach used to collect the biospecimen ([LOINC](https://loinc.org))""", json_schema_extra = { "linkml_meta": {'annotations': {'fhir_element': {'tag': 'fhir_element',
                                          'value': 'collection.method'},
                         'fhir_profile': {'tag': 'fhir_profile',
                                          'value': 'https://nih-ncpi.github.io/ncpi-fhir-ig-2/StructureDefinition/ncpi-sample'},
                         'fhir_resource': {'tag': 'fhir_resource',
                                           'value': 'Specimen'}},
         'domain_of': ['Sample']} })
    collection_site: Optional[str] = Field(default=None, title="Collection Site", description="""The location of the specimen collection""", json_schema_extra = { "linkml_meta": {'annotations': {'fhir_element': {'tag': 'fhir_element', 'value': 'bodySite'},
                         'fhir_profile': {'tag': 'fhir_profile',
                                          'value': 'https://nih-ncpi.github.io/ncpi-fhir-ig-2/StructureDefinition/ncpi-sample'},
                         'fhir_resource': {'tag': 'fhir_resource',
                                           'value': 'Specimen'}},
         'domain_of': ['Sample']} })
    spatial_qualifier: Optional[str] = Field(default=None, title="Spatial Qualifier", description="""Any spatial/location qualifiers""", json_schema_extra = { "linkml_meta": {'annotations': {'fhir_element': {'tag': 'fhir_element',
                                          'value': 'collection.extension[biospecimenSpatial]'},
                         'fhir_profile': {'tag': 'fhir_profile',
                                          'value': 'https://nih-ncpi.github.io/ncpi-fhir-ig-2/StructureDefinition/ncpi-sample'},
                         'fhir_resource': {'tag': 'fhir_resource',
                                           'value': 'Specimen'}},
         'domain_of': ['Sample']} })
    laterality: Optional[str] = Field(default=None, title="Laterality", description="""Laterality information for the site""", json_schema_extra = { "linkml_meta": {'annotations': {'fhir_element': {'tag': 'fhir_element',
                                          'value': 'collection.extension[biospecimenLaterality]'},
                         'fhir_profile': {'tag': 'fhir_profile',
                                          'value': 'https://nih-ncpi.github.io/ncpi-fhir-ig-2/StructureDefinition/ncpi-sample'},
                         'fhir_resource': {'tag': 'fhir_resource',
                                           'value': 'Specimen'}},
         'domain_of': ['Sample']} })
    processing: Optional[list[str]] = Field(default=[], title="Processing", description="""Processing that was applied to the Parent Sample or from the Biospecimen Collection that yielded this distinct sample""", json_schema_extra = { "linkml_meta": {'annotations': {'fhir_element': {'tag': 'fhir_element',
                                          'value': 'processing[].procedure'},
                         'fhir_profile': {'tag': 'fhir_profile',
                                          'value': 'https://nih-ncpi.github.io/ncpi-fhir-ig-2/StructureDefinition/ncpi-sample'},
                         'fhir_resource': {'tag': 'fhir_resource',
                                           'value': 'Specimen'}},
         'domain_of': ['Sample']} })
    availability_status: Optional[EnumSpecimenAvailability] = Field(default=None, title="Availability Status", description="""Can this Sample be requested for further analysis?""", json_schema_extra = { "linkml_meta": {'annotations': {'fhir_element': {'tag': 'fhir_element',
                                          'value': 'extension[AliquotAvailability].valueCode'},
                         'fhir_profile': {'tag': 'fhir_profile',
                                          'value': 'https://nih-ncpi.github.io/ncpi-fhir-ig-2/StructureDefinition/ncpi-sample'},
                         'fhir_resource': {'tag': 'fhir_resource',
                                           'value': 'Specimen'}},
         'domain_of': ['Sample', 'Aliquot']} })
    storage_method: Optional[str] = Field(default=None, title="Storage Method", description="""How is the Sample stored, eg, Frozen or with additives (e.g. https://terminology.hl7.org/5.3.0/ValueSet-v2-0493.html)""", json_schema_extra = { "linkml_meta": {'annotations': {'fhir_element': {'tag': 'fhir_element', 'value': 'condition'},
                         'fhir_profile': {'tag': 'fhir_profile',
                                          'value': 'https://nih-ncpi.github.io/ncpi-fhir-ig-2/StructureDefinition/ncpi-sample'},
                         'fhir_resource': {'tag': 'fhir_resource',
                                           'value': 'Specimen'}},
         'domain_of': ['Sample']} })
    quantity: Optional[float] = Field(default=None, title="Quantity", description="""The total quantity of the specimen""", json_schema_extra = { "linkml_meta": {'annotations': {'fhir_element': {'tag': 'fhir_element',
                                          'value': 'collection[].quantity'},
                         'fhir_profile': {'tag': 'fhir_profile',
                                          'value': 'https://nih-ncpi.github.io/ncpi-fhir-ig-2/StructureDefinition/ncpi-sample'},
                         'fhir_resource': {'tag': 'fhir_resource',
                                           'value': 'Specimen'}},
         'domain_of': ['Sample']} })
    quantity_units: Optional[str] = Field(default=None, title="Quantity Units", description="""Units associated with the quantity (ucum)""", json_schema_extra = { "linkml_meta": {'annotations': {'fhir_element': {'tag': 'fhir_element',
                                          'value': 'collection[].quantity.unit'},
                         'fhir_profile': {'tag': 'fhir_profile',
                                          'value': 'https://nih-ncpi.github.io/ncpi-fhir-ig-2/StructureDefinition/ncpi-participant-assertion'},
                         'fhir_resource': {'tag': 'fhir_resource',
                                           'value': 'collection[].quantity.units'}},
         'domain_of': ['Sample']} })
    sample_id: str = Field(default=..., title="Sample ID", description="""Sample Global ID""", json_schema_extra = { "linkml_meta": {'domain_of': ['Sample']} })
    external_id: Optional[list[str]] = Field(default=[], title="External Identifiers", description="""Other identifiers for this entity, eg, from the submitting study or in systems link dbGaP""", json_schema_extra = { "linkml_meta": {'domain_of': ['HasExternalId']} })


class Aliquot(HasExternalId):
    """
    A Portion of a sample extracted from a participant.
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'annotations': {'fhir_element': {'tag': 'fhir_element', 'value': 'container'},
                         'fhir_profile': {'tag': 'fhir_profile',
                                          'value': 'https://nih-ncpi.github.io/ncpi-fhir-ig-2/StructureDefinition/ncpi-sample'},
                         'fhir_resource': {'tag': 'fhir_resource',
                                           'value': 'Specimen'}},
         'from_schema': 'https://carrollaboratory.github.io/kfi-fhir-input/sample',
         'title': 'Aliquot'})

    parent_sample_id: Optional[str] = Field(default=None, title="Parent Sample ID", description="""Sample Global ID associated with the parent sample""", json_schema_extra = { "linkml_meta": {'annotations': {'fhir_element': {'tag': 'fhir_element', 'value': 'parent'},
                         'fhir_profile': {'tag': 'fhir_profile',
                                          'value': 'https://nih-ncpi.github.io/ncpi-fhir-ig-2/StructureDefinition/ncpi-sample'},
                         'fhir_resource': {'tag': 'fhir_resource',
                                           'value': 'Specimen'}},
         'domain_of': ['Sample', 'Aliquot']} })
    availability_status: Optional[EnumSpecimenAvailability] = Field(default=None, title="Availability Status", description="""Can this Sample be requested for further analysis?""", json_schema_extra = { "linkml_meta": {'annotations': {'fhir_element': {'tag': 'fhir_element',
                                          'value': 'extension[AliquotAvailability].valueCode'},
                         'fhir_profile': {'tag': 'fhir_profile',
                                          'value': 'https://nih-ncpi.github.io/ncpi-fhir-ig-2/StructureDefinition/ncpi-sample'},
                         'fhir_resource': {'tag': 'fhir_resource',
                                           'value': 'Specimen'}},
         'domain_of': ['Sample', 'Aliquot']} })
    volume: Optional[float] = Field(default=None, title="Volume", description="""What is the volume of the Aliquot?""", json_schema_extra = { "linkml_meta": {'annotations': {'fhir_element': {'tag': 'fhir_element',
                                          'value': 'collection[].quantity.value'},
                         'fhir_profile': {'tag': 'fhir_profile',
                                          'value': 'https://nih-ncpi.github.io/ncpi-fhir-ig-2/StructureDefinition/ncpi-participant-assertion'},
                         'fhir_resource': {'tag': 'fhir_resource',
                                           'value': 'Specimen'}},
         'domain_of': ['Aliquot']} })
    volume_units: Optional[str] = Field(default=None, title="Volume Units", description="""Units associated with the volume (ucum)""", json_schema_extra = { "linkml_meta": {'annotations': {'fhir_element': {'tag': 'fhir_element',
                                          'value': 'collection[].quantity.unit'},
                         'fhir_profile': {'tag': 'fhir_profile',
                                          'value': 'https://nih-ncpi.github.io/ncpi-fhir-ig-2/StructureDefinition/ncpi-participant-assertion'},
                         'fhir_resource': {'tag': 'fhir_resource',
                                           'value': 'Specimen'}},
         'domain_of': ['Aliquot']} })
    concentration: Optional[str] = Field(default=None, title="Concentration", description="""What is the concentration of the analyte in the Aliquot?""", json_schema_extra = { "linkml_meta": {'annotations': {'fhir_element': {'tag': 'fhir_element',
                                          'value': 'collection[].extension[AliquotConcentration].valueQuantity.value'},
                         'fhir_profile': {'tag': 'fhir_profile',
                                          'value': 'https://nih-ncpi.github.io/ncpi-fhir-ig-2/StructureDefinition/ncpi-participant-assertion'},
                         'fhir_resource': {'tag': 'fhir_resource',
                                           'value': 'Specimen'}},
         'domain_of': ['Aliquot']} })
    aliquot_id: str = Field(default=..., title="aliquot ID", description="""Aliquot Global ID""", json_schema_extra = { "linkml_meta": {'domain_of': ['Aliquot']} })
    external_id: Optional[list[str]] = Field(default=[], title="External Identifiers", description="""Other identifiers for this entity, eg, from the submitting study or in systems link dbGaP""", json_schema_extra = { "linkml_meta": {'domain_of': ['HasExternalId']} })


class NCPIFile(HasExternalId):
    """
    Information about a file related to a research participant
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'annotations': {'fhir_profile': {'tag': 'fhir_profile',
                                          'value': 'https://nih-ncpi.github.io/ncpi-fhir-ig-2/StructureDefinition/ncpi-drs-file'},
                         'fhir_resource': {'tag': 'fhir_resource',
                                           'value': 'DocumentReference'}},
         'from_schema': 'https://carrollaboratory.github.io/kfi-fhir-input/ncpi-file',
         'title': 'NCPI File'})

    participant_id: str = Field(default=..., title="Participant ID", description="""The Global ID for the Participant""", json_schema_extra = { "linkml_meta": {'annotations': {'target_slot': {'tag': 'target_slot',
                                         'value': 'participant_id'}},
         'domain_of': ['ParticipantAssertion',
                       'Participant',
                       'Person',
                       'StudyMembership',
                       'Sample',
                       'NCPIFile']} })
    file_format: str = Field(default=..., title="File Format", description="""The file format used ([EDAM](http://edamontology.org) where possible)""", json_schema_extra = { "linkml_meta": {'domain_of': ['NCPIFile']} })
    file_location: list[str] = Field(default=..., title="File Location", description="""Details relating to the links where documents are found""", json_schema_extra = { "linkml_meta": {'domain_of': ['NCPIFile']} })
    file_meta_data: Optional[list[str]] = Field(default=[], title="File Meta Data", description="""Representation of file metadata for NCPI""", json_schema_extra = { "linkml_meta": {'domain_of': ['NCPIFile']} })
    file_size: float = Field(default=..., title="File Size", description="""The size of the file, e.g., in bytes.""", json_schema_extra = { "linkml_meta": {'domain_of': ['NCPIFile']} })
    file_size_unit: str = Field(default=..., title="File Size Units", description="""Units associated with the file_size value (ucum)""", json_schema_extra = { "linkml_meta": {'domain_of': ['NCPIFile']} })
    content_version: Optional[str] = Field(default=None, title="Content Version", description="""Version of the file content""", json_schema_extra = { "linkml_meta": {'domain_of': ['NCPIFile']} })
    file_type: str = Field(default=..., title="File Type", description="""The type of data contained in this file. Should be as detailed as possible, e.g., Whole Exome Variant Calls.""", json_schema_extra = { "linkml_meta": {'domain_of': ['NCPIFile']} })
    file_hash: str = Field(default=..., title="File Hash", description="""Value of hashing the file""", json_schema_extra = { "linkml_meta": {'domain_of': ['NCPIFile']} })
    file_hash_type: Optional[str] = Field(default=None, title="File Has Type", description="""Algorithm used to calculate the hash (and size, where applicable)""", json_schema_extra = { "linkml_meta": {'domain_of': ['NCPIFile']} })
    description: Optional[str] = Field(default=None, title="Description", description="""More details associated with the given resource""", json_schema_extra = { "linkml_meta": {'domain_of': ['AccessPolicy',
                       'Practitioner',
                       'ResearchStudy',
                       'ResearchStudyCollection',
                       'NCPIFile']} })
    file_global_id: str = Field(default=..., title="File Global ID", description="""File Global ID""", json_schema_extra = { "linkml_meta": {'domain_of': ['NCPIFile']} })
    external_id: Optional[list[str]] = Field(default=[], title="External Identifiers", description="""Other identifiers for this entity, eg, from the submitting study or in systems link dbGaP""", json_schema_extra = { "linkml_meta": {'domain_of': ['HasExternalId']} })


class Record(HasExternalId):
    """
    One row / entity within the database
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'abstract': True,
         'from_schema': 'https://carrollaboratory.github.io/kfi-fhir-input',
         'title': 'Record'})

    id: str = Field(default=..., title="ID", description="""Unique Identifier for a table entry. This is probably not the Global ID""", json_schema_extra = { "linkml_meta": {'domain_of': ['RelativeDateTime', 'Record']} })
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
    id: str = Field(default=..., title="ID", description="""Unique Identifier for a table entry. This is probably not the Global ID""", json_schema_extra = { "linkml_meta": {'domain_of': ['RelativeDateTime', 'Record']} })
    external_id: Optional[list[str]] = Field(default=[], title="External Identifiers", description="""Other identifiers for this entity, eg, from the submitting study or in systems link dbGaP""", json_schema_extra = { "linkml_meta": {'domain_of': ['HasExternalId']} })


class Period(Record):
    """
    Time period associated with some FHIR resource
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'from_schema': 'https://carrollaboratory.github.io/kfi-fhir-input/period',
         'title': 'Period'})

    start: Optional[date] = Field(default=None, title="Start", description="""Start attribute for a FHIR period data type.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Period']} })
    end: Optional[date] = Field(default=None, title="End", description="""End attribute for a FHIR period data type.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Period']} })
    id: str = Field(default=..., title="ID", description="""Unique Identifier for a table entry. This is probably not the Global ID""", json_schema_extra = { "linkml_meta": {'domain_of': ['RelativeDateTime', 'Record']} })
    external_id: Optional[list[str]] = Field(default=[], title="External Identifiers", description="""Other identifiers for this entity, eg, from the submitting study or in systems link dbGaP""", json_schema_extra = { "linkml_meta": {'domain_of': ['HasExternalId']} })


class FileLocation(Record):
    """
    Details relating to the links where documents are found
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'annotations': {'fhir_element': {'tag': 'fhir_element', 'value': 'content'},
                         'fhir_profile': {'tag': 'fhir_profile',
                                          'value': 'https://nih-ncpi.github.io/ncpi-fhir-ig-2/StructureDefinition/ncpi-drs-file'},
                         'fhir_resource': {'tag': 'fhir_resource',
                                           'value': 'DocumentReference'}},
         'from_schema': 'https://carrollaboratory.github.io/kfi-fhir-input/file-location',
         'title': 'File Location'})

    location_uri: str = Field(default=..., title="Location URI", description="""The URI at which this data can be accessed""", json_schema_extra = { "linkml_meta": {'domain_of': ['FileLocation']} })
    file_name: str = Field(default=..., title="File Name", description="""The file's name (no path)""", json_schema_extra = { "linkml_meta": {'domain_of': ['FileLocation']} })
    access_policy_id: str = Field(default=..., title="Access Policy ID", description="""Access Policy Global ID""", json_schema_extra = { "linkml_meta": {'annotations': {'target_slot': {'tag': 'target_slot',
                                         'value': 'access_policy_id'}},
         'domain_of': ['AccessPolicy', 'StudyMembership', 'FileLocation']} })
    id: str = Field(default=..., title="ID", description="""Unique Identifier for a table entry. This is probably not the Global ID""", json_schema_extra = { "linkml_meta": {'domain_of': ['RelativeDateTime', 'Record']} })
    external_id: Optional[list[str]] = Field(default=[], title="External Identifiers", description="""Other identifiers for this entity, eg, from the submitting study or in systems link dbGaP""", json_schema_extra = { "linkml_meta": {'domain_of': ['HasExternalId']} })


class FileMetaData(Record):
    """
    Representation of file metadata for NCPI
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'annotations': {'fhir_profile': {'tag': 'fhir_profile',
                                          'value': 'https://nih-ncpi.github.io/ncpi-fhir-ig-2/StructureDefinition/ncpi-file-metadata'},
                         'fhir_resource': {'tag': 'fhir_resource',
                                           'value': 'Observation'}},
         'from_schema': 'https://carrollaboratory.github.io/kfi-fhir-input/file-meta-data',
         'title': 'File Meta Data'})

    meta_data_type: EnumFileMetaDataType = Field(default=..., title="Meta Data Type", description="""Clarify which type of meta data this file has recorded""", json_schema_extra = { "linkml_meta": {'domain_of': ['FileMetaData']} })
    assay_strategy: str = Field(default=..., title="Assay Strategy", description="""e.g., Whole Genome Sequencing""", json_schema_extra = { "linkml_meta": {'domain_of': ['FileMetaData']} })
    platform_instrument: str = Field(default=..., title="Platform Instrument", description="""e.g., Illumina HiSeq2000""", json_schema_extra = { "linkml_meta": {'domain_of': ['FileMetaData']} })
    library_prep: Optional[str] = Field(default=None, title="Library Prep", description="""e.g., polyA""", json_schema_extra = { "linkml_meta": {'domain_of': ['FileMetaData']} })
    library_selection: Optional[str] = Field(default=None, title="Library Selection", description="""...""", json_schema_extra = { "linkml_meta": {'domain_of': ['FileMetaData']} })
    strandedness: Optional[str] = Field(default=None, title="Strandedness", description="""stranded, unstranded""", json_schema_extra = { "linkml_meta": {'domain_of': ['FileMetaData']} })
    target_region: Optional[str] = Field(default=None, title="Target Region", description="""Target region""", json_schema_extra = { "linkml_meta": {'domain_of': ['FileMetaData']} })
    is_paired_end: Optional[str] = Field(default=None, title="Is Paired End", description="""True, False""", json_schema_extra = { "linkml_meta": {'domain_of': ['FileMetaData']} })
    adaptor_trimmed: Optional[str] = Field(default=None, title="Adaptor Trimmed", description="""True, False""", json_schema_extra = { "linkml_meta": {'domain_of': ['FileMetaData']} })
    reference_genome: Optional[str] = Field(default=None, title="Reference Genome", description="""GRCh37, GRCh38""", json_schema_extra = { "linkml_meta": {'domain_of': ['FileMetaData']} })
    workflow_type: Optional[str] = Field(default=None, title="Workflow Type", description="""e.g., alignment, somatic""", json_schema_extra = { "linkml_meta": {'domain_of': ['FileMetaData']} })
    workflow_tool: Optional[str] = Field(default=None, title="Workflow Tool", description="""e.g., BAM-MEM, GATK-Haplotype Caller""", json_schema_extra = { "linkml_meta": {'domain_of': ['FileMetaData']} })
    related_samples: Optional[str] = Field(default=None, title="Related Samples", description="""e.g., Reference(Participant_ID)""", json_schema_extra = { "linkml_meta": {'domain_of': ['FileMetaData']} })
    id: str = Field(default=..., title="ID", description="""Unique Identifier for a table entry. This is probably not the Global ID""", json_schema_extra = { "linkml_meta": {'domain_of': ['RelativeDateTime', 'Record']} })
    external_id: Optional[list[str]] = Field(default=[], title="External Identifiers", description="""Other identifiers for this entity, eg, from the submitting study or in systems link dbGaP""", json_schema_extra = { "linkml_meta": {'domain_of': ['HasExternalId']} })


# Model rebuild
# see https://pydantic-docs.helpmanual.io/usage/models/#rebuilding-a-model
AccessPolicy.model_rebuild()
RelativeDateTime.model_rebuild()
AgeAt.model_rebuild()
ParticipantAssertion.model_rebuild()
Person.model_rebuild()
PractitionerRole.model_rebuild()
StudyMembership.model_rebuild()
HasExternalId.model_rebuild()
Practitioner.model_rebuild()
Institution.model_rebuild()
Participant.model_rebuild()
ResearchStudy.model_rebuild()
ResearchStudyCollection.model_rebuild()
Sample.model_rebuild()
Aliquot.model_rebuild()
NCPIFile.model_rebuild()
Record.model_rebuild()
AssociatedParty.model_rebuild()
Period.model_rebuild()
FileLocation.model_rebuild()
FileMetaData.model_rebuild()
