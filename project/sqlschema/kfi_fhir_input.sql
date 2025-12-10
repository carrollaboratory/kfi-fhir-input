-- # Abstract Class: Any Description: This is a placeholder for the experimental linkml:any behavior for unions
--     * Slot: id
-- # Abstract Class: HasExternalId Description: Has an external ID
--     * Slot: id
-- # Abstract Class: Record Description: One row / entity within the database
--     * Slot: id Description: Unique Identifier for a table entry. This is probably not the Global ID
-- # Class: AccessPolicy Description: Limitations and/or requirements that define how a user may gain access to a particular set of data.
--     * Slot: description Description: More details associated with the given resource
--     * Slot: data_access_type Description: Type of access restrictions on file downloads ( open | registered | controlled )
--     * Slot: website Description: URL describing the entity this represents. This can include a formal website, such as the Entity's website, or to an online document describing the entity.
--     * Slot: consent_scope Description: Which of the four areas this resource covers (extensible)
--     * Slot: disease_limitation Description: Disease Use Limitations
--     * Slot: access_policy_id Description: Access policy communicates the limitations and/or requirements that define how a user may gain access to a particular set of data.
--     * Slot: status Description: Indicates the state of the consent.
-- # Class: Practitioner Description: For our purposes, this will be an investigator.
--     * Slot: name Description: Name of the entity.
--     * Slot: email Description: An email address to reach the entity.
--     * Slot: institution_id Description: The institution this record is associated with.
--     * Slot: practitioner_role_id Description: Global ID for this record
--     * Slot: description Description: More details associated with the given resource
--     * Slot: practitioner_title Description: The title of the Investigator, eg, "Assistant Professor"
--     * Slot: practitioner_id Description: The Global ID for the Practitioner.
-- # Class: AssociatedParty Description: Sponsors, collaborators, and other parties affiliated with a research study.
--     * Slot: name Description: Name of the entity.
--     * Slot: role Description: Research Study Party Role
--     * Slot: period_id Description: Reference to a time period which defines a Start and End datatime period.
--     * Slot: id Description: Unique Identifier for a table entry. This is probably not the Global ID
--     * Slot: party_id Description: Individual or organization associated with study
-- # Class: Institution Description: Institution related to study or research personnel
--     * Slot: name Description: Name of the entity.
--     * Slot: institution_id Description: Global ID for this record
-- # Class: Participant Description: Research oriented patient
--     * Slot: birthsex Description: Sex assigned at birth (or pre-natal observed sex)
--     * Slot: ethnicity Description: Reported ethnicity as defined by the 1997 OMB directives.
--     * Slot: population Description: opulation, Race, and/or Ethnicity information.
--     * Slot: dob Description: Date of Birth of the participant. Details of privacy method should be included in DOBMethod
--     * Slot: dob_method Description: Specifies method used to alter DOB for research sharing. Details should be available in the study protocols.
--     * Slot: patient_knowledge_source Description: The source of the knowledge represented by this Patient resource.
--     * Slot: participant_id Description: Participant Global ID
--     * Slot: consent_status Description: Indicates the state of the consent.
--     * Slot: age_at_last_vital_id Description: Age or date of last vital status
--     * Slot: deceased_id Description: Implementers can provide relativeDateTime or actual date or T/F, depending on data available.
-- # Class: Period Description: Time period associated with some FHIR resource
--     * Slot: start Description: Start attribute for a FHIR period data type.
--     * Slot: end Description: End attribute for a FHIR period data type.
--     * Slot: id Description: Unique Identifier for a table entry. This is probably not the Global ID
-- # Class: PractitionerRole Description: PractitionerRole covers the recording of the location and types of services that Practitioners are able to provide for an organization.
--     * Slot: institution_id Description: The institution this record is associated with.
--     * Slot: practitioner_id Description: The Global ID for the PractitionerRole that links a Practitioner to their Institution.
--     * Slot: period_id Description: Reference to a time period which defines a Start and End datatime period.
--     * Slot: practitioner_role_id Description: Global ID for this record
-- # Class: RelativeDateTime Description: In FHIR, we can express events using relative date/times from the participant's DOB to avoid exposing sensitive information
--     * Slot: id Description: Unique Identifier for a table entry. This is probably not the Global ID
--     * Slot: target_resource Description: FHIR Resource Type for target (i.e. Patient)
--     * Slot: target_path Description: resource property about which this is related
--     * Slot: offset Description: The point after the target being described. For ranges, this can be used for the starting point
--     * Slot: offset_end Description: The end of a relative date/time range
-- # Class: ResearchStudy Description: The NCPI Research Study FHIR resource represents an individual research effort and acts as a grouper or “container” for that effort’s study participants and their related data files.
--     * Slot: study_title Description: Research Study's formal title.
--     * Slot: parent_study_id Description: ID For Parent Study if this is a substudy
--     * Slot: description Description: More details associated with the given resource
--     * Slot: study_status Description: The current state of the study.
--     * Slot: research_study_id Description: The Global ID for the Research Study.
-- # Class: ResearchStudyCollection Description: Collections of research data including, but not limited, to Consortia, Programs, adhoc collections of Studies and datasets among other types of collections.
--     * Slot: collection_title Description: The collection's title.
--     * Slot: research_study_collection_type Description: The type of collection being described.
--     * Slot: website Description: URL describing the entity this represents. This can include a formal website, such as the Entity's website, or to an online document describing the entity.
--     * Slot: collection_status Description: The current state of the collection
--     * Slot: research_study_collection_id Description: Global ID for this record
--     * Slot: description Description: The description of the collection.
-- # Class: HasExternalId_external_id
--     * Slot: HasExternalId_id Description: Autocreated FK slot
--     * Slot: external_id Description: Other identifiers for this entity, eg, from the submitting study or in systems link dbGaP
-- # Class: Record_external_id
--     * Slot: Record_id Description: Autocreated FK slot
--     * Slot: external_id Description: Other identifiers for this entity, eg, from the submitting study or in systems link dbGaP
-- # Class: AccessPolicy_access_policy_code
--     * Slot: AccessPolicy_access_policy_id Description: Autocreated FK slot
--     * Slot: access_policy_code Description: A classification of the type of consents found in a consent statement.
-- # Class: Practitioner_external_id
--     * Slot: Practitioner_practitioner_id Description: Autocreated FK slot
--     * Slot: external_id Description: Other identifiers for this entity, eg, from the submitting study or in systems link dbGaP
-- # Class: AssociatedParty_classifier
--     * Slot: AssociatedParty_id Description: Autocreated FK slot
--     * Slot: classifier Description: Research Study Party Organization Type (what type of institution is party)
-- # Class: AssociatedParty_external_id
--     * Slot: AssociatedParty_id Description: Autocreated FK slot
--     * Slot: external_id Description: Other identifiers for this entity, eg, from the submitting study or in systems link dbGaP
-- # Class: Institution_external_id
--     * Slot: Institution_institution_id Description: Autocreated FK slot
--     * Slot: external_id Description: Other identifiers for this entity, eg, from the submitting study or in systems link dbGaP
-- # Class: Participant_race
--     * Slot: Participant_participant_id Description: Autocreated FK slot
--     * Slot: race Description: Reported race as defined by the 1997 OMB directives.
-- # Class: Participant_external_id
--     * Slot: Participant_participant_id Description: Autocreated FK slot
--     * Slot: external_id Description: Other identifiers for this entity, eg, from the submitting study or in systems link dbGaP
-- # Class: Period_external_id
--     * Slot: Period_id Description: Autocreated FK slot
--     * Slot: external_id Description: Other identifiers for this entity, eg, from the submitting study or in systems link dbGaP
-- # Class: ResearchStudy_study_focus
--     * Slot: ResearchStudy_research_study_id Description: Autocreated FK slot
--     * Slot: study_focus Description: The primary, non-disease focus(es) of the study. This can include terms related to intervention, drug, device, or other focus.
-- # Class: ResearchStudy_study_condition
--     * Slot: ResearchStudy_research_study_id Description: Autocreated FK slot
--     * Slot: study_condition Description: The primary focus(es) of the study. This is specific to the disease. MeSH terms are preferred.
-- # Class: ResearchStudy_study_acknowledgement
--     * Slot: ResearchStudy_research_study_id Description: Autocreated FK slot
--     * Slot: study_acknowledgement Description: Any attribution or acknowledgements relevant to the study. This can include but is not limited to funding sources, organizational affiliations or sponsors.
-- # Class: ResearchStudy_study_design
--     * Slot: ResearchStudy_research_study_id Description: Autocreated FK slot
--     * Slot: study_design Description: Study Design and Study Type ([example ValueSet can be found here](https://hl7.org/fhir/valueset-study-design.html))
-- # Class: ResearchStudy_study_personnel
--     * Slot: ResearchStudy_research_study_id Description: Autocreated FK slot
--     * Slot: study_personnel_id Description: Every study must have at least one Primary Contact defined. Additional personnel such as Primary Investigator(s), Administrator(s), Collaborator(s) or other roles may also be included. If there are no appropriate individuals who can serve as primary contact for a study, an organization may be provided.
-- # Class: ResearchStudy_external_id
--     * Slot: ResearchStudy_research_study_id Description: Autocreated FK slot
--     * Slot: external_id Description: Other identifiers for this entity, eg, from the submitting study or in systems link dbGaP
-- # Class: ResearchStudyCollection_label
--     * Slot: ResearchStudyCollection_research_study_collection_id Description: Autocreated FK slot
--     * Slot: label Description: Alias such as acronym and alternate names.
-- # Class: ResearchStudyCollection_research_study_collection_member_id
--     * Slot: ResearchStudyCollection_research_study_collection_id Description: Autocreated FK slot
--     * Slot: research_study_collection_member_id_research_study_id Description: ID associated with a member of the collection (Research Study, Dataset, etc)
-- # Class: ResearchStudyCollection_external_id
--     * Slot: ResearchStudyCollection_research_study_collection_id Description: Autocreated FK slot
--     * Slot: external_id Description: Other identifiers for this entity, eg, from the submitting study or in systems link dbGaP

CREATE TABLE "Any" (
	id INTEGER NOT NULL,
	PRIMARY KEY (id)
);CREATE INDEX "ix_Any_id" ON "Any" (id);
CREATE TABLE "HasExternalId" (
	id INTEGER NOT NULL,
	PRIMARY KEY (id)
);CREATE INDEX "ix_HasExternalId_id" ON "HasExternalId" (id);
CREATE TABLE "Record" (
	id TEXT NOT NULL,
	PRIMARY KEY (id)
);CREATE INDEX "ix_Record_id" ON "Record" (id);
CREATE TABLE "AccessPolicy" (
	description TEXT,
	data_access_type VARCHAR(14) NOT NULL,
	website TEXT,
	consent_scope VARCHAR(15) NOT NULL,
	disease_limitation TEXT,
	access_policy_id TEXT NOT NULL,
	status VARCHAR(16) NOT NULL,
	PRIMARY KEY (access_policy_id)
);CREATE INDEX "ix_AccessPolicy_access_policy_id" ON "AccessPolicy" (access_policy_id);
CREATE TABLE "Institution" (
	name TEXT,
	institution_id TEXT NOT NULL,
	PRIMARY KEY (institution_id)
);CREATE INDEX "ix_Institution_institution_id" ON "Institution" (institution_id);
CREATE TABLE "Period" (
	start DATE,
	"end" DATE,
	id TEXT NOT NULL,
	PRIMARY KEY (id)
);CREATE INDEX "ix_Period_id" ON "Period" (id);
CREATE TABLE "RelativeDateTime" (
	id TEXT NOT NULL,
	target_resource TEXT NOT NULL,
	target_path TEXT NOT NULL,
	"offset" DATE NOT NULL,
	offset_end DATE,
	PRIMARY KEY (id)
);CREATE INDEX "ix_RelativeDateTime_id" ON "RelativeDateTime" (id);
CREATE TABLE "ResearchStudy" (
	study_title TEXT,
	parent_study_id TEXT,
	description TEXT,
	study_status VARCHAR(46) NOT NULL,
	research_study_id TEXT NOT NULL,
	PRIMARY KEY (research_study_id),
	FOREIGN KEY(parent_study_id) REFERENCES "ResearchStudy" (research_study_id)
);CREATE INDEX "ix_ResearchStudy_research_study_id" ON "ResearchStudy" (research_study_id);
CREATE TABLE "ResearchStudyCollection" (
	collection_title TEXT NOT NULL,
	research_study_collection_type VARCHAR(12) NOT NULL,
	website TEXT,
	collection_status VARCHAR(7) NOT NULL,
	research_study_collection_id TEXT NOT NULL,
	description TEXT,
	PRIMARY KEY (research_study_collection_id)
);CREATE INDEX "ix_ResearchStudyCollection_research_study_collection_id" ON "ResearchStudyCollection" (research_study_collection_id);
CREATE TABLE "AssociatedParty" (
	name TEXT,
	role VARCHAR(20),
	period_id TEXT,
	id TEXT NOT NULL,
	party_id INTEGER,
	PRIMARY KEY (id),
	FOREIGN KEY(period_id) REFERENCES "Period" (id),
	FOREIGN KEY(party_id) REFERENCES "Any" (id)
);CREATE INDEX "ix_AssociatedParty_id" ON "AssociatedParty" (id);
CREATE TABLE "Participant" (
	birthsex VARCHAR(6),
	ethnicity VARCHAR(22) NOT NULL,
	population VARCHAR,
	dob DATE,
	dob_method VARCHAR(11),
	patient_knowledge_source VARCHAR(11),
	participant_id TEXT NOT NULL,
	consent_status VARCHAR(16) NOT NULL,
	age_at_last_vital_id INTEGER,
	deceased_id INTEGER,
	PRIMARY KEY (participant_id),
	FOREIGN KEY(age_at_last_vital_id) REFERENCES "Any" (id),
	FOREIGN KEY(deceased_id) REFERENCES "Any" (id)
);CREATE INDEX "ix_Participant_participant_id" ON "Participant" (participant_id);
CREATE TABLE "PractitionerRole" (
	institution_id TEXT,
	practitioner_id TEXT,
	period_id TEXT,
	practitioner_role_id TEXT NOT NULL,
	PRIMARY KEY (practitioner_role_id),
	FOREIGN KEY(institution_id) REFERENCES "Institution" (institution_id),
	FOREIGN KEY(period_id) REFERENCES "Period" (id)
);CREATE INDEX "ix_PractitionerRole_practitioner_role_id" ON "PractitionerRole" (practitioner_role_id);
CREATE TABLE "HasExternalId_external_id" (
	"HasExternalId_id" INTEGER,
	external_id TEXT,
	PRIMARY KEY ("HasExternalId_id", external_id),
	FOREIGN KEY("HasExternalId_id") REFERENCES "HasExternalId" (id)
);CREATE INDEX "ix_HasExternalId_external_id_external_id" ON "HasExternalId_external_id" (external_id);CREATE INDEX "ix_HasExternalId_external_id_HasExternalId_id" ON "HasExternalId_external_id" ("HasExternalId_id");
CREATE TABLE "Record_external_id" (
	"Record_id" TEXT,
	external_id TEXT,
	PRIMARY KEY ("Record_id", external_id),
	FOREIGN KEY("Record_id") REFERENCES "Record" (id)
);CREATE INDEX "ix_Record_external_id_Record_id" ON "Record_external_id" ("Record_id");CREATE INDEX "ix_Record_external_id_external_id" ON "Record_external_id" (external_id);
CREATE TABLE "AccessPolicy_access_policy_code" (
	"AccessPolicy_access_policy_id" TEXT,
	access_policy_code VARCHAR(11) NOT NULL,
	PRIMARY KEY ("AccessPolicy_access_policy_id", access_policy_code),
	FOREIGN KEY("AccessPolicy_access_policy_id") REFERENCES "AccessPolicy" (access_policy_id)
);CREATE INDEX "ix_AccessPolicy_access_policy_code_access_policy_code" ON "AccessPolicy_access_policy_code" (access_policy_code);CREATE INDEX "ix_AccessPolicy_access_policy_code_AccessPolicy_access_policy_id" ON "AccessPolicy_access_policy_code" ("AccessPolicy_access_policy_id");
CREATE TABLE "Institution_external_id" (
	"Institution_institution_id" TEXT,
	external_id TEXT,
	PRIMARY KEY ("Institution_institution_id", external_id),
	FOREIGN KEY("Institution_institution_id") REFERENCES "Institution" (institution_id)
);CREATE INDEX "ix_Institution_external_id_Institution_institution_id" ON "Institution_external_id" ("Institution_institution_id");CREATE INDEX "ix_Institution_external_id_external_id" ON "Institution_external_id" (external_id);
CREATE TABLE "Period_external_id" (
	"Period_id" TEXT,
	external_id TEXT,
	PRIMARY KEY ("Period_id", external_id),
	FOREIGN KEY("Period_id") REFERENCES "Period" (id)
);CREATE INDEX "ix_Period_external_id_Period_id" ON "Period_external_id" ("Period_id");CREATE INDEX "ix_Period_external_id_external_id" ON "Period_external_id" (external_id);
CREATE TABLE "ResearchStudy_study_focus" (
	"ResearchStudy_research_study_id" TEXT,
	study_focus TEXT,
	PRIMARY KEY ("ResearchStudy_research_study_id", study_focus),
	FOREIGN KEY("ResearchStudy_research_study_id") REFERENCES "ResearchStudy" (research_study_id)
);CREATE INDEX "ix_ResearchStudy_study_focus_ResearchStudy_research_study_id" ON "ResearchStudy_study_focus" ("ResearchStudy_research_study_id");CREATE INDEX "ix_ResearchStudy_study_focus_study_focus" ON "ResearchStudy_study_focus" (study_focus);
CREATE TABLE "ResearchStudy_study_condition" (
	"ResearchStudy_research_study_id" TEXT,
	study_condition TEXT,
	PRIMARY KEY ("ResearchStudy_research_study_id", study_condition),
	FOREIGN KEY("ResearchStudy_research_study_id") REFERENCES "ResearchStudy" (research_study_id)
);CREATE INDEX "ix_ResearchStudy_study_condition_study_condition" ON "ResearchStudy_study_condition" (study_condition);CREATE INDEX "ix_ResearchStudy_study_condition_ResearchStudy_research_study_id" ON "ResearchStudy_study_condition" ("ResearchStudy_research_study_id");
CREATE TABLE "ResearchStudy_study_acknowledgement" (
	"ResearchStudy_research_study_id" TEXT,
	study_acknowledgement TEXT,
	PRIMARY KEY ("ResearchStudy_research_study_id", study_acknowledgement),
	FOREIGN KEY("ResearchStudy_research_study_id") REFERENCES "ResearchStudy" (research_study_id)
);CREATE INDEX "ix_ResearchStudy_study_acknowledgement_ResearchStudy_research_study_id" ON "ResearchStudy_study_acknowledgement" ("ResearchStudy_research_study_id");CREATE INDEX "ix_ResearchStudy_study_acknowledgement_study_acknowledgement" ON "ResearchStudy_study_acknowledgement" (study_acknowledgement);
CREATE TABLE "ResearchStudy_study_design" (
	"ResearchStudy_research_study_id" TEXT,
	study_design TEXT,
	PRIMARY KEY ("ResearchStudy_research_study_id", study_design),
	FOREIGN KEY("ResearchStudy_research_study_id") REFERENCES "ResearchStudy" (research_study_id)
);CREATE INDEX "ix_ResearchStudy_study_design_ResearchStudy_research_study_id" ON "ResearchStudy_study_design" ("ResearchStudy_research_study_id");CREATE INDEX "ix_ResearchStudy_study_design_study_design" ON "ResearchStudy_study_design" (study_design);
CREATE TABLE "ResearchStudy_external_id" (
	"ResearchStudy_research_study_id" TEXT,
	external_id TEXT,
	PRIMARY KEY ("ResearchStudy_research_study_id", external_id),
	FOREIGN KEY("ResearchStudy_research_study_id") REFERENCES "ResearchStudy" (research_study_id)
);CREATE INDEX "ix_ResearchStudy_external_id_ResearchStudy_research_study_id" ON "ResearchStudy_external_id" ("ResearchStudy_research_study_id");CREATE INDEX "ix_ResearchStudy_external_id_external_id" ON "ResearchStudy_external_id" (external_id);
CREATE TABLE "ResearchStudyCollection_label" (
	"ResearchStudyCollection_research_study_collection_id" TEXT,
	label TEXT,
	PRIMARY KEY ("ResearchStudyCollection_research_study_collection_id", label),
	FOREIGN KEY("ResearchStudyCollection_research_study_collection_id") REFERENCES "ResearchStudyCollection" (research_study_collection_id)
);CREATE INDEX "ix_ResearchStudyCollection_label_label" ON "ResearchStudyCollection_label" (label);CREATE INDEX "ix_ResearchStudyCollection_label_ResearchStudyCollection_research_study_collection_id" ON "ResearchStudyCollection_label" ("ResearchStudyCollection_research_study_collection_id");
CREATE TABLE "ResearchStudyCollection_research_study_collection_member_id" (
	"ResearchStudyCollection_research_study_collection_id" TEXT,
	research_study_collection_member_id_research_study_id TEXT NOT NULL,
	PRIMARY KEY ("ResearchStudyCollection_research_study_collection_id", research_study_collection_member_id_research_study_id),
	FOREIGN KEY("ResearchStudyCollection_research_study_collection_id") REFERENCES "ResearchStudyCollection" (research_study_collection_id),
	FOREIGN KEY(research_study_collection_member_id_research_study_id) REFERENCES "ResearchStudy" (research_study_id)
);CREATE INDEX "ix_ResearchStudyCollection_research_study_collection_member_id_ResearchStudyCollection_research_study_collection_id" ON "ResearchStudyCollection_research_study_collection_member_id" ("ResearchStudyCollection_research_study_collection_id");CREATE INDEX "ix_ResearchStudyCollection_research_study_collection_member_id_research_study_collection_member_id_research_study_id" ON "ResearchStudyCollection_research_study_collection_member_id" (research_study_collection_member_id_research_study_id);
CREATE TABLE "ResearchStudyCollection_external_id" (
	"ResearchStudyCollection_research_study_collection_id" TEXT,
	external_id TEXT,
	PRIMARY KEY ("ResearchStudyCollection_research_study_collection_id", external_id),
	FOREIGN KEY("ResearchStudyCollection_research_study_collection_id") REFERENCES "ResearchStudyCollection" (research_study_collection_id)
);CREATE INDEX "ix_ResearchStudyCollection_external_id_ResearchStudyCollection_research_study_collection_id" ON "ResearchStudyCollection_external_id" ("ResearchStudyCollection_research_study_collection_id");CREATE INDEX "ix_ResearchStudyCollection_external_id_external_id" ON "ResearchStudyCollection_external_id" (external_id);
CREATE TABLE "Practitioner" (
	name TEXT,
	email TEXT,
	institution_id TEXT,
	practitioner_role_id TEXT,
	description TEXT,
	practitioner_title TEXT,
	practitioner_id TEXT NOT NULL,
	PRIMARY KEY (practitioner_id),
	FOREIGN KEY(institution_id) REFERENCES "Institution" (institution_id),
	FOREIGN KEY(practitioner_role_id) REFERENCES "PractitionerRole" (practitioner_role_id)
);CREATE INDEX "ix_Practitioner_practitioner_id" ON "Practitioner" (practitioner_id);
CREATE TABLE "AssociatedParty_classifier" (
	"AssociatedParty_id" TEXT,
	classifier VARCHAR(10),
	PRIMARY KEY ("AssociatedParty_id", classifier),
	FOREIGN KEY("AssociatedParty_id") REFERENCES "AssociatedParty" (id)
);CREATE INDEX "ix_AssociatedParty_classifier_AssociatedParty_id" ON "AssociatedParty_classifier" ("AssociatedParty_id");CREATE INDEX "ix_AssociatedParty_classifier_classifier" ON "AssociatedParty_classifier" (classifier);
CREATE TABLE "AssociatedParty_external_id" (
	"AssociatedParty_id" TEXT,
	external_id TEXT,
	PRIMARY KEY ("AssociatedParty_id", external_id),
	FOREIGN KEY("AssociatedParty_id") REFERENCES "AssociatedParty" (id)
);CREATE INDEX "ix_AssociatedParty_external_id_AssociatedParty_id" ON "AssociatedParty_external_id" ("AssociatedParty_id");CREATE INDEX "ix_AssociatedParty_external_id_external_id" ON "AssociatedParty_external_id" (external_id);
CREATE TABLE "Participant_race" (
	"Participant_participant_id" TEXT,
	race VARCHAR(35) NOT NULL,
	PRIMARY KEY ("Participant_participant_id", race),
	FOREIGN KEY("Participant_participant_id") REFERENCES "Participant" (participant_id)
);CREATE INDEX "ix_Participant_race_Participant_participant_id" ON "Participant_race" ("Participant_participant_id");CREATE INDEX "ix_Participant_race_race" ON "Participant_race" (race);
CREATE TABLE "Participant_external_id" (
	"Participant_participant_id" TEXT,
	external_id TEXT,
	PRIMARY KEY ("Participant_participant_id", external_id),
	FOREIGN KEY("Participant_participant_id") REFERENCES "Participant" (participant_id)
);CREATE INDEX "ix_Participant_external_id_Participant_participant_id" ON "Participant_external_id" ("Participant_participant_id");CREATE INDEX "ix_Participant_external_id_external_id" ON "Participant_external_id" (external_id);
CREATE TABLE "ResearchStudy_study_personnel" (
	"ResearchStudy_research_study_id" TEXT,
	study_personnel_id TEXT NOT NULL,
	PRIMARY KEY ("ResearchStudy_research_study_id", study_personnel_id),
	FOREIGN KEY("ResearchStudy_research_study_id") REFERENCES "ResearchStudy" (research_study_id),
	FOREIGN KEY(study_personnel_id) REFERENCES "AssociatedParty" (id)
);CREATE INDEX "ix_ResearchStudy_study_personnel_study_personnel_id" ON "ResearchStudy_study_personnel" (study_personnel_id);CREATE INDEX "ix_ResearchStudy_study_personnel_ResearchStudy_research_study_id" ON "ResearchStudy_study_personnel" ("ResearchStudy_research_study_id");
CREATE TABLE "Practitioner_external_id" (
	"Practitioner_practitioner_id" TEXT,
	external_id TEXT,
	PRIMARY KEY ("Practitioner_practitioner_id", external_id),
	FOREIGN KEY("Practitioner_practitioner_id") REFERENCES "Practitioner" (practitioner_id)
);CREATE INDEX "ix_Practitioner_external_id_external_id" ON "Practitioner_external_id" (external_id);CREATE INDEX "ix_Practitioner_external_id_Practitioner_practitioner_id" ON "Practitioner_external_id" ("Practitioner_practitioner_id");
