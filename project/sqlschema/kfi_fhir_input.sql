-- # Abstract Class: Record Description: One row / entity within the database
--     * Slot: id Description: Global ID for this record
-- # Class: Practitioner Description: For our purposes, this will be an investigator.
--     * Slot: name Description: Name of the entity.
--     * Slot: email Description: An email address to reach the entity.
--     * Slot: institution Description: The institution this record is associated with.
--     * Slot: description Description: Note relating to who this person is in relation to the study
--     * Slot: title Description: The title of the Investigator, eg, "Assistant Professor"
--     * Slot: id Description: Global ID for this record
-- # Class: Institution Description: Institution related to study or research personnel
--     * Slot: name Description: Name of the entity.
--     * Slot: id Description: Global ID for this record
-- # Class: Record_external_id
--     * Slot: Record_id Description: Autocreated FK slot
--     * Slot: external_id Description: Other identifiers for this entity, eg, from the submitting study or in systems link dbGaP
-- # Class: Practitioner_external_id
--     * Slot: Practitioner_id Description: Autocreated FK slot
--     * Slot: external_id Description: Other identifiers for this entity, eg, from the submitting study or in systems link dbGaP
-- # Class: Institution_external_id
--     * Slot: Institution_id Description: Autocreated FK slot
--     * Slot: external_id Description: Other identifiers for this entity, eg, from the submitting study or in systems link dbGaP

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
	institution TEXT,
	description TEXT,
	title TEXT,
	id TEXT NOT NULL,
	PRIMARY KEY (id),
	FOREIGN KEY(institution) REFERENCES "Institution" (id)
);CREATE INDEX "ix_Practitioner_id" ON "Practitioner" (id);
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
);CREATE INDEX "ix_Institution_external_id_Institution_id" ON "Institution_external_id" ("Institution_id");CREATE INDEX "ix_Institution_external_id_external_id" ON "Institution_external_id" (external_id);
CREATE TABLE "Practitioner_external_id" (
	"Practitioner_id" TEXT,
	external_id TEXT,
	PRIMARY KEY ("Practitioner_id", external_id),
	FOREIGN KEY("Practitioner_id") REFERENCES "Practitioner" (id)
);CREATE INDEX "ix_Practitioner_external_id_external_id" ON "Practitioner_external_id" (external_id);CREATE INDEX "ix_Practitioner_external_id_Practitioner_id" ON "Practitioner_external_id" ("Practitioner_id");
