# Auto generated from kfi_fhir_input.yaml by pythongen.py version: 0.0.1
# Generation date: 2025-11-21T14:15:35
# Schema: kfi-fhir-input
#
# id: https://carrollaboratory.github.io/kif-fhir-input
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

from linkml_runtime.linkml_model.types import Datetime, String, Uriorcurie
from linkml_runtime.utils.metamodelcore import URIorCURIE, XSDDateTime

metamodel_version = "1.7.0"
version = None

# Namespaces
HL7_RSP_ORG_TYPE = CurieNamespace('hl7_rsp_org_type', 'http://hl7.org/fhir/research-study-party-organization-type')
HL7_RSP_ROLE = CurieNamespace('hl7_rsp_role', 'http://hl7.org/fhir/research-study-party-role')
KFI = CurieNamespace('kfi', 'https://carrollaboratory.github.io/kfi-fhir-input/')
KFI_FHIR_SPARKS = CurieNamespace('kfi_fhir_sparks', 'https://carrollaboratory.github.io/kif-fhir-input')
LINKML = CurieNamespace('linkml', 'https://w3id.org/linkml/')
DEFAULT_ = KFI_FHIR_SPARKS


# Types

# Class references
class RecordId(extended_str):
    pass


class PractitionerPractitionerId(extended_str):
    pass


class InstitutionInstitutionId(extended_str):
    pass


class PeriodPeriodId(extended_str):
    pass


class PractitionerRolePractitionerRoleId(extended_str):
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
    title: Optional[str] = None

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

        if self.title is not None and not isinstance(self.title, str):
            self.title = str(self.title)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class AssociatedParty(YAMLRoot):
    """
    Sponsors, collaborators, and other parties affiliated with a research study.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = KFI["associated_party/AssociatedParty"]
    class_class_curie: ClassVar[str] = "kfi:associated_party/AssociatedParty"
    class_name: ClassVar[str] = "AssociatedParty"
    class_model_uri: ClassVar[URIRef] = KFI_FHIR_SPARKS.AssociatedParty

    name: Optional[str] = None
    role: Optional[Union[str, "EnumResearchStudyPartyRole"]] = None
    period_id: Optional[Union[Union[str, PeriodPeriodId], list[Union[str, PeriodPeriodId]]]] = empty_list()
    classifier: Optional[Union[Union[str, "EnumResearchStudyPartyOrganizationType"], list[Union[str, "EnumResearchStudyPartyOrganizationType"]]]] = empty_list()
    party: Optional[Union[dict, Any]] = None

    def __post_init__(self, *_: str, **kwargs: Any):
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
    start: Optional[Union[str, XSDDateTime]] = None
    end: Optional[Union[str, XSDDateTime]] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.period_id):
            self.MissingRequiredField("period_id")
        if not isinstance(self.period_id, PeriodPeriodId):
            self.period_id = PeriodPeriodId(self.period_id)

        if self.start is not None and not isinstance(self.start, XSDDateTime):
            self.start = XSDDateTime(self.start)

        if self.end is not None and not isinstance(self.end, XSDDateTime):
            self.end = XSDDateTime(self.end)

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


# Enumerations
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
        title="fda",
        meaning=HL7_RSP_ORG_TYPE["fda"])

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

# Slots
class slots:
    pass

slots.id = Slot(uri=KFI_FHIR_SPARKS.id, name="id", curie=KFI_FHIR_SPARKS.curie('id'),
                   model_uri=KFI_FHIR_SPARKS.id, domain=None, range=URIRef)

slots.external_id = Slot(uri=KFI_FHIR_SPARKS.external_id, name="external_id", curie=KFI_FHIR_SPARKS.curie('external_id'),
                   model_uri=KFI_FHIR_SPARKS.external_id, domain=None, range=Optional[Union[Union[str, URIorCURIE], list[Union[str, URIorCURIE]]]])

slots.name = Slot(uri=KFI_FHIR_SPARKS.name, name="name", curie=KFI_FHIR_SPARKS.curie('name'),
                   model_uri=KFI_FHIR_SPARKS.name, domain=None, range=Optional[str])

slots.practitioner_role_id = Slot(uri=KFI_FHIR_SPARKS.practitioner_role_id, name="practitioner_role_id", curie=KFI_FHIR_SPARKS.curie('practitioner_role_id'),
                   model_uri=KFI_FHIR_SPARKS.practitioner_role_id, domain=None, range=Optional[Union[str, PractitionerRolePractitionerRoleId]])

slots.description = Slot(uri=KFI['practitioner/description'], name="description", curie=KFI.curie('practitioner/description'),
                   model_uri=KFI_FHIR_SPARKS.description, domain=None, range=Optional[str])

slots.email = Slot(uri=KFI['practitioner/email'], name="email", curie=KFI.curie('practitioner/email'),
                   model_uri=KFI_FHIR_SPARKS.email, domain=None, range=Optional[str])

slots.title = Slot(uri=KFI['practitioner/title'], name="title", curie=KFI.curie('practitioner/title'),
                   model_uri=KFI_FHIR_SPARKS.title, domain=None, range=Optional[str])

slots.practitioner_id = Slot(uri=KFI['practitioner/practitioner_id'], name="practitioner_id", curie=KFI.curie('practitioner/practitioner_id'),
                   model_uri=KFI_FHIR_SPARKS.practitioner_id, domain=None, range=Optional[str])

slots.role = Slot(uri=KFI['associated_party/role'], name="role", curie=KFI.curie('associated_party/role'),
                   model_uri=KFI_FHIR_SPARKS.role, domain=None, range=Optional[Union[str, "EnumResearchStudyPartyRole"]])

slots.classifier = Slot(uri=KFI['associated_party/classifier'], name="classifier", curie=KFI.curie('associated_party/classifier'),
                   model_uri=KFI_FHIR_SPARKS.classifier, domain=None, range=Optional[Union[Union[str, "EnumResearchStudyPartyOrganizationType"], list[Union[str, "EnumResearchStudyPartyOrganizationType"]]]])

slots.party = Slot(uri=KFI['associated_party/party'], name="party", curie=KFI.curie('associated_party/party'),
                   model_uri=KFI_FHIR_SPARKS.party, domain=None, range=Optional[Union[dict, Any]])

slots.institution_id = Slot(uri=KFI['institution/institution_id'], name="institution_id", curie=KFI.curie('institution/institution_id'),
                   model_uri=KFI_FHIR_SPARKS.institution_id, domain=None, range=Optional[Union[str, InstitutionInstitutionId]])

slots.period_id = Slot(uri=KFI['period/period_id'], name="period_id", curie=KFI.curie('period/period_id'),
                   model_uri=KFI_FHIR_SPARKS.period_id, domain=None, range=Optional[Union[str, PeriodPeriodId]])

slots.practitioner__practitioner_id = Slot(uri=KFI['practitioner/practitioner_id'], name="practitioner__practitioner_id", curie=KFI.curie('practitioner/practitioner_id'),
                   model_uri=KFI_FHIR_SPARKS.practitioner__practitioner_id, domain=None, range=URIRef)

slots.institution__institution_id = Slot(uri=KFI['institution/institution_id'], name="institution__institution_id", curie=KFI.curie('institution/institution_id'),
                   model_uri=KFI_FHIR_SPARKS.institution__institution_id, domain=None, range=URIRef)

slots.period__period_id = Slot(uri=KFI['period/period_id'], name="period__period_id", curie=KFI.curie('period/period_id'),
                   model_uri=KFI_FHIR_SPARKS.period__period_id, domain=None, range=URIRef)

slots.period__start = Slot(uri=KFI['period/start'], name="period__start", curie=KFI.curie('period/start'),
                   model_uri=KFI_FHIR_SPARKS.period__start, domain=None, range=Optional[Union[str, XSDDateTime]])

slots.period__end = Slot(uri=KFI['period/end'], name="period__end", curie=KFI.curie('period/end'),
                   model_uri=KFI_FHIR_SPARKS.period__end, domain=None, range=Optional[Union[str, XSDDateTime]])

slots.practitionerRole__practitioner_role_id = Slot(uri=KFI['practitioner_role/practitioner_role_id'], name="practitionerRole__practitioner_role_id", curie=KFI.curie('practitioner_role/practitioner_role_id'),
                   model_uri=KFI_FHIR_SPARKS.practitionerRole__practitioner_role_id, domain=None, range=URIRef)

slots.AssociatedParty_period_id = Slot(uri=KFI['period/period_id'], name="AssociatedParty_period_id", curie=KFI.curie('period/period_id'),
                   model_uri=KFI_FHIR_SPARKS.AssociatedParty_period_id, domain=AssociatedParty, range=Optional[Union[Union[str, PeriodPeriodId], list[Union[str, PeriodPeriodId]]]])
