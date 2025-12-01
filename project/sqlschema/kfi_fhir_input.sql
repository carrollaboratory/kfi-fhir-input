-- # Abstract Class: Any Description: This is a placeholder for the experimental linkml:any behavior for unions
--     * Slot: id
-- # Abstract Class: HasExternalId Description: Has an external ID
--     * Slot: id
-- # Abstract Class: Record Description: One row / entity within the database
--     * Slot: id Description: Global ID for this record
-- # Class: Practitioner Description: For our purposes, this will be an investigator.
--     * Slot: name Description: Name of the entity.
--     * Slot: email Description: An email address to reach the entity.
--     * Slot: institution_id Description: The institution this record is associated with.
--     * Slot: practitioner_role_id Description: Global ID for this record
--     * Slot: description Description: More details associated with the given resource
--     * Slot: practitioner_title Description: The title of the Investigator, eg, "Assistant Professor"
--     * Slot: practitioner_id Description: The Global ID for the Practitioner.
-- # Class: AssociatedParty Description: Sponsors, collaborators, and other parties affiliated with a research study.
--     * Slot: id
--     * Slot: name Description: Name of the entity.
--     * Slot: role Description: Research Study Party Role
--     * Slot: party_id Description: Individual or organization associated with study
-- # Class: Institution Description: Institution related to study or research personnel
--     * Slot: name Description: Name of the entity.
--     * Slot: institution_id Description: Global ID for this record
-- # Class: Period Description: Time period associated with some FHIR resource
--     * Slot: period_id Description: Database ID for this record. This is not a global ID, is a global identifier
--     * Slot: start Description: Start attribute for a FHIR period data type.
--     * Slot: end Description: End attribute for a FHIR period data type.
-- # Class: PractitionerRole Description: PractitionerRole covers the recording of the location and types of services that Practitioners are able to provide for an organization.
--     * Slot: institution_id Description: The institution this record is associated with.
--     * Slot: practitioner_id Description: The Global ID for the PractitionerRole that links a Practitioner to their Institution.
--     * Slot: period_id Description: Reference to a time period which defines a Start and End datatime period.
--     * Slot: practitioner_role_id Description: Global ID for this record
-- # Class: ResearchStudy Description: The NCPI Research Study FHIR resource represents an individual research effort and acts as a grouper or “container” for that effort’s study participants and their related data files.
--     * Slot: study_title Description: Research	Study's formal title.
--     * Slot: description Description: More details associated with the given resource
--     * Slot: study_status Description: The current state of the study.
--     * Slot: research_study_id Description: The Global ID for the Research Study.
-- # Class: HasExternalId_external_id
--     * Slot: HasExternalId_id Description: Autocreated FK slot
--     * Slot: external_id Description: Other identifiers for this entity, eg, from the submitting study or in systems link dbGaP
-- # Class: Record_external_id
--     * Slot: Record_id Description: Autocreated FK slot
--     * Slot: external_id Description: Other identifiers for this entity, eg, from the submitting study or in systems link dbGaP
-- # Class: Practitioner_external_id
--     * Slot: Practitioner_practitioner_id Description: Autocreated FK slot
--     * Slot: external_id Description: Other identifiers for this entity, eg, from the submitting study or in systems link dbGaP
-- # Class: AssociatedParty_period_id
--     * Slot: AssociatedParty_id Description: Autocreated FK slot
--     * Slot: period_id_period_id Description: Reference to a time period which defines a Start and End datatime period.
-- # Class: AssociatedParty_classifier
--     * Slot: AssociatedParty_id Description: Autocreated FK slot
--     * Slot: classifier Description: Research Study Party Organization Type (what type of institution is party)
-- # Class: Institution_external_id
--     * Slot: Institution_institution_id Description: Autocreated FK slot
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
-- # Class: ResearchStudy_external_id
--     * Slot: ResearchStudy_research_study_id Description: Autocreated FK slot
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
CREATE TABLE "Institution" (
	name TEXT,
	institution_id TEXT NOT NULL,
	PRIMARY KEY (institution_id)
);CREATE INDEX "ix_Institution_institution_id" ON "Institution" (institution_id);
CREATE TABLE "Period" (
	period_id TEXT NOT NULL,
	start DATETIME,
	"end" DATETIME,
	PRIMARY KEY (period_id)
);CREATE INDEX "ix_Period_period_id" ON "Period" (period_id);
CREATE TABLE "ResearchStudy" (
	study_title TEXT,
	description TEXT,
	study_status VARCHAR(46) NOT NULL,
	research_study_id TEXT NOT NULL,
	PRIMARY KEY (research_study_id)
);CREATE INDEX "ix_ResearchStudy_research_study_id" ON "ResearchStudy" (research_study_id);
CREATE TABLE "AssociatedParty" (
	id INTEGER NOT NULL,
	name TEXT,
	role VARCHAR(20),
	party_id INTEGER,
	PRIMARY KEY (id),
	FOREIGN KEY(party_id) REFERENCES "Any" (id)
);CREATE INDEX "ix_AssociatedParty_id" ON "AssociatedParty" (id);
CREATE TABLE "PractitionerRole" (
	institution_id TEXT,
	practitioner_id TEXT,
	period_id TEXT,
	practitioner_role_id TEXT NOT NULL,
	PRIMARY KEY (practitioner_role_id),
	FOREIGN KEY(institution_id) REFERENCES "Institution" (institution_id),
	FOREIGN KEY(period_id) REFERENCES "Period" (period_id)
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
CREATE TABLE "Institution_external_id" (
	"Institution_institution_id" TEXT,
	external_id TEXT,
	PRIMARY KEY ("Institution_institution_id", external_id),
	FOREIGN KEY("Institution_institution_id") REFERENCES "Institution" (institution_id)
);CREATE INDEX "ix_Institution_external_id_Institution_institution_id" ON "Institution_external_id" ("Institution_institution_id");CREATE INDEX "ix_Institution_external_id_external_id" ON "Institution_external_id" (external_id);
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
);CREATE INDEX "ix_ResearchStudy_study_condition_ResearchStudy_research_study_id" ON "ResearchStudy_study_condition" ("ResearchStudy_research_study_id");CREATE INDEX "ix_ResearchStudy_study_condition_study_condition" ON "ResearchStudy_study_condition" (study_condition);
CREATE TABLE "ResearchStudy_study_acknowledgement" (
	"ResearchStudy_research_study_id" TEXT,
	study_acknowledgement TEXT,
	PRIMARY KEY ("ResearchStudy_research_study_id", study_acknowledgement),
	FOREIGN KEY("ResearchStudy_research_study_id") REFERENCES "ResearchStudy" (research_study_id)
);CREATE INDEX "ix_ResearchStudy_study_acknowledgement_ResearchStudy_research_study_id" ON "ResearchStudy_study_acknowledgement" ("ResearchStudy_research_study_id");CREATE INDEX "ix_ResearchStudy_study_acknowledgement_study_acknowledgement" ON "ResearchStudy_study_acknowledgement" (study_acknowledgement);
CREATE TABLE "ResearchStudy_external_id" (
	"ResearchStudy_research_study_id" TEXT,
	external_id TEXT,
	PRIMARY KEY ("ResearchStudy_research_study_id", external_id),
	FOREIGN KEY("ResearchStudy_research_study_id") REFERENCES "ResearchStudy" (research_study_id)
);CREATE INDEX "ix_ResearchStudy_external_id_external_id" ON "ResearchStudy_external_id" (external_id);CREATE INDEX "ix_ResearchStudy_external_id_ResearchStudy_research_study_id" ON "ResearchStudy_external_id" ("ResearchStudy_research_study_id");
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
CREATE TABLE "AssociatedParty_period_id" (
	"AssociatedParty_id" INTEGER,
	period_id_period_id TEXT,
	PRIMARY KEY ("AssociatedParty_id", period_id_period_id),
	FOREIGN KEY("AssociatedParty_id") REFERENCES "AssociatedParty" (id),
	FOREIGN KEY(period_id_period_id) REFERENCES "Period" (period_id)
);CREATE INDEX "ix_AssociatedParty_period_id_AssociatedParty_id" ON "AssociatedParty_period_id" ("AssociatedParty_id");CREATE INDEX "ix_AssociatedParty_period_id_period_id_period_id" ON "AssociatedParty_period_id" (period_id_period_id);
CREATE TABLE "AssociatedParty_classifier" (
	"AssociatedParty_id" INTEGER,
	classifier VARCHAR(3),
	PRIMARY KEY ("AssociatedParty_id", classifier),
	FOREIGN KEY("AssociatedParty_id") REFERENCES "AssociatedParty" (id)
);CREATE INDEX "ix_AssociatedParty_classifier_classifier" ON "AssociatedParty_classifier" (classifier);CREATE INDEX "ix_AssociatedParty_classifier_AssociatedParty_id" ON "AssociatedParty_classifier" ("AssociatedParty_id");
CREATE TABLE "Practitioner_external_id" (
	"Practitioner_practitioner_id" TEXT,
	external_id TEXT,
	PRIMARY KEY ("Practitioner_practitioner_id", external_id),
	FOREIGN KEY("Practitioner_practitioner_id") REFERENCES "Practitioner" (practitioner_id)
);CREATE INDEX "ix_Practitioner_external_id_external_id" ON "Practitioner_external_id" (external_id);CREATE INDEX "ix_Practitioner_external_id_Practitioner_practitioner_id" ON "Practitioner_external_id" ("Practitioner_practitioner_id");
