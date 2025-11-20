-- # Abstract Class: Any Description: This is a placeholder for the experimental linkml:any behavior for unions
--     * Slot: id
-- # Abstract Class: Record Description: One row / entity within the database
--     * Slot: id Description: Global ID for this record
-- # Class: Practitioner Description: For our purposes, this will be an investigator.
--     * Slot: name Description: Name of the entity.
--     * Slot: email Description: An email address to reach the entity.
--     * Slot: institution_id Description: The institution this record is associated with.
--     * Slot: description Description: Note relating to who this person is in relation to the study
--     * Slot: title Description: The title of the Investigator, eg, "Assistant Professor"
--     * Slot: id Description: Global ID for this record
-- # Class: Institution Description: Institution related to study or research personnel
--     * Slot: name Description: Name of the entity.
--     * Slot: id Description: Global ID for this record
-- # Class: AssociatedParty Description: Sponsors, collaborators, and other parties affiliated with a research study.
--     * Slot: name Description: Name of the entity.
--     * Slot: role Description: Research Study Party Role
--     * Slot: id Description: Global ID for this record
--     * Slot: party_id Description: Individual or organization associated with study
-- # Class: Record_external_id
--     * Slot: Record_id Description: Autocreated FK slot
--     * Slot: external_id Description: Other identifiers for this entity, eg, from the submitting study or in systems link dbGaP
-- # Class: Practitioner_external_id
--     * Slot: Practitioner_id Description: Autocreated FK slot
--     * Slot: external_id Description: Other identifiers for this entity, eg, from the submitting study or in systems link dbGaP
-- # Class: Institution_external_id
--     * Slot: Institution_id Description: Autocreated FK slot
--     * Slot: external_id Description: Other identifiers for this entity, eg, from the submitting study or in systems link dbGaP
-- # Class: AssociatedParty_period_start
--     * Slot: AssociatedParty_id Description: Autocreated FK slot
--     * Slot: period_start Description: Start attribute for a FHIR period data type.
-- # Class: AssociatedParty_period_end
--     * Slot: AssociatedParty_id Description: Autocreated FK slot
--     * Slot: period_end Description: End attribute for a FHIR period data type.
-- # Class: AssociatedParty_classifier
--     * Slot: AssociatedParty_id Description: Autocreated FK slot
--     * Slot: classifier Description: Research Study Party Organization Type (what type of institution is party)
-- # Class: AssociatedParty_external_id
--     * Slot: AssociatedParty_id Description: Autocreated FK slot
--     * Slot: external_id Description: Other identifiers for this entity, eg, from the submitting study or in systems link dbGaP

CREATE TABLE "Any" (
	id INTEGER NOT NULL,
	PRIMARY KEY (id)
);CREATE INDEX "ix_Any_id" ON "Any" (id);
CREATE TABLE "Record" (
	id TEXT NOT NULL,
	PRIMARY KEY (id)
);CREATE INDEX "ix_Record_id" ON "Record" (id);
CREATE TABLE "Institution" (
	name TEXT,
	id TEXT NOT NULL,
	PRIMARY KEY (id)
);CREATE INDEX "ix_Institution_id" ON "Institution" (id);
CREATE TABLE "Practitioner" (
	name TEXT,
	email TEXT,
	institution_id TEXT,
	description TEXT,
	title TEXT,
	id TEXT NOT NULL,
	PRIMARY KEY (id),
	FOREIGN KEY(institution_id) REFERENCES "Institution" (id)
);CREATE INDEX "ix_Practitioner_id" ON "Practitioner" (id);
CREATE TABLE "AssociatedParty" (
	name TEXT,
	role VARCHAR(20),
	id TEXT NOT NULL,
	party_id INTEGER,
	PRIMARY KEY (id),
	FOREIGN KEY(party_id) REFERENCES "Any" (id)
);CREATE INDEX "ix_AssociatedParty_id" ON "AssociatedParty" (id);
CREATE TABLE "Record_external_id" (
	"Record_id" TEXT,
	external_id TEXT,
	PRIMARY KEY ("Record_id", external_id),
	FOREIGN KEY("Record_id") REFERENCES "Record" (id)
);CREATE INDEX "ix_Record_external_id_Record_id" ON "Record_external_id" ("Record_id");CREATE INDEX "ix_Record_external_id_external_id" ON "Record_external_id" (external_id);
CREATE TABLE "Institution_external_id" (
	"Institution_id" TEXT,
	external_id TEXT,
	PRIMARY KEY ("Institution_id", external_id),
	FOREIGN KEY("Institution_id") REFERENCES "Institution" (id)
);CREATE INDEX "ix_Institution_external_id_external_id" ON "Institution_external_id" (external_id);CREATE INDEX "ix_Institution_external_id_Institution_id" ON "Institution_external_id" ("Institution_id");
CREATE TABLE "Practitioner_external_id" (
	"Practitioner_id" TEXT,
	external_id TEXT,
	PRIMARY KEY ("Practitioner_id", external_id),
	FOREIGN KEY("Practitioner_id") REFERENCES "Practitioner" (id)
);CREATE INDEX "ix_Practitioner_external_id_Practitioner_id" ON "Practitioner_external_id" ("Practitioner_id");CREATE INDEX "ix_Practitioner_external_id_external_id" ON "Practitioner_external_id" (external_id);
CREATE TABLE "AssociatedParty_period_start" (
	"AssociatedParty_id" TEXT,
	period_start DATETIME,
	PRIMARY KEY ("AssociatedParty_id", period_start),
	FOREIGN KEY("AssociatedParty_id") REFERENCES "AssociatedParty" (id)
);CREATE INDEX "ix_AssociatedParty_period_start_AssociatedParty_id" ON "AssociatedParty_period_start" ("AssociatedParty_id");CREATE INDEX "ix_AssociatedParty_period_start_period_start" ON "AssociatedParty_period_start" (period_start);
CREATE TABLE "AssociatedParty_period_end" (
	"AssociatedParty_id" TEXT,
	period_end DATETIME,
	PRIMARY KEY ("AssociatedParty_id", period_end),
	FOREIGN KEY("AssociatedParty_id") REFERENCES "AssociatedParty" (id)
);CREATE INDEX "ix_AssociatedParty_period_end_period_end" ON "AssociatedParty_period_end" (period_end);CREATE INDEX "ix_AssociatedParty_period_end_AssociatedParty_id" ON "AssociatedParty_period_end" ("AssociatedParty_id");
CREATE TABLE "AssociatedParty_classifier" (
	"AssociatedParty_id" TEXT,
	classifier VARCHAR(3),
	PRIMARY KEY ("AssociatedParty_id", classifier),
	FOREIGN KEY("AssociatedParty_id") REFERENCES "AssociatedParty" (id)
);CREATE INDEX "ix_AssociatedParty_classifier_AssociatedParty_id" ON "AssociatedParty_classifier" ("AssociatedParty_id");CREATE INDEX "ix_AssociatedParty_classifier_classifier" ON "AssociatedParty_classifier" (classifier);
CREATE TABLE "AssociatedParty_external_id" (
	"AssociatedParty_id" TEXT,
	external_id TEXT,
	PRIMARY KEY ("AssociatedParty_id", external_id),
	FOREIGN KEY("AssociatedParty_id") REFERENCES "AssociatedParty" (id)
);CREATE INDEX "ix_AssociatedParty_external_id_external_id" ON "AssociatedParty_external_id" (external_id);CREATE INDEX "ix_AssociatedParty_external_id_AssociatedParty_id" ON "AssociatedParty_external_id" ("AssociatedParty_id");
