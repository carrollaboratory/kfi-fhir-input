# Auto generated from kfi_fhir_input.yaml by pythongen.py version: 0.0.1
# Generation date: 2026-01-14T11:36:29
# Schema: kfi-fhir-input
#
# id: https://carrollaboratory.github.io/kfi-fhir-input
# description: DBT Output Schema for FHIR Ingest
# license: MIT

import dataclasses
import re
from dataclasses import dataclass
from datetime import (
    date,
    datetime,
    time
)
from typing import (
    Any,
    ClassVar,
    Dict,
    List,
    Optional,
    Union
)

from jsonasobj2 import (
    JsonObj,
    as_dict
)
from linkml_runtime.linkml_model.meta import (
    EnumDefinition,
    PermissibleValue,
    PvFormulaOptions
)
from linkml_runtime.utils.curienamespace import CurieNamespace
from linkml_runtime.utils.enumerations import EnumDefinitionImpl
from linkml_runtime.utils.formatutils import (
    camelcase,
    sfx,
    underscore
)
from linkml_runtime.utils.metamodelcore import (
    bnode,
    empty_dict,
    empty_list
)
from linkml_runtime.utils.slot import Slot
from linkml_runtime.utils.yamlutils import (
    YAMLRoot,
    extended_float,
    extended_int,
    extended_str
)
from rdflib import (
    Namespace,
    URIRef
)

from linkml_runtime.linkml_model.types import Boolean, Date, Float, Integer, String, Uri, Uriorcurie
from linkml_runtime.utils.metamodelcore import Bool, URI, URIorCURIE, XSDDate

metamodel_version = "1.7.0"
version = None

# Namespaces
CDC_REC = CurieNamespace('cdc_rec', 'https://phinvads.cdc.gov/baseStu3/CodeSystem/PH_RaceAndEthnicity_CDC')
CDC_UNK = CurieNamespace('cdc_unk', 'https://vsac.nlm.nih.gov/valueset/2.16.840.1.113762.1.4.1021.103/expansion')
DUO = CurieNamespace('duo', 'http://purl.obolibrary.org/obo/duo.owl')
EDAM = CurieNamespace('edam', 'https://edamontology.org')
FLUFF = CurieNamespace('fluff', 'https://fluffy.cat.onto/terms')
HL7_CONSENT_SCOPE = CurieNamespace('hl7_consent_scope', 'http://terminology.hl7.org/CodeSystem/consentscope')
HL7_CONSENT_STATE_CODES = CurieNamespace('hl7_consent_state_codes', 'http://hl7.org/fhir/consent-state-codes')
HL7_LIST_STATUS = CurieNamespace('hl7_list_status', 'https://hl7.org/fhir/R4/codesystem-list-status')
HL7_NULL = CurieNamespace('hl7_null', 'http://terminology.hl7.org/CodeSystem/v3-NullFlavor')
HL7_RSP_ORG_TYPE = CurieNamespace('hl7_rsp_org_type', 'http://hl7.org/fhir/research-study-party-organization-type')
HL7_RSP_ROLE = CurieNamespace('hl7_rsp_role', 'http://hl7.org/fhir/research-study-party-role')
HL7_STUDY_DESIGN = CurieNamespace('hl7_study_design', 'https://hl7.org/fhir/codesystem-study-design')
HL7_STUDY_STATUS = CurieNamespace('hl7_study_status', 'https://hl7.org/fhir/R4/codesystem-research-study-status')
KFI = CurieNamespace('kfi', 'https://carrollaboratory.github.io/kfi-fhir-input/')
KFI_FHIR_SPARKS = CurieNamespace('kfi_fhir_sparks', 'https://carrollaboratory.github.io/kif-fhir-input')
KIN = CurieNamespace('kin', 'http://purl.org/ga4gh/kin.fhir')
LINKML = CurieNamespace('linkml', 'https://w3id.org/linkml/')
NCPI_COLLECTION_TYPE = CurieNamespace('ncpi_collection_type', 'https://nih-ncpi.github.io/ncpi-fhir-ig-2/CodeSystem/collection-type')
NCPI_COND_TYPE = CurieNamespace('ncpi_cond_type', 'https://nih-ncpi.github.io/ncpi-fhir-ig-2/CodeSystem/condition-type/')
NCPI_DATA_ACCESS_CODE = CurieNamespace('ncpi_data_access_code', 'https://nih-ncpi.github.io/ncpi-fhir-ig-2/CodeSystem/research-data-access-code/')
NCPI_DATA_ACCESS_TYPE = CurieNamespace('ncpi_data_access_type', 'https://nih-ncpi.github.io/ncpi-fhir-ig-2/CodeSystem-research-data-access-type')
NCPI_DOB_METHOD = CurieNamespace('ncpi_dob_method', 'https://nih-ncpi.github.io/ncpi-fhir-ig-2/CodeSystem/research-data-date-of-birth-method')
NCPI_FAMILY_TYPES = CurieNamespace('ncpi_family_types', 'https://nih-ncpi.github.io/ncpi-fhir-ig-2/CodeSystem/ncpi-family-types')
NCPI_PATIENT_KNOWLEDGE_SOURCE = CurieNamespace('ncpi_patient_knowledge_source', 'https://nih-ncpi.github.io/ncpi-fhir-ig-2/CodeSystem/patient-knowledge-source')
NCPI_SAMPLE_AVAILABILITY = CurieNamespace('ncpi_sample_availability', 'https://nih-ncpi.github.io/ncpi-fhir-ig-2/CodeSystem/biospecimen-availability')
OBI = CurieNamespace('obi', 'http://purl.obolibrary.org/obo/obi.owl')
SCT = CurieNamespace('sct', 'http://snomed.info/sct')
UCUM = CurieNamespace('ucum', 'http://unitsofmeasure.org')
UMLS = CurieNamespace('umls', 'https://uts.nlm.nih.gov/uts/umls/concept')
UNKNOWN = CurieNamespace('unknown', 'https://need-more-info.org')
USC_BIRTHSEX = CurieNamespace('usc_birthsex', 'http://terminology.hl7.org/CodeSystem/v3-AdministrativeGender')
W3C = CurieNamespace('w3c', 'https://w3c.github.io/N3/ns/')
DEFAULT_ = KFI_FHIR_SPARKS


# Types

# Class references
class RecordId(extended_str):
    pass


class AccessPolicyAccessPolicyId(extended_str):
    pass


class RelativeDateTimeId(extended_str):
    pass


class AgeAtId(RecordId):
    pass


class ParticipantAssertionParticipantAssertionId(extended_str):
    pass


class PractitionerPractitionerId(extended_str):
    pass


class AssociatedPartyId(RecordId):
    pass


class InstitutionInstitutionId(extended_str):
    pass


class ParticipantParticipantId(extended_str):
    pass


class PersonPersonId(extended_str):
    pass


class PeriodPeriodId(extended_str):
    pass


class PractitionerRolePractitionerRoleId(extended_str):
    pass


class StudyMembershipStudyMembershipId(extended_str):
    pass


class ResearchStudyResearchStudyId(extended_str):
    pass


class ResearchStudyCollectionResearchStudyCollectionId(extended_str):
    pass


class SampleSampleId(extended_str):
    pass


class AliquotAliquotId(extended_str):
    pass


class NCPIFileFileGlobalId(extended_str):
    pass


class FileLocationFileLocationId(extended_str):
    pass


class FamilyRelationshipFamilyRelationshipGlobalId(extended_str):
    pass


class FamilyFamilyGlobalId(extended_str):
    pass


class FileMetaDataFileMetaDataId(extended_str):
    pass


Any = Any

@dataclass(repr=False)
class HasExternalId(YAMLRoot):
    """
    Has an external ID
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = KFI_FHIR_SPARKS["HasExternalId"]
    class_class_curie: ClassVar[str] = "kfi_fhir_sparks:HasExternalId"
    class_name: ClassVar[str] = "HasExternalId"
    class_model_uri: ClassVar[URIRef] = KFI_FHIR_SPARKS.HasExternalId

    external_id: Optional[Union[Union[str, URIorCURIE], list[Union[str, URIorCURIE]]]] = empty_list()

    def __post_init__(self, *_: str, **kwargs: Any):
        if not isinstance(self.external_id, list):
            self.external_id = [self.external_id] if self.external_id is not None else []
        self.external_id = [v if isinstance(v, URIorCURIE) else URIorCURIE(v) for v in self.external_id]

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class Record(HasExternalId):
    """
    One row / entity within the database
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = KFI_FHIR_SPARKS["Record"]
    class_class_curie: ClassVar[str] = "kfi_fhir_sparks:Record"
    class_name: ClassVar[str] = "Record"
    class_model_uri: ClassVar[URIRef] = KFI_FHIR_SPARKS.Record

    id: Union[str, RecordId] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, RecordId):
            self.id = RecordId(self.id)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class AccessPolicy(YAMLRoot):
    """
    Limitations and/or requirements that define how a user may gain access to a particular set of data.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = KFI["access-policy/AccessPolicy"]
    class_class_curie: ClassVar[str] = "kfi:access-policy/AccessPolicy"
    class_name: ClassVar[str] = "AccessPolicy"
    class_model_uri: ClassVar[URIRef] = KFI_FHIR_SPARKS.AccessPolicy

    access_policy_id: Union[str, AccessPolicyAccessPolicyId] = None
    data_access_type: Union[str, "EnumDataAccessType"] = None
    consent_scope: Union[str, "EnumConsentScope"] = None
    access_policy_code: Union[Union[str, "EnumAccessPolicyCode"], list[Union[str, "EnumAccessPolicyCode"]]] = None
    status: Union[str, "EnumConsentStateCodes"] = None
    description: Optional[str] = None
    website: Optional[Union[str, URI]] = None
    disease_limitation: Optional[str] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.access_policy_id):
            self.MissingRequiredField("access_policy_id")
        if not isinstance(self.access_policy_id, AccessPolicyAccessPolicyId):
            self.access_policy_id = AccessPolicyAccessPolicyId(self.access_policy_id)

        if self._is_empty(self.data_access_type):
            self.MissingRequiredField("data_access_type")
        if not isinstance(self.data_access_type, EnumDataAccessType):
            self.data_access_type = EnumDataAccessType(self.data_access_type)

        if self._is_empty(self.consent_scope):
            self.MissingRequiredField("consent_scope")
        if not isinstance(self.consent_scope, EnumConsentScope):
            self.consent_scope = EnumConsentScope(self.consent_scope)

        if self._is_empty(self.access_policy_code):
            self.MissingRequiredField("access_policy_code")
        if not isinstance(self.access_policy_code, list):
            self.access_policy_code = [self.access_policy_code] if self.access_policy_code is not None else []
        self.access_policy_code = [v if isinstance(v, EnumAccessPolicyCode) else EnumAccessPolicyCode(v) for v in self.access_policy_code]

        if self._is_empty(self.status):
            self.MissingRequiredField("status")
        if not isinstance(self.status, EnumConsentStateCodes):
            self.status = EnumConsentStateCodes(self.status)

        if self.description is not None and not isinstance(self.description, str):
            self.description = str(self.description)

        if self.website is not None and not isinstance(self.website, URI):
            self.website = URI(self.website)

        if self.disease_limitation is not None and not isinstance(self.disease_limitation, str):
            self.disease_limitation = str(self.disease_limitation)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class RelativeDateTime(YAMLRoot):
    """
    In FHIR, we can express events using relative date/times from the participant's DOB to avoid exposing sensitive
    information
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = KFI["relative-date-time/RelativeDateTime"]
    class_class_curie: ClassVar[str] = "kfi:relative-date-time/RelativeDateTime"
    class_name: ClassVar[str] = "RelativeDateTime"
    class_model_uri: ClassVar[URIRef] = KFI_FHIR_SPARKS.RelativeDateTime

    id: Union[str, RelativeDateTimeId] = None
    offset: int = None
    offset_type: Union[str, "EnumOffsetType"] = None
    offset_end: Optional[int] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, RelativeDateTimeId):
            self.id = RelativeDateTimeId(self.id)

        if self._is_empty(self.offset):
            self.MissingRequiredField("offset")
        if not isinstance(self.offset, int):
            self.offset = int(self.offset)

        if self._is_empty(self.offset_type):
            self.MissingRequiredField("offset_type")
        if not isinstance(self.offset_type, EnumOffsetType):
            self.offset_type = EnumOffsetType(self.offset_type)

        if self.offset_end is not None and not isinstance(self.offset_end, int):
            self.offset_end = int(self.offset_end)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class AgeAt(Record):
    """
    These represent a flexible age value that could represent one of the following-Relative Age Offset, Age Range as
    Code, Date Range, DateTime
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = KFI["age-at/AgeAt"]
    class_class_curie: ClassVar[str] = "kfi:age-at/AgeAt"
    class_name: ClassVar[str] = "AgeAt"
    class_model_uri: ClassVar[URIRef] = KFI_FHIR_SPARKS.AgeAt

    id: Union[str, AgeAtId] = None
    value_type: Union[str, "EnumAgeValueType"] = None
    age: Optional[Union[str, RelativeDateTimeId]] = None
    age_code: Optional[Union[str, URIorCURIE]] = None
    as_date: Optional[Union[str, XSDDate]] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, AgeAtId):
            self.id = AgeAtId(self.id)

        if self._is_empty(self.value_type):
            self.MissingRequiredField("value_type")
        if not isinstance(self.value_type, EnumAgeValueType):
            self.value_type = EnumAgeValueType(self.value_type)

        if self.age is not None and not isinstance(self.age, RelativeDateTimeId):
            self.age = RelativeDateTimeId(self.age)

        if self.age_code is not None and not isinstance(self.age_code, URIorCURIE):
            self.age_code = URIorCURIE(self.age_code)

        if self.as_date is not None and not isinstance(self.as_date, XSDDate):
            self.as_date = XSDDate(self.as_date)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class ParticipantAssertion(YAMLRoot):
    """
    Assertion about a particular Participant. May include Conditions, Measurements, etc.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = KFI["participant-assertion/ParticipantAssertion"]
    class_class_curie: ClassVar[str] = "kfi:participant-assertion/ParticipantAssertion"
    class_name: ClassVar[str] = "ParticipantAssertion"
    class_model_uri: ClassVar[URIRef] = KFI_FHIR_SPARKS.ParticipantAssertion

    participant_assertion_id: Union[str, ParticipantAssertionParticipantAssertionId] = None
    participant_id: Union[str, ParticipantParticipantId] = None
    assertion_type: Union[str, "EnumAssertionType"] = None
    assertion_code: Union[str, URIorCURIE] = None
    age_at_event: Optional[Union[str, AgeAtId]] = None
    age_at_assertion: Optional[Union[str, AgeAtId]] = None
    age_at_onset: Optional[Union[str, AgeAtId]] = None
    age_at_resolution: Optional[Union[str, AgeAtId]] = None
    entity_asserter: Optional[Union[str, "EnumEntityAsserter"]] = None
    other_condition_modifiers: Optional[Union[str, URIorCURIE]] = None
    assertion_text: Optional[str] = None
    assertion_source: Optional[Union[str, URIorCURIE]] = None
    value_code: Optional[Union[str, URIorCURIE]] = None
    value_string: Optional[str] = None
    value_number: Optional[float] = None
    value_units: Optional[Union[str, URIorCURIE]] = None
    body_site: Optional[Union[str, URIorCURIE]] = None
    body_location: Optional[Union[str, URIorCURIE]] = None
    body_laterality: Optional[Union[str, URIorCURIE]] = None
    cancer_stage: Optional[Union[str, URIorCURIE]] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.participant_assertion_id):
            self.MissingRequiredField("participant_assertion_id")
        if not isinstance(self.participant_assertion_id, ParticipantAssertionParticipantAssertionId):
            self.participant_assertion_id = ParticipantAssertionParticipantAssertionId(self.participant_assertion_id)

        if self._is_empty(self.participant_id):
            self.MissingRequiredField("participant_id")
        if not isinstance(self.participant_id, ParticipantParticipantId):
            self.participant_id = ParticipantParticipantId(self.participant_id)

        if self._is_empty(self.assertion_type):
            self.MissingRequiredField("assertion_type")
        if not isinstance(self.assertion_type, EnumAssertionType):
            self.assertion_type = EnumAssertionType(self.assertion_type)

        if self._is_empty(self.assertion_code):
            self.MissingRequiredField("assertion_code")
        if not isinstance(self.assertion_code, URIorCURIE):
            self.assertion_code = URIorCURIE(self.assertion_code)

        if self.age_at_event is not None and not isinstance(self.age_at_event, AgeAtId):
            self.age_at_event = AgeAtId(self.age_at_event)

        if self.age_at_assertion is not None and not isinstance(self.age_at_assertion, AgeAtId):
            self.age_at_assertion = AgeAtId(self.age_at_assertion)

        if self.age_at_onset is not None and not isinstance(self.age_at_onset, AgeAtId):
            self.age_at_onset = AgeAtId(self.age_at_onset)

        if self.age_at_resolution is not None and not isinstance(self.age_at_resolution, AgeAtId):
            self.age_at_resolution = AgeAtId(self.age_at_resolution)

        if self.entity_asserter is not None and not isinstance(self.entity_asserter, EnumEntityAsserter):
            self.entity_asserter = EnumEntityAsserter(self.entity_asserter)

        if self.other_condition_modifiers is not None and not isinstance(self.other_condition_modifiers, URIorCURIE):
            self.other_condition_modifiers = URIorCURIE(self.other_condition_modifiers)

        if self.assertion_text is not None and not isinstance(self.assertion_text, str):
            self.assertion_text = str(self.assertion_text)

        if self.assertion_source is not None and not isinstance(self.assertion_source, URIorCURIE):
            self.assertion_source = URIorCURIE(self.assertion_source)

        if self.value_code is not None and not isinstance(self.value_code, URIorCURIE):
            self.value_code = URIorCURIE(self.value_code)

        if self.value_string is not None and not isinstance(self.value_string, str):
            self.value_string = str(self.value_string)

        if self.value_number is not None and not isinstance(self.value_number, float):
            self.value_number = float(self.value_number)

        if self.value_units is not None and not isinstance(self.value_units, URIorCURIE):
            self.value_units = URIorCURIE(self.value_units)

        if self.body_site is not None and not isinstance(self.body_site, URIorCURIE):
            self.body_site = URIorCURIE(self.body_site)

        if self.body_location is not None and not isinstance(self.body_location, URIorCURIE):
            self.body_location = URIorCURIE(self.body_location)

        if self.body_laterality is not None and not isinstance(self.body_laterality, URIorCURIE):
            self.body_laterality = URIorCURIE(self.body_laterality)

        if self.cancer_stage is not None and not isinstance(self.cancer_stage, URIorCURIE):
            self.cancer_stage = URIorCURIE(self.cancer_stage)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class Practitioner(HasExternalId):
    """
    For our purposes, this will be an investigator.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = KFI["practitioner/Practitioner"]
    class_class_curie: ClassVar[str] = "kfi:practitioner/Practitioner"
    class_name: ClassVar[str] = "Practitioner"
    class_model_uri: ClassVar[URIRef] = KFI_FHIR_SPARKS.Practitioner

    practitioner_id: Union[str, PractitionerPractitionerId] = None
    name: Optional[str] = None
    email: Optional[str] = None
    institution_id: Optional[Union[str, InstitutionInstitutionId]] = None
    practitioner_role_id: Optional[Union[str, PractitionerRolePractitionerRoleId]] = None
    description: Optional[str] = None
    practitioner_title: Optional[str] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.practitioner_id):
            self.MissingRequiredField("practitioner_id")
        if not isinstance(self.practitioner_id, PractitionerPractitionerId):
            self.practitioner_id = PractitionerPractitionerId(self.practitioner_id)

        if self.name is not None and not isinstance(self.name, str):
            self.name = str(self.name)

        if self.email is not None and not isinstance(self.email, str):
            self.email = str(self.email)

        if self.institution_id is not None and not isinstance(self.institution_id, InstitutionInstitutionId):
            self.institution_id = InstitutionInstitutionId(self.institution_id)

        if self.practitioner_role_id is not None and not isinstance(self.practitioner_role_id, PractitionerRolePractitionerRoleId):
            self.practitioner_role_id = PractitionerRolePractitionerRoleId(self.practitioner_role_id)

        if self.description is not None and not isinstance(self.description, str):
            self.description = str(self.description)

        if self.practitioner_title is not None and not isinstance(self.practitioner_title, str):
            self.practitioner_title = str(self.practitioner_title)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class AssociatedParty(Record):
    """
    Sponsors, collaborators, and other parties affiliated with a research study.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = KFI["associated_party/AssociatedParty"]
    class_class_curie: ClassVar[str] = "kfi:associated_party/AssociatedParty"
    class_name: ClassVar[str] = "AssociatedParty"
    class_model_uri: ClassVar[URIRef] = KFI_FHIR_SPARKS.AssociatedParty

    id: Union[str, AssociatedPartyId] = None
    name: Optional[str] = None
    role: Optional[Union[str, "EnumResearchStudyPartyRole"]] = None
    period_id: Optional[Union[Union[str, PeriodPeriodId], list[Union[str, PeriodPeriodId]]]] = empty_list()
    classifier: Optional[Union[Union[str, "EnumResearchStudyPartyOrganizationType"], list[Union[str, "EnumResearchStudyPartyOrganizationType"]]]] = empty_list()
    associated_party_practitioner_id: Optional[Union[str, PractitionerPractitionerId]] = None
    associated_party_practitioner_role_id: Optional[Union[str, PractitionerRolePractitionerRoleId]] = None
    associated_party_institution_id: Optional[Union[str, PractitionerRolePractitionerRoleId]] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, AssociatedPartyId):
            self.id = AssociatedPartyId(self.id)

        if self.name is not None and not isinstance(self.name, str):
            self.name = str(self.name)

        if self.role is not None and not isinstance(self.role, EnumResearchStudyPartyRole):
            self.role = EnumResearchStudyPartyRole(self.role)

        if not isinstance(self.period_id, list):
            self.period_id = [self.period_id] if self.period_id is not None else []
        self.period_id = [v if isinstance(v, PeriodPeriodId) else PeriodPeriodId(v) for v in self.period_id]

        if not isinstance(self.classifier, list):
            self.classifier = [self.classifier] if self.classifier is not None else []
        self.classifier = [v if isinstance(v, EnumResearchStudyPartyOrganizationType) else EnumResearchStudyPartyOrganizationType(v) for v in self.classifier]

        if self.associated_party_practitioner_id is not None and not isinstance(self.associated_party_practitioner_id, PractitionerPractitionerId):
            self.associated_party_practitioner_id = PractitionerPractitionerId(self.associated_party_practitioner_id)

        if self.associated_party_practitioner_role_id is not None and not isinstance(self.associated_party_practitioner_role_id, PractitionerRolePractitionerRoleId):
            self.associated_party_practitioner_role_id = PractitionerRolePractitionerRoleId(self.associated_party_practitioner_role_id)

        if self.associated_party_institution_id is not None and not isinstance(self.associated_party_institution_id, PractitionerRolePractitionerRoleId):
            self.associated_party_institution_id = PractitionerRolePractitionerRoleId(self.associated_party_institution_id)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class Institution(HasExternalId):
    """
    Institution related to study or research personnel
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = KFI["institution/Institution"]
    class_class_curie: ClassVar[str] = "kfi:institution/Institution"
    class_name: ClassVar[str] = "Institution"
    class_model_uri: ClassVar[URIRef] = KFI_FHIR_SPARKS.Institution

    institution_id: Union[str, InstitutionInstitutionId] = None
    name: Optional[str] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.institution_id):
            self.MissingRequiredField("institution_id")
        if not isinstance(self.institution_id, InstitutionInstitutionId):
            self.institution_id = InstitutionInstitutionId(self.institution_id)

        if self.name is not None and not isinstance(self.name, str):
            self.name = str(self.name)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class Participant(HasExternalId):
    """
    Research oriented patient
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = KFI["participant/Participant"]
    class_class_curie: ClassVar[str] = "kfi:participant/Participant"
    class_name: ClassVar[str] = "Participant"
    class_model_uri: ClassVar[URIRef] = KFI_FHIR_SPARKS.Participant

    participant_id: Union[str, ParticipantParticipantId] = None
    race: Union[Union[str, "EnumRace"], list[Union[str, "EnumRace"]]] = None
    ethnicity: Union[str, "EnumEthnicity"] = None
    birthsex: Optional[Union[str, "EnumBirthSex"]] = None
    population: Optional[Union[str, "EnumPopulation"]] = None
    dob: Optional[str] = None
    dob_method: Optional[Union[str, "EnumDobMethod"]] = None
    age_at_last_vital: Optional[str] = None
    is_deceased: Optional[Union[bool, Bool]] = None
    deceased_rel: Optional[Union[str, RelativeDateTimeId]] = None
    patient_knowledge_source: Optional[Union[str, "EnumPatientKnowledgeSource"]] = None
    family_global_id: Optional[Union[str, FamilyFamilyGlobalId]] = None
    sample_id: Optional[Union[Union[str, SampleSampleId], list[Union[str, SampleSampleId]]]] = empty_list()

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.participant_id):
            self.MissingRequiredField("participant_id")
        if not isinstance(self.participant_id, ParticipantParticipantId):
            self.participant_id = ParticipantParticipantId(self.participant_id)

        if self._is_empty(self.race):
            self.MissingRequiredField("race")
        if not isinstance(self.race, list):
            self.race = [self.race] if self.race is not None else []
        self.race = [v if isinstance(v, EnumRace) else EnumRace(v) for v in self.race]

        if self._is_empty(self.ethnicity):
            self.MissingRequiredField("ethnicity")
        if not isinstance(self.ethnicity, EnumEthnicity):
            self.ethnicity = EnumEthnicity(self.ethnicity)

        if self.birthsex is not None and not isinstance(self.birthsex, EnumBirthSex):
            self.birthsex = EnumBirthSex(self.birthsex)

        if self.dob is not None and not isinstance(self.dob, str):
            self.dob = str(self.dob)

        if self.dob_method is not None and not isinstance(self.dob_method, EnumDobMethod):
            self.dob_method = EnumDobMethod(self.dob_method)

        if self.age_at_last_vital is not None and not isinstance(self.age_at_last_vital, str):
            self.age_at_last_vital = str(self.age_at_last_vital)

        if self.is_deceased is not None and not isinstance(self.is_deceased, Bool):
            self.is_deceased = Bool(self.is_deceased)

        if self.deceased_rel is not None and not isinstance(self.deceased_rel, RelativeDateTimeId):
            self.deceased_rel = RelativeDateTimeId(self.deceased_rel)

        if self.patient_knowledge_source is not None and not isinstance(self.patient_knowledge_source, EnumPatientKnowledgeSource):
            self.patient_knowledge_source = EnumPatientKnowledgeSource(self.patient_knowledge_source)

        if self.family_global_id is not None and not isinstance(self.family_global_id, FamilyFamilyGlobalId):
            self.family_global_id = FamilyFamilyGlobalId(self.family_global_id)

        if not isinstance(self.sample_id, list):
            self.sample_id = [self.sample_id] if self.sample_id is not None else []
        self.sample_id = [v if isinstance(v, SampleSampleId) else SampleSampleId(v) for v in self.sample_id]

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class Person(YAMLRoot):
    """
    Relate one or more participants to a single person entity
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = KFI["person/Person"]
    class_class_curie: ClassVar[str] = "kfi:person/Person"
    class_name: ClassVar[str] = "Person"
    class_model_uri: ClassVar[URIRef] = KFI_FHIR_SPARKS.Person

    person_id: Union[str, PersonPersonId] = None
    participant_id: Union[Union[str, ParticipantParticipantId], list[Union[str, ParticipantParticipantId]]] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.person_id):
            self.MissingRequiredField("person_id")
        if not isinstance(self.person_id, PersonPersonId):
            self.person_id = PersonPersonId(self.person_id)

        if self._is_empty(self.participant_id):
            self.MissingRequiredField("participant_id")
        if not isinstance(self.participant_id, list):
            self.participant_id = [self.participant_id] if self.participant_id is not None else []
        self.participant_id = [v if isinstance(v, ParticipantParticipantId) else ParticipantParticipantId(v) for v in self.participant_id]

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class Period(YAMLRoot):
    """
    Time period associated with some FHIR resource
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = KFI["period/Period"]
    class_class_curie: ClassVar[str] = "kfi:period/Period"
    class_name: ClassVar[str] = "Period"
    class_model_uri: ClassVar[URIRef] = KFI_FHIR_SPARKS.Period

    period_id: Union[str, PeriodPeriodId] = None
    start: Optional[Union[str, XSDDate]] = None
    end: Optional[Union[str, XSDDate]] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.period_id):
            self.MissingRequiredField("period_id")
        if not isinstance(self.period_id, PeriodPeriodId):
            self.period_id = PeriodPeriodId(self.period_id)

        if self.start is not None and not isinstance(self.start, XSDDate):
            self.start = XSDDate(self.start)

        if self.end is not None and not isinstance(self.end, XSDDate):
            self.end = XSDDate(self.end)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class PractitionerRole(YAMLRoot):
    """
    PractitionerRole covers the recording of the location and types of services that Practitioners are able to provide
    for an organization.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = KFI["practitioner_role/PractitionerRole"]
    class_class_curie: ClassVar[str] = "kfi:practitioner_role/PractitionerRole"
    class_name: ClassVar[str] = "PractitionerRole"
    class_model_uri: ClassVar[URIRef] = KFI_FHIR_SPARKS.PractitionerRole

    practitioner_role_id: Union[str, PractitionerRolePractitionerRoleId] = None
    institution_id: Optional[Union[str, InstitutionInstitutionId]] = None
    practitioner_id: Optional[str] = None
    period_id: Optional[Union[str, PeriodPeriodId]] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.practitioner_role_id):
            self.MissingRequiredField("practitioner_role_id")
        if not isinstance(self.practitioner_role_id, PractitionerRolePractitionerRoleId):
            self.practitioner_role_id = PractitionerRolePractitionerRoleId(self.practitioner_role_id)

        if self.institution_id is not None and not isinstance(self.institution_id, InstitutionInstitutionId):
            self.institution_id = InstitutionInstitutionId(self.institution_id)

        if self.practitioner_id is not None and not isinstance(self.practitioner_id, str):
            self.practitioner_id = str(self.practitioner_id)

        if self.period_id is not None and not isinstance(self.period_id, PeriodPeriodId):
            self.period_id = PeriodPeriodId(self.period_id)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class StudyMembership(YAMLRoot):
    """
    Grouping subject participation within a research study is helpful to provide definitive lists of participants that
    fit a specific criteria such as All Participants or Participants From a Particular Consent Group, etc.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = KFI["study-membership/StudyMembership"]
    class_class_curie: ClassVar[str] = "kfi:study-membership/StudyMembership"
    class_name: ClassVar[str] = "StudyMembership"
    class_model_uri: ClassVar[URIRef] = KFI_FHIR_SPARKS.StudyMembership

    study_membership_id: Union[str, StudyMembershipStudyMembershipId] = None
    access_policy_id: Union[str, AccessPolicyAccessPolicyId] = None
    participant_id: Union[Union[str, ParticipantParticipantId], list[Union[str, ParticipantParticipantId]]] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.study_membership_id):
            self.MissingRequiredField("study_membership_id")
        if not isinstance(self.study_membership_id, StudyMembershipStudyMembershipId):
            self.study_membership_id = StudyMembershipStudyMembershipId(self.study_membership_id)

        if self._is_empty(self.access_policy_id):
            self.MissingRequiredField("access_policy_id")
        if not isinstance(self.access_policy_id, AccessPolicyAccessPolicyId):
            self.access_policy_id = AccessPolicyAccessPolicyId(self.access_policy_id)

        if self._is_empty(self.participant_id):
            self.MissingRequiredField("participant_id")
        if not isinstance(self.participant_id, list):
            self.participant_id = [self.participant_id] if self.participant_id is not None else []
        self.participant_id = [v if isinstance(v, ParticipantParticipantId) else ParticipantParticipantId(v) for v in self.participant_id]

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class ResearchStudy(HasExternalId):
    """
    The NCPI Research Study FHIR resource represents an individual research effort and acts as a grouper or
    “container” for that effort’s study participants and their related data files.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = KFI["research_study/ResearchStudy"]
    class_class_curie: ClassVar[str] = "kfi:research_study/ResearchStudy"
    class_name: ClassVar[str] = "ResearchStudy"
    class_model_uri: ClassVar[URIRef] = KFI_FHIR_SPARKS.ResearchStudy

    research_study_id: Union[str, ResearchStudyResearchStudyId] = None
    study_status: Union[str, "EnumStudyStatus"] = None
    study_personnel: Union[Union[str, AssociatedPartyId], list[Union[str, AssociatedPartyId]]] = None
    study_membership_id: Union[str, list[str]] = None
    study_title: Optional[str] = None
    parent_study_id: Optional[Union[str, ResearchStudyResearchStudyId]] = None
    study_focus: Optional[Union[Union[str, URIorCURIE], list[Union[str, URIorCURIE]]]] = empty_list()
    description: Optional[str] = None
    study_condition: Optional[Union[Union[str, URIorCURIE], list[Union[str, URIorCURIE]]]] = empty_list()
    study_acknowledgement: Optional[Union[str, list[str]]] = empty_list()
    study_design: Optional[Union[Union[str, URIorCURIE], list[Union[str, URIorCURIE]]]] = empty_list()

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.research_study_id):
            self.MissingRequiredField("research_study_id")
        if not isinstance(self.research_study_id, ResearchStudyResearchStudyId):
            self.research_study_id = ResearchStudyResearchStudyId(self.research_study_id)

        if self._is_empty(self.study_status):
            self.MissingRequiredField("study_status")
        if not isinstance(self.study_status, EnumStudyStatus):
            self.study_status = EnumStudyStatus(self.study_status)

        if self._is_empty(self.study_personnel):
            self.MissingRequiredField("study_personnel")
        if not isinstance(self.study_personnel, list):
            self.study_personnel = [self.study_personnel] if self.study_personnel is not None else []
        self.study_personnel = [v if isinstance(v, AssociatedPartyId) else AssociatedPartyId(v) for v in self.study_personnel]

        if self._is_empty(self.study_membership_id):
            self.MissingRequiredField("study_membership_id")
        if not isinstance(self.study_membership_id, list):
            self.study_membership_id = [self.study_membership_id] if self.study_membership_id is not None else []
        self.study_membership_id = [v if isinstance(v, str) else str(v) for v in self.study_membership_id]

        if self.study_title is not None and not isinstance(self.study_title, str):
            self.study_title = str(self.study_title)

        if self.parent_study_id is not None and not isinstance(self.parent_study_id, ResearchStudyResearchStudyId):
            self.parent_study_id = ResearchStudyResearchStudyId(self.parent_study_id)

        if not isinstance(self.study_focus, list):
            self.study_focus = [self.study_focus] if self.study_focus is not None else []
        self.study_focus = [v if isinstance(v, URIorCURIE) else URIorCURIE(v) for v in self.study_focus]

        if self.description is not None and not isinstance(self.description, str):
            self.description = str(self.description)

        if not isinstance(self.study_condition, list):
            self.study_condition = [self.study_condition] if self.study_condition is not None else []
        self.study_condition = [v if isinstance(v, URIorCURIE) else URIorCURIE(v) for v in self.study_condition]

        if not isinstance(self.study_acknowledgement, list):
            self.study_acknowledgement = [self.study_acknowledgement] if self.study_acknowledgement is not None else []
        self.study_acknowledgement = [v if isinstance(v, str) else str(v) for v in self.study_acknowledgement]

        if not isinstance(self.study_design, list):
            self.study_design = [self.study_design] if self.study_design is not None else []
        self.study_design = [v if isinstance(v, URIorCURIE) else URIorCURIE(v) for v in self.study_design]

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class ResearchStudyCollection(HasExternalId):
    """
    Collections of research data including, but not limited, to Consortia, Programs, adhoc collections of Studies and
    datasets among other types of collections.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = KFI["research-study-collection/ResearchStudyCollection"]
    class_class_curie: ClassVar[str] = "kfi:research-study-collection/ResearchStudyCollection"
    class_name: ClassVar[str] = "ResearchStudyCollection"
    class_model_uri: ClassVar[URIRef] = KFI_FHIR_SPARKS.ResearchStudyCollection

    research_study_collection_id: Union[str, ResearchStudyCollectionResearchStudyCollectionId] = None
    collection_title: str = None
    research_study_collection_type: Union[str, "EnumResearchCollectionType"] = None
    collection_status: Union[str, "EnumCollectionStatus"] = None
    research_study_collection_member_id: Union[Union[str, ResearchStudyResearchStudyId], list[Union[str, ResearchStudyResearchStudyId]]] = None
    label: Optional[Union[str, list[str]]] = empty_list()
    website: Optional[Union[str, URI]] = None
    description: Optional[str] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.research_study_collection_id):
            self.MissingRequiredField("research_study_collection_id")
        if not isinstance(self.research_study_collection_id, ResearchStudyCollectionResearchStudyCollectionId):
            self.research_study_collection_id = ResearchStudyCollectionResearchStudyCollectionId(self.research_study_collection_id)

        if self._is_empty(self.collection_title):
            self.MissingRequiredField("collection_title")
        if not isinstance(self.collection_title, str):
            self.collection_title = str(self.collection_title)

        if self._is_empty(self.research_study_collection_type):
            self.MissingRequiredField("research_study_collection_type")
        if not isinstance(self.research_study_collection_type, EnumResearchCollectionType):
            self.research_study_collection_type = EnumResearchCollectionType(self.research_study_collection_type)

        if self._is_empty(self.collection_status):
            self.MissingRequiredField("collection_status")
        if not isinstance(self.collection_status, EnumCollectionStatus):
            self.collection_status = EnumCollectionStatus(self.collection_status)

        if self._is_empty(self.research_study_collection_member_id):
            self.MissingRequiredField("research_study_collection_member_id")
        if not isinstance(self.research_study_collection_member_id, list):
            self.research_study_collection_member_id = [self.research_study_collection_member_id] if self.research_study_collection_member_id is not None else []
        self.research_study_collection_member_id = [v if isinstance(v, ResearchStudyResearchStudyId) else ResearchStudyResearchStudyId(v) for v in self.research_study_collection_member_id]

        if not isinstance(self.label, list):
            self.label = [self.label] if self.label is not None else []
        self.label = [v if isinstance(v, str) else str(v) for v in self.label]

        if self.website is not None and not isinstance(self.website, URI):
            self.website = URI(self.website)

        if self.description is not None and not isinstance(self.description, str):
            self.description = str(self.description)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class Sample(HasExternalId):
    """
    Sample encompasses biospecimen collection, sample information, and aliquot information.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = KFI["sample/Sample"]
    class_class_curie: ClassVar[str] = "kfi:sample/Sample"
    class_name: ClassVar[str] = "Sample"
    class_model_uri: ClassVar[URIRef] = KFI_FHIR_SPARKS.Sample

    sample_id: Union[str, SampleSampleId] = None
    participant_id: Union[str, ParticipantParticipantId] = None
    sample_type: Union[str, URIorCURIE] = None
    parent_sample_id: Optional[Union[str, SampleSampleId]] = None
    age_at_collection: Optional[Union[str, AgeAtId]] = None
    collection_method: Optional[Union[str, URIorCURIE]] = None
    collection_site: Optional[Union[str, URIorCURIE]] = None
    spatial_qualifier: Optional[Union[str, URIorCURIE]] = None
    laterality: Optional[Union[str, URIorCURIE]] = None
    processing: Optional[Union[Union[str, URIorCURIE], list[Union[str, URIorCURIE]]]] = empty_list()
    availability_status: Optional[Union[str, "EnumSpecimenAvailability"]] = None
    storage_method: Optional[Union[str, URIorCURIE]] = None
    quantity: Optional[float] = None
    quantity_units: Optional[Union[str, URIorCURIE]] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.sample_id):
            self.MissingRequiredField("sample_id")
        if not isinstance(self.sample_id, SampleSampleId):
            self.sample_id = SampleSampleId(self.sample_id)

        if self._is_empty(self.participant_id):
            self.MissingRequiredField("participant_id")
        if not isinstance(self.participant_id, ParticipantParticipantId):
            self.participant_id = ParticipantParticipantId(self.participant_id)

        if self._is_empty(self.sample_type):
            self.MissingRequiredField("sample_type")
        if not isinstance(self.sample_type, URIorCURIE):
            self.sample_type = URIorCURIE(self.sample_type)

        if self.parent_sample_id is not None and not isinstance(self.parent_sample_id, SampleSampleId):
            self.parent_sample_id = SampleSampleId(self.parent_sample_id)

        if self.age_at_collection is not None and not isinstance(self.age_at_collection, AgeAtId):
            self.age_at_collection = AgeAtId(self.age_at_collection)

        if self.collection_method is not None and not isinstance(self.collection_method, URIorCURIE):
            self.collection_method = URIorCURIE(self.collection_method)

        if self.collection_site is not None and not isinstance(self.collection_site, URIorCURIE):
            self.collection_site = URIorCURIE(self.collection_site)

        if self.spatial_qualifier is not None and not isinstance(self.spatial_qualifier, URIorCURIE):
            self.spatial_qualifier = URIorCURIE(self.spatial_qualifier)

        if self.laterality is not None and not isinstance(self.laterality, URIorCURIE):
            self.laterality = URIorCURIE(self.laterality)

        if not isinstance(self.processing, list):
            self.processing = [self.processing] if self.processing is not None else []
        self.processing = [v if isinstance(v, URIorCURIE) else URIorCURIE(v) for v in self.processing]

        if self.availability_status is not None and not isinstance(self.availability_status, EnumSpecimenAvailability):
            self.availability_status = EnumSpecimenAvailability(self.availability_status)

        if self.storage_method is not None and not isinstance(self.storage_method, URIorCURIE):
            self.storage_method = URIorCURIE(self.storage_method)

        if self.quantity is not None and not isinstance(self.quantity, float):
            self.quantity = float(self.quantity)

        if self.quantity_units is not None and not isinstance(self.quantity_units, URIorCURIE):
            self.quantity_units = URIorCURIE(self.quantity_units)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class Aliquot(HasExternalId):
    """
    A Portion of a sample extracted from a participant.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = KFI["sample/Aliquot"]
    class_class_curie: ClassVar[str] = "kfi:sample/Aliquot"
    class_name: ClassVar[str] = "Aliquot"
    class_model_uri: ClassVar[URIRef] = KFI_FHIR_SPARKS.Aliquot

    aliquot_id: Union[str, AliquotAliquotId] = None
    sample_id: Union[str, SampleSampleId] = None
    availability_status: Optional[Union[str, "EnumSpecimenAvailability"]] = None
    volume: Optional[float] = None
    volume_units: Optional[Union[str, URIorCURIE]] = None
    concentration: Optional[Union[str, URIorCURIE]] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.aliquot_id):
            self.MissingRequiredField("aliquot_id")
        if not isinstance(self.aliquot_id, AliquotAliquotId):
            self.aliquot_id = AliquotAliquotId(self.aliquot_id)

        if self._is_empty(self.sample_id):
            self.MissingRequiredField("sample_id")
        if not isinstance(self.sample_id, SampleSampleId):
            self.sample_id = SampleSampleId(self.sample_id)

        if self.availability_status is not None and not isinstance(self.availability_status, EnumSpecimenAvailability):
            self.availability_status = EnumSpecimenAvailability(self.availability_status)

        if self.volume is not None and not isinstance(self.volume, float):
            self.volume = float(self.volume)

        if self.volume_units is not None and not isinstance(self.volume_units, URIorCURIE):
            self.volume_units = URIorCURIE(self.volume_units)

        if self.concentration is not None and not isinstance(self.concentration, URIorCURIE):
            self.concentration = URIorCURIE(self.concentration)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class NCPIFile(HasExternalId):
    """
    Information about a file related to a research participant
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = KFI["ncpi-file/NCPIFile"]
    class_class_curie: ClassVar[str] = "kfi:ncpi-file/NCPIFile"
    class_name: ClassVar[str] = "NCPIFile"
    class_model_uri: ClassVar[URIRef] = KFI_FHIR_SPARKS.NCPIFile

    file_global_id: Union[str, NCPIFileFileGlobalId] = None
    participant_id: Union[str, ParticipantParticipantId] = None
    file_format: Union[str, URIorCURIE] = None
    file_location_id: Union[Union[str, FileLocationFileLocationId], list[Union[str, FileLocationFileLocationId]]] = None
    file_size: float = None
    file_size_unit: Union[str, URIorCURIE] = None
    file_type: Union[str, URIorCURIE] = None
    file_hash: str = None
    file_meta_data_id: Optional[Union[Union[str, FileMetaDataFileMetaDataId], list[Union[str, FileMetaDataFileMetaDataId]]]] = empty_list()
    content_version: Optional[str] = None
    file_hash_type: Optional[Union[str, URIorCURIE]] = None
    description: Optional[str] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.file_global_id):
            self.MissingRequiredField("file_global_id")
        if not isinstance(self.file_global_id, NCPIFileFileGlobalId):
            self.file_global_id = NCPIFileFileGlobalId(self.file_global_id)

        if self._is_empty(self.participant_id):
            self.MissingRequiredField("participant_id")
        if not isinstance(self.participant_id, ParticipantParticipantId):
            self.participant_id = ParticipantParticipantId(self.participant_id)

        if self._is_empty(self.file_format):
            self.MissingRequiredField("file_format")
        if not isinstance(self.file_format, URIorCURIE):
            self.file_format = URIorCURIE(self.file_format)

        if self._is_empty(self.file_location_id):
            self.MissingRequiredField("file_location_id")
        if not isinstance(self.file_location_id, list):
            self.file_location_id = [self.file_location_id] if self.file_location_id is not None else []
        self.file_location_id = [v if isinstance(v, FileLocationFileLocationId) else FileLocationFileLocationId(v) for v in self.file_location_id]

        if self._is_empty(self.file_size):
            self.MissingRequiredField("file_size")
        if not isinstance(self.file_size, float):
            self.file_size = float(self.file_size)

        if self._is_empty(self.file_size_unit):
            self.MissingRequiredField("file_size_unit")
        if not isinstance(self.file_size_unit, URIorCURIE):
            self.file_size_unit = URIorCURIE(self.file_size_unit)

        if self._is_empty(self.file_type):
            self.MissingRequiredField("file_type")
        if not isinstance(self.file_type, URIorCURIE):
            self.file_type = URIorCURIE(self.file_type)

        if self._is_empty(self.file_hash):
            self.MissingRequiredField("file_hash")
        if not isinstance(self.file_hash, str):
            self.file_hash = str(self.file_hash)

        if not isinstance(self.file_meta_data_id, list):
            self.file_meta_data_id = [self.file_meta_data_id] if self.file_meta_data_id is not None else []
        self.file_meta_data_id = [v if isinstance(v, FileMetaDataFileMetaDataId) else FileMetaDataFileMetaDataId(v) for v in self.file_meta_data_id]

        if self.content_version is not None and not isinstance(self.content_version, str):
            self.content_version = str(self.content_version)

        if self.file_hash_type is not None and not isinstance(self.file_hash_type, URIorCURIE):
            self.file_hash_type = URIorCURIE(self.file_hash_type)

        if self.description is not None and not isinstance(self.description, str):
            self.description = str(self.description)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class FileLocation(YAMLRoot):
    """
    Details relating to the links where documents are found
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = KFI["file-location/FileLocation"]
    class_class_curie: ClassVar[str] = "kfi:file-location/FileLocation"
    class_name: ClassVar[str] = "FileLocation"
    class_model_uri: ClassVar[URIRef] = KFI_FHIR_SPARKS.FileLocation

    file_location_id: Union[Union[str, FileLocationFileLocationId], list[Union[str, FileLocationFileLocationId]]] = None
    location_uri: Union[str, URI] = None
    file_name: str = None
    access_policy_id: Union[str, AccessPolicyAccessPolicyId] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.file_location_id):
            self.MissingRequiredField("file_location_id")
        if not isinstance(self.file_location_id, list):
            self.file_location_id = [self.file_location_id] if self.file_location_id is not None else []
        self.file_location_id = [v if isinstance(v, FileLocationFileLocationId) else FileLocationFileLocationId(v) for v in self.file_location_id]

        if self._is_empty(self.location_uri):
            self.MissingRequiredField("location_uri")
        if not isinstance(self.location_uri, URI):
            self.location_uri = URI(self.location_uri)

        if self._is_empty(self.file_name):
            self.MissingRequiredField("file_name")
        if not isinstance(self.file_name, str):
            self.file_name = str(self.file_name)

        if self._is_empty(self.access_policy_id):
            self.MissingRequiredField("access_policy_id")
        if not isinstance(self.access_policy_id, AccessPolicyAccessPolicyId):
            self.access_policy_id = AccessPolicyAccessPolicyId(self.access_policy_id)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class FamilyRelationship(YAMLRoot):
    """
    A relationship between individuals in a pedigree or family.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = KFI["family-relationship/FamilyRelationship"]
    class_class_curie: ClassVar[str] = "kfi:family-relationship/FamilyRelationship"
    class_name: ClassVar[str] = "FamilyRelationship"
    class_model_uri: ClassVar[URIRef] = KFI_FHIR_SPARKS.FamilyRelationship

    family_relationship_global_id: Union[str, FamilyRelationshipFamilyRelationshipGlobalId] = None
    patient_id: Union[str, ParticipantParticipantId] = None
    relative_id: Union[str, ParticipantParticipantId] = None
    relationship: Union[str, "EnumFamilyRelationship"] = None
    knowledge_source: Union[str, "EnumRelationshipKnowledgeSource"] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.family_relationship_global_id):
            self.MissingRequiredField("family_relationship_global_id")
        if not isinstance(self.family_relationship_global_id, FamilyRelationshipFamilyRelationshipGlobalId):
            self.family_relationship_global_id = FamilyRelationshipFamilyRelationshipGlobalId(self.family_relationship_global_id)

        if self._is_empty(self.patient_id):
            self.MissingRequiredField("patient_id")
        if not isinstance(self.patient_id, ParticipantParticipantId):
            self.patient_id = ParticipantParticipantId(self.patient_id)

        if self._is_empty(self.relative_id):
            self.MissingRequiredField("relative_id")
        if not isinstance(self.relative_id, ParticipantParticipantId):
            self.relative_id = ParticipantParticipantId(self.relative_id)

        if self._is_empty(self.relationship):
            self.MissingRequiredField("relationship")
        if not isinstance(self.relationship, EnumFamilyRelationship):
            self.relationship = EnumFamilyRelationship(self.relationship)

        if self._is_empty(self.knowledge_source):
            self.MissingRequiredField("knowledge_source")
        if not isinstance(self.knowledge_source, EnumRelationshipKnowledgeSource):
            self.knowledge_source = EnumRelationshipKnowledgeSource(self.knowledge_source)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class Family(HasExternalId):
    """
    Group of Participants that are related.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = KFI["family/Family"]
    class_class_curie: ClassVar[str] = "kfi:family/Family"
    class_name: ClassVar[str] = "Family"
    class_model_uri: ClassVar[URIRef] = KFI_FHIR_SPARKS.Family

    family_global_id: Union[str, FamilyFamilyGlobalId] = None
    family_id: str = None
    family_type: Union[str, "EnumFamilyType"] = None
    description: Optional[str] = None
    consanguinity: Optional[Union[str, "EnumConsanguinity"]] = None
    family_focus: Optional[Union[str, URIorCURIE]] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.family_global_id):
            self.MissingRequiredField("family_global_id")
        if not isinstance(self.family_global_id, FamilyFamilyGlobalId):
            self.family_global_id = FamilyFamilyGlobalId(self.family_global_id)

        if self._is_empty(self.family_id):
            self.MissingRequiredField("family_id")
        if not isinstance(self.family_id, str):
            self.family_id = str(self.family_id)

        if self._is_empty(self.family_type):
            self.MissingRequiredField("family_type")
        if not isinstance(self.family_type, EnumFamilyType):
            self.family_type = EnumFamilyType(self.family_type)

        if self.description is not None and not isinstance(self.description, str):
            self.description = str(self.description)

        if self.consanguinity is not None and not isinstance(self.consanguinity, EnumConsanguinity):
            self.consanguinity = EnumConsanguinity(self.consanguinity)

        if self.family_focus is not None and not isinstance(self.family_focus, URIorCURIE):
            self.family_focus = URIorCURIE(self.family_focus)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class FileMetaData(YAMLRoot):
    """
    Representation of file metadata for NCPI
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = KFI["file-meta-data/FileMetaData"]
    class_class_curie: ClassVar[str] = "kfi:file-meta-data/FileMetaData"
    class_name: ClassVar[str] = "FileMetaData"
    class_model_uri: ClassVar[URIRef] = KFI_FHIR_SPARKS.FileMetaData

    file_meta_data_id: Union[Union[str, FileMetaDataFileMetaDataId], list[Union[str, FileMetaDataFileMetaDataId]]] = None
    meta_data_type: Union[str, "EnumFileMetaDataType"] = None
    assay_strategy: Union[str, URIorCURIE] = None
    platform_instrument: Union[str, URIorCURIE] = None
    library_prep: Optional[Union[str, URIorCURIE]] = None
    library_selection: Optional[Union[str, URIorCURIE]] = None
    strandedness: Optional[Union[str, URIorCURIE]] = None
    target_region: Optional[Union[str, URIorCURIE]] = None
    is_paired_end: Optional[Union[str, URIorCURIE]] = None
    adaptor_trimmed: Optional[Union[str, URIorCURIE]] = None
    reference_genome: Optional[Union[str, URIorCURIE]] = None
    workflow_type: Optional[Union[str, URIorCURIE]] = None
    workflow_tool: Optional[Union[str, URIorCURIE]] = None
    related_samples: Optional[Union[str, SampleSampleId]] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.file_meta_data_id):
            self.MissingRequiredField("file_meta_data_id")
        if not isinstance(self.file_meta_data_id, list):
            self.file_meta_data_id = [self.file_meta_data_id] if self.file_meta_data_id is not None else []
        self.file_meta_data_id = [v if isinstance(v, FileMetaDataFileMetaDataId) else FileMetaDataFileMetaDataId(v) for v in self.file_meta_data_id]

        if self._is_empty(self.meta_data_type):
            self.MissingRequiredField("meta_data_type")
        if not isinstance(self.meta_data_type, EnumFileMetaDataType):
            self.meta_data_type = EnumFileMetaDataType(self.meta_data_type)

        if self._is_empty(self.assay_strategy):
            self.MissingRequiredField("assay_strategy")
        if not isinstance(self.assay_strategy, URIorCURIE):
            self.assay_strategy = URIorCURIE(self.assay_strategy)

        if self._is_empty(self.platform_instrument):
            self.MissingRequiredField("platform_instrument")
        if not isinstance(self.platform_instrument, URIorCURIE):
            self.platform_instrument = URIorCURIE(self.platform_instrument)

        if self.library_prep is not None and not isinstance(self.library_prep, URIorCURIE):
            self.library_prep = URIorCURIE(self.library_prep)

        if self.library_selection is not None and not isinstance(self.library_selection, URIorCURIE):
            self.library_selection = URIorCURIE(self.library_selection)

        if self.strandedness is not None and not isinstance(self.strandedness, URIorCURIE):
            self.strandedness = URIorCURIE(self.strandedness)

        if self.target_region is not None and not isinstance(self.target_region, URIorCURIE):
            self.target_region = URIorCURIE(self.target_region)

        if self.is_paired_end is not None and not isinstance(self.is_paired_end, URIorCURIE):
            self.is_paired_end = URIorCURIE(self.is_paired_end)

        if self.adaptor_trimmed is not None and not isinstance(self.adaptor_trimmed, URIorCURIE):
            self.adaptor_trimmed = URIorCURIE(self.adaptor_trimmed)

        if self.reference_genome is not None and not isinstance(self.reference_genome, URIorCURIE):
            self.reference_genome = URIorCURIE(self.reference_genome)

        if self.workflow_type is not None and not isinstance(self.workflow_type, URIorCURIE):
            self.workflow_type = URIorCURIE(self.workflow_type)

        if self.workflow_tool is not None and not isinstance(self.workflow_tool, URIorCURIE):
            self.workflow_tool = URIorCURIE(self.workflow_tool)

        if self.related_samples is not None and not isinstance(self.related_samples, SampleSampleId):
            self.related_samples = SampleSampleId(self.related_samples)

        super().__post_init__(**kwargs)


# Enumerations
class EnumAccessPolicyCode(EnumDefinitionImpl):
    """
    Type of research use case allowed
    """
    gru = PermissibleValue(
        text="gru",
        title="GRU",
        description="General Research Use",
        meaning=NCPI_DATA_ACCESS_CODE["GRU"])
    hmb = PermissibleValue(
        text="hmb",
        title="HMB",
        description="Health/Medical/Biomedical",
        meaning=NCPI_DATA_ACCESS_CODE["HMB"])
    ds = PermissibleValue(
        text="ds",
        title="DS",
        description="Disease-Specific (Disease/Trait/Exposure)",
        meaning=NCPI_DATA_ACCESS_CODE["DS"])
    irb = PermissibleValue(
        text="irb",
        title="IRB",
        description="IRB Approval Required",
        meaning=NCPI_DATA_ACCESS_CODE["IRB"])
    pub = PermissibleValue(
        text="pub",
        title="PUB",
        description="Publication Required",
        meaning=NCPI_DATA_ACCESS_CODE["PUB"])
    col = PermissibleValue(
        text="col",
        title="COL",
        description="Collaboration Required",
        meaning=NCPI_DATA_ACCESS_CODE["COL"])
    npu = PermissibleValue(
        text="npu",
        title="NPU",
        description="Not-for-profit use only",
        meaning=NCPI_DATA_ACCESS_CODE["NPU"])
    mds = PermissibleValue(
        text="mds",
        title="MDS",
        description="Methods",
        meaning=NCPI_DATA_ACCESS_CODE["MDS"])
    gso = PermissibleValue(
        text="gso",
        title="GSO",
        description="Genetic Studies only",
        meaning=NCPI_DATA_ACCESS_CODE["GSO"])
    gsr = PermissibleValue(
        text="gsr",
        title="GSR",
        description="Genomic Summary Results",
        meaning=NCPI_DATA_ACCESS_CODE["GSR"])
    rd = PermissibleValue(
        text="rd",
        title="RD",
        description="Related Diseases",
        meaning=NCPI_DATA_ACCESS_CODE["RD"])
    duo_0000004 = PermissibleValue(
        text="duo_0000004",
        title="no restriction",
        description="This data use permission indicates there is no restriction on use.",
        meaning=DUO["0000004"])
    duo_0000042 = PermissibleValue(
        text="duo_0000042",
        title="general research use",
        description="""This data use permission indicates that use is allowed for general research use for any research purpose.""",
        meaning=DUO["0000042"])
    duo_0000006 = PermissibleValue(
        text="duo_0000006",
        title="health or medical or biomedical research",
        description="""This data use permission indicates that use is allowed for health/medical/biomedical purposes; does not include the study of population origins or ancestry.""",
        meaning=DUO["0000006"])
    duo_0000007 = PermissibleValue(
        text="duo_0000007",
        title="disease specific research",
        description="""This data use permission indicates that use is allowed provided it is related to the specified disease.""",
        meaning=DUO["0000007"])
    duo_0000011 = PermissibleValue(
        text="duo_0000011",
        title="population origins or ancestry research only",
        description="""This data use permission indicates that use of the data is limited to the study of population origins or ancestry.""",
        meaning=DUO["0000011"])
    duo_0000012 = PermissibleValue(
        text="duo_0000012",
        title="research specific restrictions",
        description="This data use modifier indicates that use is limited to studies of a certain research type.",
        meaning=DUO["0000012"])
    duo_0000015 = PermissibleValue(
        text="duo_0000015",
        title="no general methods research",
        description="""This data use modifier indicates that use does not allow methods development research (e.g., development of software or algorithms).""",
        meaning=DUO["0000015"])
    duo_0000016 = PermissibleValue(
        text="duo_0000016",
        title="genetic studies only",
        description="""This data use modifier indicates that use is limited to genetic studies only (i.e., studies that include genotype research alone or both genotype and phenotype research, but not phenotype research exclusively)""",
        meaning=DUO["0000016"])
    duo_0000018 = PermissibleValue(
        text="duo_0000018",
        title="not for profit, non commercial use only",
        description="""This data use modifier indicates that use of the data is limited to not-for-profit organizations and not-for-profit use, non-commercial use.""",
        meaning=DUO["0000018"])
    duo_0000019 = PermissibleValue(
        text="duo_0000019",
        title="publication required",
        description="""This data use modifier indicates that requestor agrees to make results of studies using the data available to the larger scientific community.""",
        meaning=DUO["0000019"])
    duo_0000020 = PermissibleValue(
        text="duo_0000020",
        title="collaboration required",
        description="""This data use modifier indicates that the requestor must agree to collaboration with the primary study investigator(s).""",
        meaning=DUO["0000020"])
    duo_0000021 = PermissibleValue(
        text="duo_0000021",
        title="ethics approval required",
        description="""This data use modifier indicates that the requestor must provide documentation of local IRB/ERB approval.""",
        meaning=DUO["0000021"])
    duo_0000022 = PermissibleValue(
        text="duo_0000022",
        title="geographical restriction",
        description="This data use modifier indicates that use is limited to within a specific geographic region.",
        meaning=DUO["0000022"])
    duo_0000024 = PermissibleValue(
        text="duo_0000024",
        title="publication moratorium",
        description="""This data use modifier indicates that requestor agrees not to publish results of studies until a specific date.""",
        meaning=DUO["0000024"])
    duo_0000025 = PermissibleValue(
        text="duo_0000025",
        title="time limit on use",
        description="This data use modifier indicates that use is approved for a specific number of months.",
        meaning=DUO["0000025"])
    duo_0000026 = PermissibleValue(
        text="duo_0000026",
        title="user specific restriction",
        description="This data use modifier indicates that use is limited to use by approved users.",
        meaning=DUO["0000026"])
    duo_0000027 = PermissibleValue(
        text="duo_0000027",
        title="project specific restriction",
        description="This data use modifier indicates that use is limited to use within an approved project.",
        meaning=DUO["0000027"])
    duo_0000028 = PermissibleValue(
        text="duo_0000028",
        title="institution specific restriction",
        description="This data use modifier indicates that use is limited to use within an approved institution.",
        meaning=DUO["0000028"])
    duo_0000029 = PermissibleValue(
        text="duo_0000029",
        title="return to database or resource",
        description="""This data use modifier indicates that the requestor must return derived/enriched data to the database/resource.""",
        meaning=DUO["0000029"])
    duo_0000043 = PermissibleValue(
        text="duo_0000043",
        title="clinical care use",
        description="This data use modifier indicates that use is allowed for clinical use and care.",
        meaning=DUO["0000043"])
    duo_0000044 = PermissibleValue(
        text="duo_0000044",
        title="population origins or ancestry research prohibited",
        description="""This data use modifier indicates use for purposes of population, origin, or ancestry research is prohibited.""",
        meaning=DUO["0000044"])
    duo_0000045 = PermissibleValue(
        text="duo_0000045",
        title="not for profit organisation use only",
        description="""This data use modifier indicates that use of the data is limited to not-for-profit organisations.""",
        meaning=DUO["0000045"])
    duo_0000046 = PermissibleValue(
        text="duo_0000046",
        title="non-commercial use only",
        description="This data use modifier indicates that use of the data is limited to not-for-profit use.",
        meaning=DUO["0000046"])

    _defn = EnumDefinition(
        name="EnumAccessPolicyCode",
        description="Type of research use case allowed",
    )

class EnumConsentScope(EnumDefinitionImpl):
    """
    The four anticipated uses for the Consent Resource.
    """
    adr = PermissibleValue(
        text="adr",
        title="Advanced Care Directive",
        meaning=HL7_CONSENT_SCOPE["adr"])
    research = PermissibleValue(
        text="research",
        title="Research",
        meaning=HL7_CONSENT_SCOPE["research"])
    patient_privacy = PermissibleValue(
        text="patient_privacy",
        title="Patient Privacy",
        meaning=HL7_CONSENT_SCOPE["patient-privacy"])
    treatment = PermissibleValue(
        text="treatment",
        title="Treatment",
        meaning=HL7_CONSENT_SCOPE["treatment"])

    _defn = EnumDefinition(
        name="EnumConsentScope",
        description="The four anticipated uses for the Consent Resource.",
    )

class EnumConsentStateCodes(EnumDefinitionImpl):
    """
    Indicates the state of the consent.
    """
    draft = PermissibleValue(
        text="draft",
        title="Draft",
        meaning=HL7_CONSENT_STATE_CODES["draft"])
    proposed = PermissibleValue(
        text="proposed",
        title="Proposed",
        meaning=HL7_CONSENT_STATE_CODES["proposed"])
    active = PermissibleValue(
        text="active",
        title="Active",
        meaning=HL7_CONSENT_STATE_CODES["active"])
    rejected = PermissibleValue(
        text="rejected",
        title="Rejected",
        meaning=HL7_CONSENT_STATE_CODES["rejected"])
    inactive = PermissibleValue(
        text="inactive",
        title="Inactive",
        meaning=HL7_CONSENT_STATE_CODES["inactive"])
    entered_in_error = PermissibleValue(
        text="entered_in_error",
        title="Entered in Error",
        meaning=HL7_CONSENT_STATE_CODES["entered-in-error"])

    _defn = EnumDefinition(
        name="EnumConsentStateCodes",
        description="Indicates the state of the consent.",
    )

class EnumDataAccessType(EnumDefinitionImpl):
    """
    Enumerated list of access type codes such as 'Open Access', 'Registered Access' and 'Controlled Access'
    """
    open = PermissibleValue(
        text="open",
        title="Open Access",
        meaning=NCPI_DATA_ACCESS_TYPE["open"])
    registered = PermissibleValue(
        text="registered",
        title="Registered",
        meaning=NCPI_DATA_ACCESS_TYPE["registered"])
    controlled = PermissibleValue(
        text="controlled",
        title="Controlled",
        meaning=NCPI_DATA_ACCESS_TYPE["controlled"])
    gsr_restricted = PermissibleValue(
        text="gsr_restricted",
        title="GSR Restricted",
        meaning=NCPI_DATA_ACCESS_TYPE["gsr-restricted"])
    gsr_allowed = PermissibleValue(
        text="gsr_allowed",
        title="GSR Allowed",
        meaning=NCPI_DATA_ACCESS_TYPE["gsr-allowed"])

    _defn = EnumDefinition(
        name="EnumDataAccessType",
        description="""Enumerated list of access type codes such as 'Open Access', 'Registered Access' and 'Controlled Access'""",
    )

class EnumOffsetType(EnumDefinitionImpl):
    """
    Offset Type
    """
    days = PermissibleValue(
        text="days",
        title="Days",
        description="The offset is represented in days")
    years = PermissibleValue(
        text="years",
        title="Years",
        description="The offset is represented in Years")

    _defn = EnumDefinition(
        name="EnumOffsetType",
        description="Offset Type",
    )

class EnumAgeValueType(EnumDefinitionImpl):
    """
    Describes where to look for the data (as value, code, range, etc)
    """
    age = PermissibleValue(
        text="age",
        title="Age",
        description="Age (must also be annotated with age units)")
    code = PermissibleValue(
        text="code",
        title="Age as Code",
        description="Age as Code (ages will be provided as coded values)")
    age_range = PermissibleValue(
        text="age_range",
        title="Age Range",
        description="Age expressed as a range (relative date/time)")
    date = PermissibleValue(
        text="date",
        title="Date",
        description="Rather than an age, we have an actual date for the event's occurence")

    _defn = EnumDefinition(
        name="EnumAgeValueType",
        description="Describes where to look for the data (as value, code, range, etc)",
    )

class EnumEntityAsserter(EnumDefinitionImpl):
    """
    Who recorded this assertion about the Participant? This can support understanding the differences between
    self-report, doctor, trained research staff.
    """
    self_report = PermissibleValue(
        text="self_report",
        title="Self Report",
        description="The participant reported the assertion")
    doctor = PermissibleValue(
        text="doctor",
        title="Doctor",
        description="Physician")
    staff = PermissibleValue(
        text="staff",
        title="Trained Research Staff",
        description="Trained research staff")

    _defn = EnumDefinition(
        name="EnumEntityAsserter",
        description="""Who recorded this assertion about the Participant? This can support understanding the differences between self-report, doctor, trained research staff.""",
    )

class EnumAssertionType(EnumDefinitionImpl):
    """
    Provides options to describe the expressed semantics of a condition.
    """
    phenotypic_feature = PermissibleValue(
        text="phenotypic_feature",
        title="Phenotypic Feature",
        description="This is a phenotypic feature",
        meaning=NCPI_COND_TYPE["Phenotypic-Feature"])
    disease = PermissibleValue(
        text="disease",
        title="disease",
        description="Disease",
        meaning=NCPI_COND_TYPE["Disease"])
    comorbidity = PermissibleValue(
        text="comorbidity",
        title="comorbidity",
        description="Comorbidity",
        meaning=NCPI_COND_TYPE["Comorbidity"])
    histology = PermissibleValue(
        text="histology",
        title="histology",
        description="Histology",
        meaning=NCPI_COND_TYPE["Histology"])
    clinical_finding = PermissibleValue(
        text="clinical_finding",
        title="clinical-finding",
        description="Clinical Finding",
        meaning=NCPI_COND_TYPE["Clinical-Finding"])
    ehr_billing_code = PermissibleValue(
        text="ehr_billing_code",
        title="EHR Billing Code",
        description="From an EHR billing record, which may indicate only investigation into a possible diagnosis.",
        meaning=NCPI_COND_TYPE["EHR-Condition-Code"])
    measurement = PermissibleValue(
        text="measurement",
        title="Measurement",
        description="A measurement of some feature, eg, height or glucose.")

    _defn = EnumDefinition(
        name="EnumAssertionType",
        description="Provides options to describe the expressed semantics of a condition.",
    )

class EnumResearchStudyPartyOrganizationType(EnumDefinitionImpl):
    """
    Research Study Party Organization Type
    """
    nih = PermissibleValue(
        text="nih",
        title="NIH",
        meaning=HL7_RSP_ORG_TYPE["nih"])
    fda = PermissibleValue(
        text="fda",
        title="FDA",
        meaning=HL7_RSP_ORG_TYPE["fda"])
    academic = PermissibleValue(
        text="academic",
        title="Academic",
        meaning=HL7_RSP_ORG_TYPE["academic"])
    government = PermissibleValue(
        text="government",
        title="Government",
        meaning=HL7_RSP_ORG_TYPE["government"])
    nonprofit = PermissibleValue(
        text="nonprofit",
        title="Nonprofit",
        meaning=HL7_RSP_ORG_TYPE["nonprofit"])
    industry = PermissibleValue(
        text="industry",
        title="Industry",
        meaning=HL7_RSP_ORG_TYPE["industry"])

    _defn = EnumDefinition(
        name="EnumResearchStudyPartyOrganizationType",
        description="Research Study Party Organization Type",
    )

class EnumResearchStudyPartyRole(EnumDefinitionImpl):
    """
    This is a ResearchStudy's party role.
    """
    sponsor = PermissibleValue(
        text="sponsor",
        title="sponsor",
        meaning=HL7_RSP_ROLE["sponsor"])
    lead_sponsor = PermissibleValue(
        text="lead_sponsor",
        title="lead-sponsor",
        meaning=HL7_RSP_ROLE["lead-sponsor"])
    sponsor_investigator = PermissibleValue(
        text="sponsor_investigator",
        meaning=HL7_RSP_ROLE["sponsor-investigator"])
    primary_investigator = PermissibleValue(
        text="primary_investigator",
        meaning=HL7_RSP_ROLE["primary-investigator"])
    collaborator = PermissibleValue(
        text="collaborator",
        meaning=HL7_RSP_ROLE["collaborator"])
    funding_source = PermissibleValue(
        text="funding_source",
        meaning=HL7_RSP_ROLE["funding-source"])
    general_contact = PermissibleValue(
        text="general_contact",
        meaning=HL7_RSP_ROLE["general=contact"])
    recruitment_contact = PermissibleValue(
        text="recruitment_contact",
        meaning=HL7_RSP_ROLE["recruitment-contact"])
    sub_investigator = PermissibleValue(
        text="sub_investigator",
        meaning=HL7_RSP_ROLE["sub-investigator"])
    study_director = PermissibleValue(
        text="study_director",
        meaning=HL7_RSP_ROLE["study-director"])
    study_chair = PermissibleValue(
        text="study_chair",
        meaning=HL7_RSP_ROLE["study-chair"])
    irb = PermissibleValue(
        text="irb",
        title="Institutional Review Board",
        meaning=HL7_RSP_ROLE["irb"])

    _defn = EnumDefinition(
        name="EnumResearchStudyPartyRole",
        description="This is a ResearchStudy's party role.",
    )

class EnumBirthSex(EnumDefinitionImpl):
    """
    Codes for assigning sex at birth as specified by the Office of the National Coordinator for Health IT (ONC)
    """
    female = PermissibleValue(
        text="female",
        title="Female",
        description="Female",
        meaning=USC_BIRTHSEX["F"])
    male = PermissibleValue(
        text="male",
        title="Male",
        description="Male",
        meaning=USC_BIRTHSEX["M"])
    asku = PermissibleValue(
        text="asku",
        title="asked but unknown",
        description="Information was sought but not found (e.g., patient was asked but didn't know)",
        meaning=HL7_NULL["ASKU"])
    oth = PermissibleValue(
        text="oth",
        title="other",
        description="""**Description:**The actual value is not a member of the set of permitted data values in the constrained value domain of a variable. (e.g., concept not provided by required code system).
Usage Notes: This flavor and its specializations are most commonly used with the CD datatype and its flavors. However, it may apply to *any* datatype where the constraints of the type are tighter than can be conveyed. For example, a PQ that is for a true measured amount whose units are not supported in UCUM, a need to convey a REAL when the type has been constrained to INT, etc.
With coded datatypes, this null flavor may only be used if the vocabulary binding has a coding strength of CNE. By definition, all local codes and original text are part of the value set if the coding strength is CWE.""",
        meaning=HL7_NULL["OTH"])
    unk = PermissibleValue(
        text="unk",
        title="Unknown",
        description="""*Description:**A proper value is applicable, but not known.
Usage Notes: This means the actual value is not known. If the only thing that is unknown is how to properly express the value in the necessary constraints (value set, datatype, etc.), then the OTH or UNC flavor should be used. No properties should be included for a datatype with this property unless:
Those properties themselves directly translate to a semantic of 'unknown'. (E.g. a local code sent as a translation that conveys 'unknown') Those properties further qualify the nature of what is unknown. (E.g. specifying a use code of 'H' and a URL prefix of 'tel:' to convey that it is the home phone number that is unknown.)""",
        meaning=HL7_NULL["UNK"])

    _defn = EnumDefinition(
        name="EnumBirthSex",
        description="""Codes for assigning sex at birth as specified by the Office of the National Coordinator for Health IT (ONC)""",
    )

class EnumRace(EnumDefinitionImpl):
    """
    OMB Codes describing race.
    """
    american_indian_or_alaskan_native = PermissibleValue(
        text="american_indian_or_alaskan_native",
        title="American Indian or Alaskan Native",
        meaning=CDC_REC["1002-5"])
    asian = PermissibleValue(
        text="asian",
        title="Asian",
        meaning=CDC_REC["2028-9"])
    black_or_african_american = PermissibleValue(
        text="black_or_african_american",
        title="Black or African American",
        meaning=CDC_REC["2054-5"])
    native_hawaiian_or_pacific_islander = PermissibleValue(
        text="native_hawaiian_or_pacific_islander",
        title="Native Hawaiian or Other Pacific Islander",
        meaning=CDC_REC["2076-8"])
    white = PermissibleValue(
        text="white",
        title="White",
        meaning=CDC_REC["2106-3"])
    other_race = PermissibleValue(
        text="other_race",
        title="Other Race",
        meaning=CDC_REC["2131-1"])
    unknown = PermissibleValue(
        text="unknown",
        title="unknown",
        meaning=HL7_NULL["UNK"])
    asked_but_unknown = PermissibleValue(
        text="asked_but_unknown",
        title="asked but unknown",
        meaning=HL7_NULL["ASKU"])

    _defn = EnumDefinition(
        name="EnumRace",
        description="OMB Codes describing race.",
    )

class EnumEthnicity(EnumDefinitionImpl):
    """
    OMB Codes describing Hispanic or Latino ethnicity.
    """
    hispanic_or_latino = PermissibleValue(
        text="hispanic_or_latino",
        description="Hispanic or Latino",
        meaning=CDC_REC["2135-2"])
    not_hispanic_or_latino = PermissibleValue(
        text="not_hispanic_or_latino",
        description="Not Hispanic or Latino",
        meaning=CDC_REC["2186-5"])
    unknown = PermissibleValue(
        text="unknown",
        description="unknown",
        meaning=HL7_NULL["UNK"])
    asked_but_unknown = PermissibleValue(
        text="asked_but_unknown",
        description="asked but unknown",
        meaning=HL7_NULL["ASKU"])

    _defn = EnumDefinition(
        name="EnumEthnicity",
        description="OMB Codes describing Hispanic or Latino ethnicity.",
    )

class EnumPopulation(EnumDefinitionImpl):
    """
    Code describing the population (CDC). This should be one of the codes from the [CDC Race
    codes](https://hl7.org/fhir/us/core/STU6.1/ValueSet-detailed-race.html).
    """
    _defn = EnumDefinition(
        name="EnumPopulation",
        description="""Code describing the population (CDC). This should be one of the codes from the [CDC Race codes](https://hl7.org/fhir/us/core/STU6.1/ValueSet-detailed-race.html).""",
    )

class EnumDobMethod(EnumDefinitionImpl):
    """
    Enumerations for how DOB was constructed
    """
    exact = PermissibleValue(
        text="exact",
        description="Exact",
        meaning=NCPI_DOB_METHOD["exact"])
    year_only = PermissibleValue(
        text="year_only",
        description="Year Only",
        meaning=NCPI_DOB_METHOD["year-only"])
    shifted = PermissibleValue(
        text="shifted",
        description="Shifted",
        meaning=NCPI_DOB_METHOD["shifted"])
    decade_only = PermissibleValue(
        text="decade_only",
        description="Decade Only",
        meaning=NCPI_DOB_METHOD["decade-only"])
    other = PermissibleValue(
        text="other",
        description="Other",
        meaning=NCPI_DOB_METHOD["other"])

    _defn = EnumDefinition(
        name="EnumDobMethod",
        description="Enumerations for how DOB was constructed",
    )

class EnumPatientKnowledgeSource(EnumDefinitionImpl):
    """
    The source of the knowledge represented in a Patient resource.
    """
    traditional = PermissibleValue(
        text="traditional",
        title="Traditional",
        description="""The knowledge comes from traditional sources like a form filled out by a patient or information copied from an external traditional source like government records.""",
        meaning=NCPI_PATIENT_KNOWLEDGE_SOURCE["traditional"])
    inferred = PermissibleValue(
        text="inferred",
        title="Inferred",
        description="""The knowledge is inferred from indirect evidence. For example, the existence of one patient's mother can be inferred from the existence of the patient.""",
        meaning=NCPI_PATIENT_KNOWLEDGE_SOURCE["traditional"])

    _defn = EnumDefinition(
        name="EnumPatientKnowledgeSource",
        description="The source of the knowledge represented in a Patient resource.",
    )

class EnumStudyStatus(EnumDefinitionImpl):
    """
    Codes indicating the study's current status
    """
    active = PermissibleValue(
        text="active",
        title="Active",
        description="Study is opened for accrual.",
        meaning=HL7_STUDY_STATUS["active"])
    administratively_completed = PermissibleValue(
        text="administratively_completed",
        title="Administratively Completed",
        description="""Study is completed prematurely and will not resume; patients are no longer examined nor treated.""",
        meaning=HL7_STUDY_STATUS["administratively-completed"])
    approved = PermissibleValue(
        text="approved",
        title="Approved",
        meaning=HL7_STUDY_STATUS["approved"])
    closed_to_accrual = PermissibleValue(
        text="closed_to_accrual",
        title="Closed to Accrual",
        meaning=KFI_FHIR_SPARKS["closed-to-accrual"])
    closed_to_accrual_and_intervention = PermissibleValue(
        text="closed_to_accrual_and_intervention",
        title="Closed to Accrual and Intervention",
        meaning=HL7_STUDY_STATUS["closed-to-accrual-and-intervention"])
    completed = PermissibleValue(
        text="completed",
        title="Completed",
        meaning=HL7_STUDY_STATUS["completed"])
    disapproved = PermissibleValue(
        text="disapproved",
        title="Disapproved",
        meaning=HL7_STUDY_STATUS["disapproved"])
    in_review = PermissibleValue(
        text="in_review",
        title="In Review",
        meaning=HL7_STUDY_STATUS["in-review"])
    temporarily_closed_to_accrual = PermissibleValue(
        text="temporarily_closed_to_accrual",
        title="Temporarily Closed to Accrual",
        meaning=HL7_STUDY_STATUS["temporarily-closed-to-accrual"])
    temporarily_closed_to_accrual_and_intervention = PermissibleValue(
        text="temporarily_closed_to_accrual_and_intervention",
        title="Temporarily Closed to Accrual and Intervention",
        meaning=HL7_STUDY_STATUS["temporarily-closed-to-accrual-and-intervention"])
    withdrawn = PermissibleValue(
        text="withdrawn",
        title="Withdrawn",
        meaning=HL7_STUDY_STATUS["withdrawn"])

    _defn = EnumDefinition(
        name="EnumStudyStatus",
        description="Codes indicating the study's current status",
    )

class EnumResearchCollectionType(EnumDefinitionImpl):
    """
    Research Study Collection Type
    """
    consortium = PermissibleValue(
        text="consortium",
        title="Consortium",
        meaning=NCPI_COLLECTION_TYPE["consortium"])
    program = PermissibleValue(
        text="program",
        title="Program",
        meaning=NCPI_COLLECTION_TYPE["program"])
    user_defined = PermissibleValue(
        text="user_defined",
        title="User Defined",
        meaning=NCPI_COLLECTION_TYPE["user-defined"])

    _defn = EnumDefinition(
        name="EnumResearchCollectionType",
        description="Research Study Collection Type",
    )

class EnumCollectionStatus(EnumDefinitionImpl):
    """
    The current state of the collection
    """
    current = PermissibleValue(
        text="current",
        title="Current",
        meaning=HL7_LIST_STATUS["current"])
    retired = PermissibleValue(
        text="retired",
        title="Retired",
        meaning=HL7_LIST_STATUS["retired"])

    _defn = EnumDefinition(
        name="EnumCollectionStatus",
        description="The current state of the collection",
    )

class EnumSpecimenAvailability(EnumDefinitionImpl):
    """
    Can this sample be requested for further analysis
    """
    available = PermissibleValue(
        text="available",
        title="Available",
        description="Specimen is currently available",
        meaning=NCPI_SAMPLE_AVAILABILITY["available"])
    unavailable = PermissibleValue(
        text="unavailable",
        title="Unavailable",
        description="Specimen is currently unavailable",
        meaning=NCPI_SAMPLE_AVAILABILITY["unavailable"])

    _defn = EnumDefinition(
        name="EnumSpecimenAvailability",
        description="Can this sample be requested for further analysis",
    )

class EnumFamilyRelationship(EnumDefinitionImpl):
    """
    What is the relative's relationship to the patient
    """
    mother = PermissibleValue(
        text="mother",
        title="Mother",
        description="The relative is the biological mother of the patient.",
        meaning=KIN["027"])
    father = PermissibleValue(
        text="father",
        title="Father",
        description="The relative is the biological father of the patient.",
        meaning=KIN["028"])
    monozygotic_twin = PermissibleValue(
        text="monozygotic_twin",
        title="Monozygotic Twin",
        description="The relative and patient are monozygotic twins",
        meaning=KIN["010"])
    polyzygotic_twin = PermissibleValue(
        text="polyzygotic_twin",
        title="Polyzygotic Twin",
        description="The relative and patient are polyzygotic twins",
        meaning=KIN["011"])
    twin = PermissibleValue(
        text="twin",
        title="Twin",
        description="""The relative and patient are twins, but no further clarification is available (always use the more specific form when possible)""",
        meaning=KIN["009"])
    full_sibling = PermissibleValue(
        text="full_sibling",
        title="Full Sibling",
        description="The relative and child both share the same biological mother and father",
        meaning=KIN["008"])
    half_sibling = PermissibleValue(
        text="half_sibling",
        title="Half Sibling",
        description="The relative and child only share one biological parent",
        meaning=KIN["012"])
    sibling = PermissibleValue(
        text="sibling",
        title="Biological Sibling",
        description="""The relative share at least one biological parent, but there isn't enough information to confirm more then that.""",
        meaning=KIN["007"])

    _defn = EnumDefinition(
        name="EnumFamilyRelationship",
        description="What is the relative's relationship to the patient",
    )

class EnumRelationshipKnowledgeSource(EnumDefinitionImpl):
    """
    Indicate if the relationship is real or inferred
    """
    traditional = PermissibleValue(
        text="traditional",
        title="Traditional",
        description="""The knowledge comes from traditional sources like a form filled out by a patient or information copied from an external traditional source like government records.""",
        meaning=NCPI_PATIENT_KNOWLEDGE_SOURCE["traditional"])
    inferred = PermissibleValue(
        text="inferred",
        title="Inferred",
        description="""The knowledge is inferred from indirect evidence. For example, the existence of one patient's mother can be inferred from the existence of the patient.""",
        meaning=NCPI_PATIENT_KNOWLEDGE_SOURCE["inferred"])

    _defn = EnumDefinition(
        name="EnumRelationshipKnowledgeSource",
        description="Indicate if the relationship is real or inferred",
    )

class EnumFamilyType(EnumDefinitionImpl):
    """
    Describes the 'type' of study family, eg, trio.
    """
    control_only = PermissibleValue(
        text="control_only",
        title="Control Only",
        description="Control Only",
        meaning=NCPI_FAMILY_TYPES["Control-only"])
    duo = PermissibleValue(
        text="duo",
        title="Duo",
        description="Duo",
        meaning=NCPI_FAMILY_TYPES["Duo"])
    trio = PermissibleValue(
        text="trio",
        title="Trio",
        description="Trio",
        meaning=NCPI_FAMILY_TYPES["Trio"])
    trioplus = PermissibleValue(
        text="trioplus",
        title="Trio+",
        description="Trio+",
        meaning=NCPI_FAMILY_TYPES["Trio+"])
    proband_only = PermissibleValue(
        text="proband_only",
        title="Proband Only",
        description="Proband Only",
        meaning=NCPI_FAMILY_TYPES["Proband-only"])
    other = PermissibleValue(
        text="other",
        title="Other",
        description="Other",
        meaning=NCPI_FAMILY_TYPES["Other"])

    _defn = EnumDefinition(
        name="EnumFamilyType",
        description="Describes the 'type' of study family, eg, trio.",
    )

class EnumConsanguinity(EnumDefinitionImpl):
    """
    List of codes indicates the level of known consanguinity (blood relation) within a study family.
    """
    not_suspected = PermissibleValue(
        text="not_suspected",
        title="Not suspected",
        description="Not suspected",
        meaning=SCT["428263003"])
    suspected = PermissibleValue(
        text="suspected",
        title="Suspected",
        description="Suspected",
        meaning=SCT["415684004"])
    known_present = PermissibleValue(
        text="known_present",
        title="Known present",
        description="Known present",
        meaning=SCT["410515003"])
    unknown = PermissibleValue(
        text="unknown",
        title="Unknown",
        description="Unknown",
        meaning=SCT["261665006"])

    _defn = EnumDefinition(
        name="EnumConsanguinity",
        description="List of codes indicates the level of known consanguinity (blood relation) within a study family.",
    )

class EnumFileMetaDataType(EnumDefinitionImpl):
    """
    Identify the type of profile to use
    """
    bam_cram = PermissibleValue(
        text="bam_cram",
        title="BAM/CRAM",
        description="Bam or Cram file")
    fastq = PermissibleValue(
        text="fastq",
        title="FASTQ",
        description="FASTQ File")
    maf = PermissibleValue(
        text="maf",
        title="MAF (Somatic Mutation) file",
        description="MAF (Somatic Mutation)")
    proteomics = PermissibleValue(
        text="proteomics",
        title="Proteomics file",
        description="Proteomics file")
    vcf = PermissibleValue(
        text="vcf",
        title="VCF (and gVCF) file",
        description="GC or gVCF file")

    _defn = EnumDefinition(
        name="EnumFileMetaDataType",
        description="Identify the type of profile to use",
    )

# Slots
class slots:
    pass

slots.id = Slot(uri=KFI_FHIR_SPARKS.id, name="id", curie=KFI_FHIR_SPARKS.curie('id'),
                   model_uri=KFI_FHIR_SPARKS.id, domain=None, range=URIRef)

slots.external_id = Slot(uri=KFI_FHIR_SPARKS.external_id, name="external_id", curie=KFI_FHIR_SPARKS.curie('external_id'),
                   model_uri=KFI_FHIR_SPARKS.external_id, domain=None, range=Optional[Union[Union[str, URIorCURIE], list[Union[str, URIorCURIE]]]])

slots.name = Slot(uri=KFI_FHIR_SPARKS.name, name="name", curie=KFI_FHIR_SPARKS.curie('name'),
                   model_uri=KFI_FHIR_SPARKS.name, domain=None, range=Optional[str])

slots.description = Slot(uri=KFI_FHIR_SPARKS.description, name="description", curie=KFI_FHIR_SPARKS.curie('description'),
                   model_uri=KFI_FHIR_SPARKS.description, domain=None, range=Optional[str])

slots.practitioner_role_id = Slot(uri=KFI_FHIR_SPARKS.practitioner_role_id, name="practitioner_role_id", curie=KFI_FHIR_SPARKS.curie('practitioner_role_id'),
                   model_uri=KFI_FHIR_SPARKS.practitioner_role_id, domain=None, range=Optional[Union[str, PractitionerRolePractitionerRoleId]])

slots.research_study_id = Slot(uri=KFI_FHIR_SPARKS.research_study_id, name="research_study_id", curie=KFI_FHIR_SPARKS.curie('research_study_id'),
                   model_uri=KFI_FHIR_SPARKS.research_study_id, domain=None, range=URIRef)

slots.website = Slot(uri=KFI_FHIR_SPARKS.website, name="website", curie=KFI_FHIR_SPARKS.curie('website'),
                   model_uri=KFI_FHIR_SPARKS.website, domain=None, range=Optional[Union[str, URI]])

slots.label = Slot(uri=KFI_FHIR_SPARKS.label, name="label", curie=KFI_FHIR_SPARKS.curie('label'),
                   model_uri=KFI_FHIR_SPARKS.label, domain=None, range=Optional[Union[str, list[str]]])

slots.access_policy_id = Slot(uri=KFI['access-policy/access_policy_id'], name="access_policy_id", curie=KFI.curie('access-policy/access_policy_id'),
                   model_uri=KFI_FHIR_SPARKS.access_policy_id, domain=None, range=Union[str, AccessPolicyAccessPolicyId])

slots.disease_limitation = Slot(uri=KFI['access-policy/disease_limitation'], name="disease_limitation", curie=KFI.curie('access-policy/disease_limitation'),
                   model_uri=KFI_FHIR_SPARKS.disease_limitation, domain=None, range=Optional[str])

slots.access_policy_code = Slot(uri=KFI['access-policy/access_policy_code'], name="access_policy_code", curie=KFI.curie('access-policy/access_policy_code'),
                   model_uri=KFI_FHIR_SPARKS.access_policy_code, domain=None, range=Union[Union[str, "EnumAccessPolicyCode"], list[Union[str, "EnumAccessPolicyCode"]]])

slots.data_access_type = Slot(uri=KFI['access-policy/data_access_type'], name="data_access_type", curie=KFI.curie('access-policy/data_access_type'),
                   model_uri=KFI_FHIR_SPARKS.data_access_type, domain=None, range=Union[str, "EnumDataAccessType"])

slots.consent_scope = Slot(uri=KFI['access-policy/consent_scope'], name="consent_scope", curie=KFI.curie('access-policy/consent_scope'),
                   model_uri=KFI_FHIR_SPARKS.consent_scope, domain=None, range=Union[str, "EnumConsentScope"])

slots.offset = Slot(uri=KFI['relative-date-time/offset'], name="offset", curie=KFI.curie('relative-date-time/offset'),
                   model_uri=KFI_FHIR_SPARKS.offset, domain=None, range=int)

slots.offset_end = Slot(uri=KFI['relative-date-time/offset_end'], name="offset_end", curie=KFI.curie('relative-date-time/offset_end'),
                   model_uri=KFI_FHIR_SPARKS.offset_end, domain=None, range=Optional[int])

slots.offset_type = Slot(uri=KFI['relative-date-time/offset_type'], name="offset_type", curie=KFI.curie('relative-date-time/offset_type'),
                   model_uri=KFI_FHIR_SPARKS.offset_type, domain=None, range=Union[str, "EnumOffsetType"])

slots.age_at_event = Slot(uri=KFI['participant-assertion/age_at_event'], name="age_at_event", curie=KFI.curie('participant-assertion/age_at_event'),
                   model_uri=KFI_FHIR_SPARKS.age_at_event, domain=None, range=Optional[Union[str, AgeAtId]])

slots.age_at_assertion = Slot(uri=KFI['participant-assertion/age_at_assertion'], name="age_at_assertion", curie=KFI.curie('participant-assertion/age_at_assertion'),
                   model_uri=KFI_FHIR_SPARKS.age_at_assertion, domain=None, range=Optional[Union[str, AgeAtId]])

slots.age_at_onset = Slot(uri=KFI['participant-assertion/age_at_onset'], name="age_at_onset", curie=KFI.curie('participant-assertion/age_at_onset'),
                   model_uri=KFI_FHIR_SPARKS.age_at_onset, domain=None, range=Optional[Union[str, AgeAtId]])

slots.age_at_resolution = Slot(uri=KFI['participant-assertion/age_at_resolution'], name="age_at_resolution", curie=KFI.curie('participant-assertion/age_at_resolution'),
                   model_uri=KFI_FHIR_SPARKS.age_at_resolution, domain=None, range=Optional[Union[str, AgeAtId]])

slots.entity_asserter = Slot(uri=KFI['participant-assertion/entity_asserter'], name="entity_asserter", curie=KFI.curie('participant-assertion/entity_asserter'),
                   model_uri=KFI_FHIR_SPARKS.entity_asserter, domain=None, range=Optional[Union[str, "EnumEntityAsserter"]])

slots.other_condition_modifiers = Slot(uri=KFI['participant-assertion/other_condition_modifiers'], name="other_condition_modifiers", curie=KFI.curie('participant-assertion/other_condition_modifiers'),
                   model_uri=KFI_FHIR_SPARKS.other_condition_modifiers, domain=None, range=Optional[Union[str, URIorCURIE]])

slots.assertion_type = Slot(uri=KFI['participant-assertion/assertion_type'], name="assertion_type", curie=KFI.curie('participant-assertion/assertion_type'),
                   model_uri=KFI_FHIR_SPARKS.assertion_type, domain=None, range=Union[str, "EnumAssertionType"])

slots.assertion_code = Slot(uri=KFI['participant-assertion/assertion_code'], name="assertion_code", curie=KFI.curie('participant-assertion/assertion_code'),
                   model_uri=KFI_FHIR_SPARKS.assertion_code, domain=None, range=Union[str, URIorCURIE])

slots.assertion_text = Slot(uri=KFI['participant-assertion/assertion_text'], name="assertion_text", curie=KFI.curie('participant-assertion/assertion_text'),
                   model_uri=KFI_FHIR_SPARKS.assertion_text, domain=None, range=Optional[str])

slots.assertion_source = Slot(uri=KFI['participant-assertion/assertion_source'], name="assertion_source", curie=KFI.curie('participant-assertion/assertion_source'),
                   model_uri=KFI_FHIR_SPARKS.assertion_source, domain=None, range=Optional[Union[str, URIorCURIE]])

slots.value_code = Slot(uri=KFI['participant-assertion/value_code'], name="value_code", curie=KFI.curie('participant-assertion/value_code'),
                   model_uri=KFI_FHIR_SPARKS.value_code, domain=None, range=Optional[Union[str, URIorCURIE]])

slots.value_string = Slot(uri=KFI['participant-assertion/value_string'], name="value_string", curie=KFI.curie('participant-assertion/value_string'),
                   model_uri=KFI_FHIR_SPARKS.value_string, domain=None, range=Optional[str])

slots.value_number = Slot(uri=KFI['participant-assertion/value_number'], name="value_number", curie=KFI.curie('participant-assertion/value_number'),
                   model_uri=KFI_FHIR_SPARKS.value_number, domain=None, range=Optional[float])

slots.value_units = Slot(uri=KFI['participant-assertion/value_units'], name="value_units", curie=KFI.curie('participant-assertion/value_units'),
                   model_uri=KFI_FHIR_SPARKS.value_units, domain=None, range=Optional[Union[str, URIorCURIE]])

slots.body_site = Slot(uri=KFI['participant-assertion/body_site'], name="body_site", curie=KFI.curie('participant-assertion/body_site'),
                   model_uri=KFI_FHIR_SPARKS.body_site, domain=None, range=Optional[Union[str, URIorCURIE]])

slots.body_location = Slot(uri=KFI['participant-assertion/body_location'], name="body_location", curie=KFI.curie('participant-assertion/body_location'),
                   model_uri=KFI_FHIR_SPARKS.body_location, domain=None, range=Optional[Union[str, URIorCURIE]])

slots.body_laterality = Slot(uri=KFI['participant-assertion/body_laterality'], name="body_laterality", curie=KFI.curie('participant-assertion/body_laterality'),
                   model_uri=KFI_FHIR_SPARKS.body_laterality, domain=None, range=Optional[Union[str, URIorCURIE]])

slots.cancer_stage = Slot(uri=KFI['participant-assertion/cancer_stage'], name="cancer_stage", curie=KFI.curie('participant-assertion/cancer_stage'),
                   model_uri=KFI_FHIR_SPARKS.cancer_stage, domain=None, range=Optional[Union[str, URIorCURIE]])

slots.email = Slot(uri=KFI['practitioner/email'], name="email", curie=KFI.curie('practitioner/email'),
                   model_uri=KFI_FHIR_SPARKS.email, domain=None, range=Optional[str])

slots.practitioner_title = Slot(uri=KFI['practitioner/practitioner_title'], name="practitioner_title", curie=KFI.curie('practitioner/practitioner_title'),
                   model_uri=KFI_FHIR_SPARKS.practitioner_title, domain=None, range=Optional[str])

slots.practitioner_id = Slot(uri=KFI['practitioner/practitioner_id'], name="practitioner_id", curie=KFI.curie('practitioner/practitioner_id'),
                   model_uri=KFI_FHIR_SPARKS.practitioner_id, domain=None, range=Optional[str])

slots.role = Slot(uri=KFI['associated_party/role'], name="role", curie=KFI.curie('associated_party/role'),
                   model_uri=KFI_FHIR_SPARKS.role, domain=None, range=Optional[Union[str, "EnumResearchStudyPartyRole"]])

slots.classifier = Slot(uri=KFI['associated_party/classifier'], name="classifier", curie=KFI.curie('associated_party/classifier'),
                   model_uri=KFI_FHIR_SPARKS.classifier, domain=None, range=Optional[Union[Union[str, "EnumResearchStudyPartyOrganizationType"], list[Union[str, "EnumResearchStudyPartyOrganizationType"]]]])

slots.associated_party_practitioner_id = Slot(uri=KFI['associated_party/associated_party_practitioner_id'], name="associated_party_practitioner_id", curie=KFI.curie('associated_party/associated_party_practitioner_id'),
                   model_uri=KFI_FHIR_SPARKS.associated_party_practitioner_id, domain=None, range=Optional[Union[str, PractitionerPractitionerId]])

slots.associated_party_practitioner_role_id = Slot(uri=KFI['associated_party/associated_party_practitioner_role_id'], name="associated_party_practitioner_role_id", curie=KFI.curie('associated_party/associated_party_practitioner_role_id'),
                   model_uri=KFI_FHIR_SPARKS.associated_party_practitioner_role_id, domain=None, range=Optional[Union[str, PractitionerRolePractitionerRoleId]])

slots.associated_party_institution_id = Slot(uri=KFI['associated_party/associated_party_institution_id'], name="associated_party_institution_id", curie=KFI.curie('associated_party/associated_party_institution_id'),
                   model_uri=KFI_FHIR_SPARKS.associated_party_institution_id, domain=None, range=Optional[Union[str, PractitionerRolePractitionerRoleId]])

slots.party = Slot(uri=KFI['associated_party/party'], name="party", curie=KFI.curie('associated_party/party'),
                   model_uri=KFI_FHIR_SPARKS.party, domain=None, range=Optional[Union[dict, Any]])

slots.institution_id = Slot(uri=KFI['institution/institution_id'], name="institution_id", curie=KFI.curie('institution/institution_id'),
                   model_uri=KFI_FHIR_SPARKS.institution_id, domain=None, range=Optional[Union[str, InstitutionInstitutionId]])

slots.participant_id = Slot(uri=KFI['participant/participant_id'], name="participant_id", curie=KFI.curie('participant/participant_id'),
                   model_uri=KFI_FHIR_SPARKS.participant_id, domain=None, range=Union[str, ParticipantParticipantId])

slots.birthsex = Slot(uri=KFI['participant/birthsex'], name="birthsex", curie=KFI.curie('participant/birthsex'),
                   model_uri=KFI_FHIR_SPARKS.birthsex, domain=None, range=Optional[Union[str, "EnumBirthSex"]])

slots.race = Slot(uri=KFI['participant/race'], name="race", curie=KFI.curie('participant/race'),
                   model_uri=KFI_FHIR_SPARKS.race, domain=None, range=Union[Union[str, "EnumRace"], list[Union[str, "EnumRace"]]])

slots.ethnicity = Slot(uri=KFI['participant/ethnicity'], name="ethnicity", curie=KFI.curie('participant/ethnicity'),
                   model_uri=KFI_FHIR_SPARKS.ethnicity, domain=None, range=Union[str, "EnumEthnicity"])

slots.population = Slot(uri=KFI['participant/population'], name="population", curie=KFI.curie('participant/population'),
                   model_uri=KFI_FHIR_SPARKS.population, domain=None, range=Optional[Union[str, "EnumPopulation"]])

slots.dob = Slot(uri=KFI['participant/dob'], name="dob", curie=KFI.curie('participant/dob'),
                   model_uri=KFI_FHIR_SPARKS.dob, domain=None, range=Optional[str])

slots.dob_method = Slot(uri=KFI['participant/dob_method'], name="dob_method", curie=KFI.curie('participant/dob_method'),
                   model_uri=KFI_FHIR_SPARKS.dob_method, domain=None, range=Optional[Union[str, "EnumDobMethod"]])

slots.age_at_last_vital = Slot(uri=KFI['participant/age_at_last_vital'], name="age_at_last_vital", curie=KFI.curie('participant/age_at_last_vital'),
                   model_uri=KFI_FHIR_SPARKS.age_at_last_vital, domain=None, range=Optional[str])

slots.is_deceased = Slot(uri=KFI['participant/is_deceased'], name="is_deceased", curie=KFI.curie('participant/is_deceased'),
                   model_uri=KFI_FHIR_SPARKS.is_deceased, domain=None, range=Optional[Union[bool, Bool]])

slots.deceased_rel = Slot(uri=KFI['participant/deceased_rel'], name="deceased_rel", curie=KFI.curie('participant/deceased_rel'),
                   model_uri=KFI_FHIR_SPARKS.deceased_rel, domain=None, range=Optional[Union[str, RelativeDateTimeId]])

slots.patient_knowledge_source = Slot(uri=KFI['participant/patient_knowledge_source'], name="patient_knowledge_source", curie=KFI.curie('participant/patient_knowledge_source'),
                   model_uri=KFI_FHIR_SPARKS.patient_knowledge_source, domain=None, range=Optional[Union[str, "EnumPatientKnowledgeSource"]])

slots.family_global_id = Slot(uri=KFI['participant/family_global_id'], name="family_global_id", curie=KFI.curie('participant/family_global_id'),
                   model_uri=KFI_FHIR_SPARKS.family_global_id, domain=None, range=Optional[Union[str, FamilyFamilyGlobalId]])

slots.period_id = Slot(uri=KFI['period/period_id'], name="period_id", curie=KFI.curie('period/period_id'),
                   model_uri=KFI_FHIR_SPARKS.period_id, domain=None, range=Optional[Union[str, PeriodPeriodId]])

slots.study_membership_id = Slot(uri=KFI['study-membership/study_membership_id'], name="study_membership_id", curie=KFI.curie('study-membership/study_membership_id'),
                   model_uri=KFI_FHIR_SPARKS.study_membership_id, domain=None, range=str)

slots.parent_study_id = Slot(uri=KFI['research_study/parent_study_id'], name="parent_study_id", curie=KFI.curie('research_study/parent_study_id'),
                   model_uri=KFI_FHIR_SPARKS.parent_study_id, domain=None, range=Optional[Union[str, ResearchStudyResearchStudyId]])

slots.study_title = Slot(uri=KFI['research_study/study_title'], name="study_title", curie=KFI.curie('research_study/study_title'),
                   model_uri=KFI_FHIR_SPARKS.study_title, domain=None, range=Optional[str])

slots.study_focus = Slot(uri=KFI['research_study/study_focus'], name="study_focus", curie=KFI.curie('research_study/study_focus'),
                   model_uri=KFI_FHIR_SPARKS.study_focus, domain=None, range=Optional[Union[Union[str, URIorCURIE], list[Union[str, URIorCURIE]]]])

slots.study_condition = Slot(uri=KFI['research_study/study_condition'], name="study_condition", curie=KFI.curie('research_study/study_condition'),
                   model_uri=KFI_FHIR_SPARKS.study_condition, domain=None, range=Optional[Union[Union[str, URIorCURIE], list[Union[str, URIorCURIE]]]])

slots.study_acknowledgement = Slot(uri=KFI['research_study/study_acknowledgement'], name="study_acknowledgement", curie=KFI.curie('research_study/study_acknowledgement'),
                   model_uri=KFI_FHIR_SPARKS.study_acknowledgement, domain=None, range=Optional[Union[str, list[str]]])

slots.study_status = Slot(uri=KFI['research_study/study_status'], name="study_status", curie=KFI.curie('research_study/study_status'),
                   model_uri=KFI_FHIR_SPARKS.study_status, domain=None, range=Union[str, "EnumStudyStatus"])

slots.study_design = Slot(uri=KFI['research_study/study_design'], name="study_design", curie=KFI.curie('research_study/study_design'),
                   model_uri=KFI_FHIR_SPARKS.study_design, domain=None, range=Optional[Union[Union[str, URIorCURIE], list[Union[str, URIorCURIE]]]])

slots.study_personnel = Slot(uri=KFI['research_study/study_personnel'], name="study_personnel", curie=KFI.curie('research_study/study_personnel'),
                   model_uri=KFI_FHIR_SPARKS.study_personnel, domain=None, range=Union[Union[str, AssociatedPartyId], list[Union[str, AssociatedPartyId]]])

slots.collection_title = Slot(uri=KFI['research-study-collection/collection_title'], name="collection_title", curie=KFI.curie('research-study-collection/collection_title'),
                   model_uri=KFI_FHIR_SPARKS.collection_title, domain=None, range=str)

slots.research_study_collection_type = Slot(uri=KFI['research-study-collection/research_study_collection_type'], name="research_study_collection_type", curie=KFI.curie('research-study-collection/research_study_collection_type'),
                   model_uri=KFI_FHIR_SPARKS.research_study_collection_type, domain=None, range=Union[str, "EnumResearchCollectionType"])

slots.research_study_collection_id = Slot(uri=KFI['research-study-collection/research_study_collection_id'], name="research_study_collection_id", curie=KFI.curie('research-study-collection/research_study_collection_id'),
                   model_uri=KFI_FHIR_SPARKS.research_study_collection_id, domain=None, range=Optional[str])

slots.research_study_collection_member_id = Slot(uri=KFI['research-study-collection/research_study_collection_member_id'], name="research_study_collection_member_id", curie=KFI.curie('research-study-collection/research_study_collection_member_id'),
                   model_uri=KFI_FHIR_SPARKS.research_study_collection_member_id, domain=None, range=Union[Union[str, ResearchStudyResearchStudyId], list[Union[str, ResearchStudyResearchStudyId]]])

slots.collection_status = Slot(uri=KFI['research-study-collection/collection_status'], name="collection_status", curie=KFI.curie('research-study-collection/collection_status'),
                   model_uri=KFI_FHIR_SPARKS.collection_status, domain=None, range=Union[str, "EnumCollectionStatus"])

slots.aliquot_id = Slot(uri=KFI['sample/aliquot_id'], name="aliquot_id", curie=KFI.curie('sample/aliquot_id'),
                   model_uri=KFI_FHIR_SPARKS.aliquot_id, domain=None, range=Optional[Union[str, AliquotAliquotId]])

slots.sample_id = Slot(uri=KFI['sample/sample_id'], name="sample_id", curie=KFI.curie('sample/sample_id'),
                   model_uri=KFI_FHIR_SPARKS.sample_id, domain=None, range=Optional[Union[str, SampleSampleId]])

slots.parent_sample_id = Slot(uri=KFI['sample/parent_sample_id'], name="parent_sample_id", curie=KFI.curie('sample/parent_sample_id'),
                   model_uri=KFI_FHIR_SPARKS.parent_sample_id, domain=None, range=Optional[Union[str, SampleSampleId]])

slots.sample_type = Slot(uri=KFI['sample/sample_type'], name="sample_type", curie=KFI.curie('sample/sample_type'),
                   model_uri=KFI_FHIR_SPARKS.sample_type, domain=None, range=Union[str, URIorCURIE])

slots.age_at_collection = Slot(uri=KFI['sample/age_at_collection'], name="age_at_collection", curie=KFI.curie('sample/age_at_collection'),
                   model_uri=KFI_FHIR_SPARKS.age_at_collection, domain=None, range=Optional[Union[str, AgeAtId]])

slots.collection_method = Slot(uri=KFI['sample/collection_method'], name="collection_method", curie=KFI.curie('sample/collection_method'),
                   model_uri=KFI_FHIR_SPARKS.collection_method, domain=None, range=Optional[Union[str, URIorCURIE]])

slots.collection_site = Slot(uri=KFI['sample/collection_site'], name="collection_site", curie=KFI.curie('sample/collection_site'),
                   model_uri=KFI_FHIR_SPARKS.collection_site, domain=None, range=Optional[Union[str, URIorCURIE]])

slots.spatial_qualifier = Slot(uri=KFI['sample/spatial_qualifier'], name="spatial_qualifier", curie=KFI.curie('sample/spatial_qualifier'),
                   model_uri=KFI_FHIR_SPARKS.spatial_qualifier, domain=None, range=Optional[Union[str, URIorCURIE]])

slots.laterality = Slot(uri=KFI['sample/laterality'], name="laterality", curie=KFI.curie('sample/laterality'),
                   model_uri=KFI_FHIR_SPARKS.laterality, domain=None, range=Optional[Union[str, URIorCURIE]])

slots.processing = Slot(uri=KFI['sample/processing'], name="processing", curie=KFI.curie('sample/processing'),
                   model_uri=KFI_FHIR_SPARKS.processing, domain=None, range=Optional[Union[Union[str, URIorCURIE], list[Union[str, URIorCURIE]]]])

slots.availability_status = Slot(uri=KFI['sample/availability_status'], name="availability_status", curie=KFI.curie('sample/availability_status'),
                   model_uri=KFI_FHIR_SPARKS.availability_status, domain=None, range=Optional[Union[str, "EnumSpecimenAvailability"]])

slots.storage_method = Slot(uri=KFI['sample/storage_method'], name="storage_method", curie=KFI.curie('sample/storage_method'),
                   model_uri=KFI_FHIR_SPARKS.storage_method, domain=None, range=Optional[Union[str, URIorCURIE]])

slots.quantity = Slot(uri=KFI['sample/quantity'], name="quantity", curie=KFI.curie('sample/quantity'),
                   model_uri=KFI_FHIR_SPARKS.quantity, domain=None, range=Optional[float])

slots.quantity_units = Slot(uri=KFI['sample/quantity_units'], name="quantity_units", curie=KFI.curie('sample/quantity_units'),
                   model_uri=KFI_FHIR_SPARKS.quantity_units, domain=None, range=Optional[Union[str, URIorCURIE]])

slots.volume = Slot(uri=KFI['sample/volume'], name="volume", curie=KFI.curie('sample/volume'),
                   model_uri=KFI_FHIR_SPARKS.volume, domain=None, range=Optional[float])

slots.volume_units = Slot(uri=KFI['sample/volume_units'], name="volume_units", curie=KFI.curie('sample/volume_units'),
                   model_uri=KFI_FHIR_SPARKS.volume_units, domain=None, range=Optional[Union[str, URIorCURIE]])

slots.concentration = Slot(uri=KFI['sample/concentration'], name="concentration", curie=KFI.curie('sample/concentration'),
                   model_uri=KFI_FHIR_SPARKS.concentration, domain=None, range=Optional[Union[str, URIorCURIE]])

slots.concentration_units = Slot(uri=KFI['sample/concentration_units'], name="concentration_units", curie=KFI.curie('sample/concentration_units'),
                   model_uri=KFI_FHIR_SPARKS.concentration_units, domain=None, range=Optional[Union[str, URIorCURIE]])

slots.file_format = Slot(uri=KFI['ncpi-file/file_format'], name="file_format", curie=KFI.curie('ncpi-file/file_format'),
                   model_uri=KFI_FHIR_SPARKS.file_format, domain=None, range=Union[str, URIorCURIE])

slots.file_size = Slot(uri=KFI['ncpi-file/file_size'], name="file_size", curie=KFI.curie('ncpi-file/file_size'),
                   model_uri=KFI_FHIR_SPARKS.file_size, domain=None, range=float)

slots.file_size_unit = Slot(uri=KFI['ncpi-file/file_size_unit'], name="file_size_unit", curie=KFI.curie('ncpi-file/file_size_unit'),
                   model_uri=KFI_FHIR_SPARKS.file_size_unit, domain=None, range=Union[str, URIorCURIE])

slots.content_version = Slot(uri=KFI['ncpi-file/content_version'], name="content_version", curie=KFI.curie('ncpi-file/content_version'),
                   model_uri=KFI_FHIR_SPARKS.content_version, domain=None, range=Optional[str])

slots.file_type = Slot(uri=KFI['ncpi-file/file_type'], name="file_type", curie=KFI.curie('ncpi-file/file_type'),
                   model_uri=KFI_FHIR_SPARKS.file_type, domain=None, range=Union[str, URIorCURIE])

slots.file_hash = Slot(uri=KFI['ncpi-file/file_hash'], name="file_hash", curie=KFI.curie('ncpi-file/file_hash'),
                   model_uri=KFI_FHIR_SPARKS.file_hash, domain=None, range=str)

slots.file_hash_type = Slot(uri=KFI['ncpi-file/file_hash_type'], name="file_hash_type", curie=KFI.curie('ncpi-file/file_hash_type'),
                   model_uri=KFI_FHIR_SPARKS.file_hash_type, domain=None, range=Optional[Union[str, URIorCURIE]])

slots.file_location_id = Slot(uri=KFI['file-location/file_location_id'], name="file_location_id", curie=KFI.curie('file-location/file_location_id'),
                   model_uri=KFI_FHIR_SPARKS.file_location_id, domain=None, range=Union[Union[str, FileLocationFileLocationId], list[Union[str, FileLocationFileLocationId]]])

slots.location_uri = Slot(uri=KFI['file-location/location_uri'], name="location_uri", curie=KFI.curie('file-location/location_uri'),
                   model_uri=KFI_FHIR_SPARKS.location_uri, domain=None, range=Union[str, URI])

slots.file_name = Slot(uri=KFI['file-location/file_name'], name="file_name", curie=KFI.curie('file-location/file_name'),
                   model_uri=KFI_FHIR_SPARKS.file_name, domain=None, range=str)

slots.patient_id = Slot(uri=KFI['family-relationship/patient_id'], name="patient_id", curie=KFI.curie('family-relationship/patient_id'),
                   model_uri=KFI_FHIR_SPARKS.patient_id, domain=None, range=Union[str, ParticipantParticipantId])

slots.relative_id = Slot(uri=KFI['family-relationship/relative_id'], name="relative_id", curie=KFI.curie('family-relationship/relative_id'),
                   model_uri=KFI_FHIR_SPARKS.relative_id, domain=None, range=Union[str, ParticipantParticipantId])

slots.relationship = Slot(uri=KFI['family-relationship/relationship'], name="relationship", curie=KFI.curie('family-relationship/relationship'),
                   model_uri=KFI_FHIR_SPARKS.relationship, domain=None, range=Union[str, "EnumFamilyRelationship"])

slots.knowledge_source = Slot(uri=KFI['family-relationship/knowledge_source'], name="knowledge_source", curie=KFI.curie('family-relationship/knowledge_source'),
                   model_uri=KFI_FHIR_SPARKS.knowledge_source, domain=None, range=Union[str, "EnumRelationshipKnowledgeSource"])

slots.family_id = Slot(uri=KFI['family/family_id'], name="family_id", curie=KFI.curie('family/family_id'),
                   model_uri=KFI_FHIR_SPARKS.family_id, domain=None, range=str)

slots.family_type = Slot(uri=KFI['family/family_type'], name="family_type", curie=KFI.curie('family/family_type'),
                   model_uri=KFI_FHIR_SPARKS.family_type, domain=None, range=Union[str, "EnumFamilyType"])

slots.consanguinity = Slot(uri=KFI['family/consanguinity'], name="consanguinity", curie=KFI.curie('family/consanguinity'),
                   model_uri=KFI_FHIR_SPARKS.consanguinity, domain=None, range=Optional[Union[str, "EnumConsanguinity"]])

slots.family_focus = Slot(uri=KFI['family/family_focus'], name="family_focus", curie=KFI.curie('family/family_focus'),
                   model_uri=KFI_FHIR_SPARKS.family_focus, domain=None, range=Optional[Union[str, URIorCURIE]])

slots.file_meta_data_id = Slot(uri=KFI['file-meta-data/file_meta_data_id'], name="file_meta_data_id", curie=KFI.curie('file-meta-data/file_meta_data_id'),
                   model_uri=KFI_FHIR_SPARKS.file_meta_data_id, domain=None, range=Optional[Union[Union[str, FileMetaDataFileMetaDataId], list[Union[str, FileMetaDataFileMetaDataId]]]])

slots.meta_data_type = Slot(uri=KFI['file-meta-data/meta_data_type'], name="meta_data_type", curie=KFI.curie('file-meta-data/meta_data_type'),
                   model_uri=KFI_FHIR_SPARKS.meta_data_type, domain=None, range=Union[str, "EnumFileMetaDataType"])

slots.assay_strategy = Slot(uri=KFI['file-meta-data/assay_strategy'], name="assay_strategy", curie=KFI.curie('file-meta-data/assay_strategy'),
                   model_uri=KFI_FHIR_SPARKS.assay_strategy, domain=None, range=Union[str, URIorCURIE])

slots.platform_instrument = Slot(uri=KFI['file-meta-data/platform_instrument'], name="platform_instrument", curie=KFI.curie('file-meta-data/platform_instrument'),
                   model_uri=KFI_FHIR_SPARKS.platform_instrument, domain=None, range=Union[str, URIorCURIE])

slots.library_prep = Slot(uri=KFI['file-meta-data/library_prep'], name="library_prep", curie=KFI.curie('file-meta-data/library_prep'),
                   model_uri=KFI_FHIR_SPARKS.library_prep, domain=None, range=Optional[Union[str, URIorCURIE]])

slots.library_selection = Slot(uri=KFI['file-meta-data/library_selection'], name="library_selection", curie=KFI.curie('file-meta-data/library_selection'),
                   model_uri=KFI_FHIR_SPARKS.library_selection, domain=None, range=Optional[Union[str, URIorCURIE]])

slots.strandedness = Slot(uri=KFI['file-meta-data/strandedness'], name="strandedness", curie=KFI.curie('file-meta-data/strandedness'),
                   model_uri=KFI_FHIR_SPARKS.strandedness, domain=None, range=Optional[Union[str, URIorCURIE]])

slots.target_region = Slot(uri=KFI['file-meta-data/target_region'], name="target_region", curie=KFI.curie('file-meta-data/target_region'),
                   model_uri=KFI_FHIR_SPARKS.target_region, domain=None, range=Optional[Union[str, URIorCURIE]])

slots.is_paired_end = Slot(uri=KFI['file-meta-data/is_paired_end'], name="is_paired_end", curie=KFI.curie('file-meta-data/is_paired_end'),
                   model_uri=KFI_FHIR_SPARKS.is_paired_end, domain=None, range=Optional[Union[str, URIorCURIE]])

slots.adaptor_trimmed = Slot(uri=KFI['file-meta-data/adaptor_trimmed'], name="adaptor_trimmed", curie=KFI.curie('file-meta-data/adaptor_trimmed'),
                   model_uri=KFI_FHIR_SPARKS.adaptor_trimmed, domain=None, range=Optional[Union[str, URIorCURIE]])

slots.reference_genome = Slot(uri=KFI['file-meta-data/reference_genome'], name="reference_genome", curie=KFI.curie('file-meta-data/reference_genome'),
                   model_uri=KFI_FHIR_SPARKS.reference_genome, domain=None, range=Optional[Union[str, URIorCURIE]])

slots.workflow_type = Slot(uri=KFI['file-meta-data/workflow_type'], name="workflow_type", curie=KFI.curie('file-meta-data/workflow_type'),
                   model_uri=KFI_FHIR_SPARKS.workflow_type, domain=None, range=Optional[Union[str, URIorCURIE]])

slots.workflow_tool = Slot(uri=KFI['file-meta-data/workflow_tool'], name="workflow_tool", curie=KFI.curie('file-meta-data/workflow_tool'),
                   model_uri=KFI_FHIR_SPARKS.workflow_tool, domain=None, range=Optional[Union[str, URIorCURIE]])

slots.related_samples = Slot(uri=KFI['file-meta-data/related_samples'], name="related_samples", curie=KFI.curie('file-meta-data/related_samples'),
                   model_uri=KFI_FHIR_SPARKS.related_samples, domain=None, range=Optional[Union[str, SampleSampleId]])

slots.accessPolicy__status = Slot(uri=KFI['access-policy/status'], name="accessPolicy__status", curie=KFI.curie('access-policy/status'),
                   model_uri=KFI_FHIR_SPARKS.accessPolicy__status, domain=None, range=Union[str, "EnumConsentStateCodes"])

slots.ageAt__value_type = Slot(uri=KFI['age-at/value_type'], name="ageAt__value_type", curie=KFI.curie('age-at/value_type'),
                   model_uri=KFI_FHIR_SPARKS.ageAt__value_type, domain=None, range=Union[str, "EnumAgeValueType"])

slots.ageAt__age = Slot(uri=KFI['age-at/age'], name="ageAt__age", curie=KFI.curie('age-at/age'),
                   model_uri=KFI_FHIR_SPARKS.ageAt__age, domain=None, range=Optional[Union[str, RelativeDateTimeId]])

slots.ageAt__age_code = Slot(uri=KFI['age-at/age_code'], name="ageAt__age_code", curie=KFI.curie('age-at/age_code'),
                   model_uri=KFI_FHIR_SPARKS.ageAt__age_code, domain=None, range=Optional[Union[str, URIorCURIE]])

slots.ageAt__as_date = Slot(uri=KFI['age-at/as_date'], name="ageAt__as_date", curie=KFI.curie('age-at/as_date'),
                   model_uri=KFI_FHIR_SPARKS.ageAt__as_date, domain=None, range=Optional[Union[str, XSDDate]])

slots.participantAssertion__participant_assertion_id = Slot(uri=KFI['participant-assertion/participant_assertion_id'], name="participantAssertion__participant_assertion_id", curie=KFI.curie('participant-assertion/participant_assertion_id'),
                   model_uri=KFI_FHIR_SPARKS.participantAssertion__participant_assertion_id, domain=None, range=URIRef)

slots.practitioner__practitioner_id = Slot(uri=KFI['practitioner/practitioner_id'], name="practitioner__practitioner_id", curie=KFI.curie('practitioner/practitioner_id'),
                   model_uri=KFI_FHIR_SPARKS.practitioner__practitioner_id, domain=None, range=URIRef)

slots.institution__institution_id = Slot(uri=KFI['institution/institution_id'], name="institution__institution_id", curie=KFI.curie('institution/institution_id'),
                   model_uri=KFI_FHIR_SPARKS.institution__institution_id, domain=None, range=URIRef)

slots.person__person_id = Slot(uri=KFI['person/person_id'], name="person__person_id", curie=KFI.curie('person/person_id'),
                   model_uri=KFI_FHIR_SPARKS.person__person_id, domain=None, range=URIRef)

slots.person__participant_id = Slot(uri=KFI['person/participant_id'], name="person__participant_id", curie=KFI.curie('person/participant_id'),
                   model_uri=KFI_FHIR_SPARKS.person__participant_id, domain=None, range=Union[Union[str, ParticipantParticipantId], list[Union[str, ParticipantParticipantId]]])

slots.period__start = Slot(uri=KFI['period/start'], name="period__start", curie=KFI.curie('period/start'),
                   model_uri=KFI_FHIR_SPARKS.period__start, domain=None, range=Optional[Union[str, XSDDate]])

slots.period__end = Slot(uri=KFI['period/end'], name="period__end", curie=KFI.curie('period/end'),
                   model_uri=KFI_FHIR_SPARKS.period__end, domain=None, range=Optional[Union[str, XSDDate]])

slots.practitionerRole__practitioner_role_id = Slot(uri=KFI['practitioner_role/practitioner_role_id'], name="practitionerRole__practitioner_role_id", curie=KFI.curie('practitioner_role/practitioner_role_id'),
                   model_uri=KFI_FHIR_SPARKS.practitionerRole__practitioner_role_id, domain=None, range=URIRef)

slots.researchStudy__research_study_id = Slot(uri=KFI['research_study/research_study_id'], name="researchStudy__research_study_id", curie=KFI.curie('research_study/research_study_id'),
                   model_uri=KFI_FHIR_SPARKS.researchStudy__research_study_id, domain=None, range=URIRef)

slots.researchStudyCollection__research_study_collection_id = Slot(uri=KFI['research-study-collection/research_study_collection_id'], name="researchStudyCollection__research_study_collection_id", curie=KFI.curie('research-study-collection/research_study_collection_id'),
                   model_uri=KFI_FHIR_SPARKS.researchStudyCollection__research_study_collection_id, domain=None, range=URIRef)

slots.researchStudyCollection__description = Slot(uri=KFI['research-study-collection/description'], name="researchStudyCollection__description", curie=KFI.curie('research-study-collection/description'),
                   model_uri=KFI_FHIR_SPARKS.researchStudyCollection__description, domain=None, range=Optional[str])

slots.nCPIFile__file_global_id = Slot(uri=KFI['ncpi-file/file_global_id'], name="nCPIFile__file_global_id", curie=KFI.curie('ncpi-file/file_global_id'),
                   model_uri=KFI_FHIR_SPARKS.nCPIFile__file_global_id, domain=None, range=URIRef)

slots.familyRelationship__family_relationship_global_id = Slot(uri=KFI['family-relationship/family_relationship_global_id'], name="familyRelationship__family_relationship_global_id", curie=KFI.curie('family-relationship/family_relationship_global_id'),
                   model_uri=KFI_FHIR_SPARKS.familyRelationship__family_relationship_global_id, domain=None, range=URIRef)

slots.family__family_global_id = Slot(uri=KFI['family/family_global_id'], name="family__family_global_id", curie=KFI.curie('family/family_global_id'),
                   model_uri=KFI_FHIR_SPARKS.family__family_global_id, domain=None, range=URIRef)

slots.AccessPolicy_access_policy_id = Slot(uri=KFI['access-policy/access_policy_id'], name="AccessPolicy_access_policy_id", curie=KFI.curie('access-policy/access_policy_id'),
                   model_uri=KFI_FHIR_SPARKS.AccessPolicy_access_policy_id, domain=AccessPolicy, range=Union[str, AccessPolicyAccessPolicyId])

slots.ParticipantAssertion_participant_id = Slot(uri=KFI['participant/participant_id'], name="ParticipantAssertion_participant_id", curie=KFI.curie('participant/participant_id'),
                   model_uri=KFI_FHIR_SPARKS.ParticipantAssertion_participant_id, domain=ParticipantAssertion, range=Union[str, ParticipantParticipantId])

slots.AssociatedParty_period_id = Slot(uri=KFI['period/period_id'], name="AssociatedParty_period_id", curie=KFI.curie('period/period_id'),
                   model_uri=KFI_FHIR_SPARKS.AssociatedParty_period_id, domain=AssociatedParty, range=Optional[Union[Union[str, PeriodPeriodId], list[Union[str, PeriodPeriodId]]]])

slots.Participant_participant_id = Slot(uri=KFI['participant/participant_id'], name="Participant_participant_id", curie=KFI.curie('participant/participant_id'),
                   model_uri=KFI_FHIR_SPARKS.Participant_participant_id, domain=Participant, range=Union[str, ParticipantParticipantId])

slots.Participant_sample_id = Slot(uri=KFI['sample/sample_id'], name="Participant_sample_id", curie=KFI.curie('sample/sample_id'),
                   model_uri=KFI_FHIR_SPARKS.Participant_sample_id, domain=Participant, range=Optional[Union[Union[str, SampleSampleId], list[Union[str, SampleSampleId]]]])

slots.Period_period_id = Slot(uri=KFI['period/period_id'], name="Period_period_id", curie=KFI.curie('period/period_id'),
                   model_uri=KFI_FHIR_SPARKS.Period_period_id, domain=Period, range=Union[str, PeriodPeriodId])

slots.StudyMembership_participant_id = Slot(uri=KFI['participant/participant_id'], name="StudyMembership_participant_id", curie=KFI.curie('participant/participant_id'),
                   model_uri=KFI_FHIR_SPARKS.StudyMembership_participant_id, domain=StudyMembership, range=Union[Union[str, ParticipantParticipantId], list[Union[str, ParticipantParticipantId]]])

slots.StudyMembership_study_membership_id = Slot(uri=KFI['study-membership/study_membership_id'], name="StudyMembership_study_membership_id", curie=KFI.curie('study-membership/study_membership_id'),
                   model_uri=KFI_FHIR_SPARKS.StudyMembership_study_membership_id, domain=StudyMembership, range=Union[str, StudyMembershipStudyMembershipId])

slots.ResearchStudy_study_membership_id = Slot(uri=KFI['study-membership/study_membership_id'], name="ResearchStudy_study_membership_id", curie=KFI.curie('study-membership/study_membership_id'),
                   model_uri=KFI_FHIR_SPARKS.ResearchStudy_study_membership_id, domain=ResearchStudy, range=Union[str, list[str]])

slots.Sample_sample_id = Slot(uri=KFI['sample/sample_id'], name="Sample_sample_id", curie=KFI.curie('sample/sample_id'),
                   model_uri=KFI_FHIR_SPARKS.Sample_sample_id, domain=Sample, range=Union[str, SampleSampleId])

slots.Aliquot_aliquot_id = Slot(uri=KFI['sample/aliquot_id'], name="Aliquot_aliquot_id", curie=KFI.curie('sample/aliquot_id'),
                   model_uri=KFI_FHIR_SPARKS.Aliquot_aliquot_id, domain=Aliquot, range=Union[str, AliquotAliquotId])

slots.Aliquot_sample_id = Slot(uri=KFI['sample/sample_id'], name="Aliquot_sample_id", curie=KFI.curie('sample/sample_id'),
                   model_uri=KFI_FHIR_SPARKS.Aliquot_sample_id, domain=Aliquot, range=Union[str, SampleSampleId])

slots.FileLocation_file_location_id = Slot(uri=KFI['file-location/file_location_id'], name="FileLocation_file_location_id", curie=KFI.curie('file-location/file_location_id'),
                   model_uri=KFI_FHIR_SPARKS.FileLocation_file_location_id, domain=FileLocation, range=Union[Union[str, FileLocationFileLocationId], list[Union[str, FileLocationFileLocationId]]])

slots.FileMetaData_file_meta_data_id = Slot(uri=KFI['file-meta-data/file_meta_data_id'], name="FileMetaData_file_meta_data_id", curie=KFI.curie('file-meta-data/file_meta_data_id'),
                   model_uri=KFI_FHIR_SPARKS.FileMetaData_file_meta_data_id, domain=FileMetaData, range=Union[Union[str, FileMetaDataFileMetaDataId], list[Union[str, FileMetaDataFileMetaDataId]]])
