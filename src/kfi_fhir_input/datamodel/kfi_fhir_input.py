# Auto generated from kfi_fhir_input.yaml by pythongen.py version: 0.0.1
# Generation date: 2025-11-20T15:41:22
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

from linkml_runtime.linkml_model.types import String, Uriorcurie
from linkml_runtime.utils.metamodelcore import URIorCURIE

metamodel_version = "1.7.0"
version = None

# Namespaces
PATO = CurieNamespace('PATO', 'http://purl.obolibrary.org/obo/PATO_')
BIOLINK = CurieNamespace('biolink', 'https://w3id.org/biolink/vocab/')
EXAMPLE = CurieNamespace('example', 'http://www.example.org/rdf#')
HL7_RSP_ROLE = CurieNamespace('hl7_rsp_role', 'http://hl7.org/fhir/research-study-party-role')
KFI_FHIR_SPARKS = CurieNamespace('kfi_fhir_sparks', 'https://carrollaboratory.github.io/kif-fhir-input')
LINKML = CurieNamespace('linkml', 'https://w3id.org/linkml/')
SCHEMA = CurieNamespace('schema', 'http://schema.org/')
DEFAULT_ = KFI_FHIR_SPARKS


# Types

# Class references
class RecordId(extended_str):
    pass


class PractitionerId(RecordId):
    pass


class InstitutionId(RecordId):
    pass


@dataclass(repr=False)
class Record(YAMLRoot):
    """
    One row / entity within the database
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = KFI_FHIR_SPARKS["Record"]
    class_class_curie: ClassVar[str] = "kfi_fhir_sparks:Record"
    class_name: ClassVar[str] = "Record"
    class_model_uri: ClassVar[URIRef] = KFI_FHIR_SPARKS.Record

    id: Union[str, RecordId] = None
    external_id: Optional[Union[Union[str, URIorCURIE], list[Union[str, URIorCURIE]]]] = empty_list()

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, RecordId):
            self.id = RecordId(self.id)

        if not isinstance(self.external_id, list):
            self.external_id = [self.external_id] if self.external_id is not None else []
        self.external_id = [v if isinstance(v, URIorCURIE) else URIorCURIE(v) for v in self.external_id]

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class Practitioner(Record):
    """
    For our purposes, this will be an investigator.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = URIRef("https://carrollaboratory.github.io/kfi-fhir-input/practitioner/Practitioner")
    class_class_curie: ClassVar[str] = None
    class_name: ClassVar[str] = "Practitioner"
    class_model_uri: ClassVar[URIRef] = KFI_FHIR_SPARKS.Practitioner

    id: Union[str, PractitionerId] = None
    name: Optional[str] = None
    email: Optional[str] = None
    institution_id: Optional[Union[str, InstitutionId]] = None
    description: Optional[str] = None
    title: Optional[str] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, PractitionerId):
            self.id = PractitionerId(self.id)

        if self.name is not None and not isinstance(self.name, str):
            self.name = str(self.name)

        if self.email is not None and not isinstance(self.email, str):
            self.email = str(self.email)

        if self.institution_id is not None and not isinstance(self.institution_id, InstitutionId):
            self.institution_id = InstitutionId(self.institution_id)

        if self.description is not None and not isinstance(self.description, str):
            self.description = str(self.description)

        if self.title is not None and not isinstance(self.title, str):
            self.title = str(self.title)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class Institution(Record):
    """
    Institution related to study or research personnel
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = URIRef("https://carrollaboratory.github.io/kfi-fhir-input/institution/Institution")
    class_class_curie: ClassVar[str] = None
    class_name: ClassVar[str] = "Institution"
    class_model_uri: ClassVar[URIRef] = KFI_FHIR_SPARKS.Institution

    id: Union[str, InstitutionId] = None
    name: Optional[str] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, InstitutionId):
            self.id = InstitutionId(self.id)

        if self.name is not None and not isinstance(self.name, str):
            self.name = str(self.name)

        super().__post_init__(**kwargs)


# Enumerations


# Slots
class slots:
    pass

slots.id = Slot(uri=KFI_FHIR_SPARKS.id, name="id", curie=KFI_FHIR_SPARKS.curie('id'),
                   model_uri=KFI_FHIR_SPARKS.id, domain=None, range=URIRef)

slots.external_id = Slot(uri=KFI_FHIR_SPARKS.external_id, name="external_id", curie=KFI_FHIR_SPARKS.curie('external_id'),
                   model_uri=KFI_FHIR_SPARKS.external_id, domain=None, range=Optional[Union[Union[str, URIorCURIE], list[Union[str, URIorCURIE]]]])

slots.name = Slot(uri=KFI_FHIR_SPARKS.name, name="name", curie=KFI_FHIR_SPARKS.curie('name'),
                   model_uri=KFI_FHIR_SPARKS.name, domain=None, range=Optional[str])

slots.description = Slot(uri="str(uriorcurie)", name="description", curie=None,
                   model_uri=KFI_FHIR_SPARKS.description, domain=None, range=Optional[str])

slots.email = Slot(uri="str(uriorcurie)", name="email", curie=None,
                   model_uri=KFI_FHIR_SPARKS.email, domain=None, range=Optional[str])

slots.institution_id = Slot(uri="str(uriorcurie)", name="institution_id", curie=None,
                   model_uri=KFI_FHIR_SPARKS.institution_id, domain=None, range=Optional[Union[str, InstitutionId]])

slots.title = Slot(uri="str(uriorcurie)", name="title", curie=None,
                   model_uri=KFI_FHIR_SPARKS.title, domain=None, range=Optional[str])
