-- # Abstract Class: Any Description: This is a placeholder for the experimental linkml:any behavior for unions
--     * Slot: id
-- # Abstract Class: HasExternalId Description: Has an external ID
--     * Slot: id
-- # Abstract Class: Record Description: One row / entity within the database
--     * Slot: id Description: Unique Identifier for a table entry. This is probably not the Global ID
-- # Class: AccessPolicy Description: Limitations and/or requirements that define how a user may gain access to a particular set of data.
--     * Slot: access_policy_id Description: Access policy communicates the limitations and/or requirements that define how a user may gain access to a particular set of data.
--     * Slot: description Description: More details associated with the given resource
--     * Slot: data_access_type Description: Type of access restrictions on file downloads ( open | registered | controlled )
--     * Slot: website Description: URL describing the entity this represents. This can include a formal website, such as the Entity's website, or to an online document describing the entity.
--     * Slot: consent_scope Description: Which of the four areas this resource covers (extensible)
--     * Slot: disease_limitation Description: Disease Use Limitations
--     * Slot: status Description: Indicates the state of the consent.
-- # Class: RelativeDateTime Description: In FHIR, we can express events using relative date/times from the participant's DOB to avoid exposing sensitive information
--     * Slot: id Description: Unique Identifier for a table entry. This is probably not the Global ID
--     * Slot: offset Description: The point after the target being described. For ranges, this can be used for the starting point
--     * Slot: offset_end Description: The end of a relative date/time range
--     * Slot: offset_type Description: What is the datatype associated with the offset (days, years, etc)
-- # Class: AgeAt Description: These represent a flexible age value that could represent one of the following-Relative Age Offset, Age Range as Code, Date Range, DateTime
--     * Slot: value_type Description: Age Value Type
--     * Slot: age Description: Age either numeric value or range
--     * Slot: age_code Description: Age expressed as an enumerated value representing an age category
--     * Slot: as_date Description: Event Date (rather than age)
--     * Slot: id Description: Unique Identifier for a table entry. This is probably not the Global ID
-- # Class: ParticipantAssertion Description: Assertion about a particular Participant. May include Conditions, Measurements, etc.
--     * Slot: participant_id Description: The Global ID for the Participant
--     * Slot: age_at_event Description: The date or age at which the event relating to this assertion occured.
--     * Slot: age_at_assertion Description: The date or age at which this condition is being asserted.
--     * Slot: age_at_onset Description: The age of onset for this condition. Could be expressed with a term, an age, or an age range.
--     * Slot: age_at_resolution Description: The age at which this condition was resolved, abated, or cured. Should be left empty in cases of current active status. Could be expressed with a term, an age, or an age range.
--     * Slot: entity_asserter Description: Who recorded this assertion about the Participant? This can support understanding the differences between self-report, doctor, trained research staff.
--     * Slot: other_condition_modifiers Description: Any additional modifiers for this condition, such as severity.
--     * Slot: assertion_type Description: Describe the type of assertion being made.
--     * Slot: assertion_code Description: The structured term defining the meaning of the assertion.
--     * Slot: assertion_text Description: Detailed description / free text about this assertion.
--     * Slot: assertion_source Description: Where or how was this this assertion about the Participant recorded? This can support understanding the differences between surveys, automated EHR extraction, manual chart abstraction, etc.
--     * Slot: value_code Description: Value as code
--     * Slot: value_string Description: Value as string
--     * Slot: value_number Description: Value as numer
--     * Slot: value_units Description: The structured term defining the units of the value (ucum).
--     * Slot: body_site Description: Location information for the observation, including site, laterality, and other qualifiers as appropriate. Multiple observations may be required if the same assertion is made in many locations, or complete location details can be provided in an NCPI Condition Summary.
--     * Slot: body_location Description: Any location qualifiers
--     * Slot: body_laterality Description: Laterality information for the condition site
--     * Slot: cancer_stage Description: Cancer staging information
--     * Slot: participant_assertion_id Description: Participant Assertion Global ID
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
--     * Slot: associated_party_practitioner_id Description: Associated Party (is Practitioner).
--     * Slot: associated_party_practitioner_role_id Description: Associated Party (is Practitioner Role)
--     * Slot: associated_party_institution_id Description: Associated Party (is Institution)
--     * Slot: id Description: Unique Identifier for a table entry. This is probably not the Global ID
-- # Class: Institution Description: Institution related to study or research personnel
--     * Slot: institution_id Description: The institution this record is associated with.
--     * Slot: name Description: Name of the entity.
-- # Class: Participant Description: Research oriented patient
--     * Slot: participant_id Description: The Global ID for the Participant
--     * Slot: birthsex Description: Sex assigned at birth (or pre-natal observed sex)
--     * Slot: ethnicity Description: Reported ethnicity as defined by the 1997 OMB directives.
--     * Slot: population Description: opulation, Race, and/or Ethnicity information.
--     * Slot: dob Description: Date of Birth of the participant. Details of privacy method should be included in DOBMethod
--     * Slot: dob_method Description: Specifies method used to alter DOB for research sharing. Details should be available in the study protocols.
--     * Slot: age_at_last_vital Description: Age or date of last vital status
--     * Slot: is_deceased Description: Is the participant known to be Deceased, T, or Alive, F
--     * Slot: deceased_rel Description: Implementers can provide relativeDateTime if information is available.
--     * Slot: patient_knowledge_source Description: The source of the knowledge represented by this Patient resource.
--     * Slot: family_global_id Description: The family the participant is a part of
-- # Class: Person Description: Relate one or more participants to a single person entity
--     * Slot: person_id Description: Person Global ID (group)
-- # Class: Period Description: Time period associated with some FHIR resource
--     * Slot: period_id Description: ID for period (not a global ID)
--     * Slot: start Description: Start attribute for a FHIR period data type.
--     * Slot: end Description: End attribute for a FHIR period data type.
-- # Class: PractitionerRole Description: PractitionerRole covers the recording of the location and types of services that Practitioners are able to provide for an organization.
--     * Slot: institution_id Description: The institution this record is associated with.
--     * Slot: practitioner_id Description: The Global ID for the PractitionerRole that links a Practitioner to their Institution.
--     * Slot: period_id Description: Reference to a time period which defines a Start and End datatime period.
--     * Slot: practitioner_role_id Description: Global ID for this record
-- # Class: StudyMembership Description: Grouping subject participation within a research study is helpful to provide definitive lists of participants that fit a specific criteria such as All Participants or Participants From a Particular Consent Group, etc.
--     * Slot: study_membership_id Description: Study Membership Global ID (group)
--     * Slot: access_policy_id Description: Access Policy Global ID
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
-- # Class: Sample Description: Sample encompasses biospecimen collection, sample information, and aliquot information.
--     * Slot: sample_id Description: Sample Global ID
--     * Slot: parent_sample_id Description: Sample Global ID associated with the parent sample
--     * Slot: participant_id Description: The Global ID for the Participant
--     * Slot: sample_type Description: The type of material of which this Sample is comprised
--     * Slot: age_at_collection Description: The age at which this biospecimen was collected. Could be expressed with a term, an age, or an age range.
--     * Slot: collection_method Description: The approach used to collect the biospecimen ([LOINC](https://loinc.org))
--     * Slot: collection_site Description: The location of the specimen collection
--     * Slot: spatial_qualifier Description: Any spatial/location qualifiers
--     * Slot: laterality Description: Laterality information for the site
--     * Slot: availability_status Description: Can this Sample be requested for further analysis?
--     * Slot: storage_method Description: How is the Sample stored, eg, Frozen or with additives (e.g. https://terminology.hl7.org/5.3.0/ValueSet-v2-0493.html)
--     * Slot: quantity Description: The total quantity of the specimen
--     * Slot: quantity_units Description: Units associated with the quantity (ucum)
-- # Class: Aliquot Description: A Portion of a sample extracted from a participant.
--     * Slot: aliquot_id Description: Aliquot Global ID
--     * Slot: availability_status Description: Can this Sample be requested for further analysis?
--     * Slot: volume Description: What is the volume of the Aliquot?
--     * Slot: volume_units Description: Units associated with the volume (ucum)
--     * Slot: concentration Description: What is the concentration of the analyte in the Aliquot?
--     * Slot: sample_id Description: Sample Global ID
-- # Class: NCPIFile Description: Information about a file related to a research participant
--     * Slot: participant_id Description: The Global ID for the Participant
--     * Slot: file_format Description: The file format used ([EDAM](http://edamontology.org) where possible)
--     * Slot: file_size Description: The size of the file, e.g., in bytes.
--     * Slot: file_size_unit Description: Units associated with the file_size value (ucum)
--     * Slot: content_version Description: Version of the file content
--     * Slot: file_type Description: The type of data contained in this file. Should be as detailed as possible, e.g., Whole Exome Variant Calls.
--     * Slot: file_hash Description: Value of hashing the file
--     * Slot: file_hash_type Description: Algorithm used to calculate the hash (and size, where applicable)
--     * Slot: description Description: More details associated with the given resource
--     * Slot: file_global_id Description: File Global ID
-- # Class: FileLocation Description: Details relating to the links where documents are found
--     * Slot: file_location_id Description: Location details (this is not a global ID)
--     * Slot: location_uri Description: The URI at which this data can be accessed
--     * Slot: file_name Description: The file's name (no path)
--     * Slot: access_policy_id Description: Access Policy Global ID
-- # Class: FamilyRelationship Description: A relationship between individuals in a pedigree or family.
--     * Slot: family_relationship_id Description: Family Relationship Global ID
--     * Slot: patient_id Description: The child from the parent-child relationship
--     * Slot: relative_id Description: The parent from the parent-child relationship
--     * Slot: relationship Description: The role the relative (parent) fills with respect to the patient (child) for this relationship.
--     * Slot: knowledge_source Description: The source for the reltionship term
-- # Class: FileMetaData Description: Representation of file metadata for NCPI
--     * Slot: file_meta_data_id Description: Representation of file metadata for NCPI
--     * Slot: meta_data_type Description: Clarify which type of meta data this file has recorded
--     * Slot: assay_strategy Description: e.g., Whole Genome Sequencing
--     * Slot: platform_instrument Description: e.g., Illumina HiSeq2000
--     * Slot: library_prep Description: e.g., polyA
--     * Slot: library_selection Description: ...
--     * Slot: strandedness Description: stranded, unstranded
--     * Slot: target_region Description: Target region
--     * Slot: is_paired_end Description: True, False
--     * Slot: adaptor_trimmed Description: True, False
--     * Slot: reference_genome Description: GRCh37, GRCh38
--     * Slot: workflow_type Description: e.g., alignment, somatic
--     * Slot: workflow_tool Description: e.g., BAM-MEM, GATK-Haplotype Caller
-- # Class: Family Description: Group of Participants that are related.
--     * Slot: family_global_id Description: Family Global ID
--     * Slot: family_id Description: External ID common to all family members
--     * Slot: family_type Description: Describes the 'type' of study family, eg, trio.
--     * Slot: description Description: More details associated with the given resource
--     * Slot: consanguinity Description: Is there known or suspected consanguinity in this study family?
--     * Slot: family_focus Description: What is this study family investigating? EG, a specific condition
-- # Class: HasExternalId_external_id
--     * Slot: HasExternalId_id Description: Autocreated FK slot
--     * Slot: external_id Description: Other identifiers for this entity, eg, from the submitting study or in systems link dbGaP
-- # Class: Record_external_id
--     * Slot: Record_id Description: Autocreated FK slot
--     * Slot: external_id Description: Other identifiers for this entity, eg, from the submitting study or in systems link dbGaP
-- # Class: AccessPolicy_access_policy_code
--     * Slot: AccessPolicy_access_policy_id Description: Autocreated FK slot
--     * Slot: access_policy_code Description: A classification of the type of consents found in a consent statement.
-- # Class: AgeAt_external_id
--     * Slot: AgeAt_id Description: Autocreated FK slot
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
-- # Class: AssociatedParty_external_id
--     * Slot: AssociatedParty_id Description: Autocreated FK slot
--     * Slot: external_id Description: Other identifiers for this entity, eg, from the submitting study or in systems link dbGaP
-- # Class: Institution_external_id
--     * Slot: Institution_institution_id Description: Autocreated FK slot
--     * Slot: external_id Description: Other identifiers for this entity, eg, from the submitting study or in systems link dbGaP
-- # Class: Participant_race
--     * Slot: Participant_participant_id Description: Autocreated FK slot
--     * Slot: race Description: Reported race as defined by the 1997 OMB directives.
-- # Class: Participant_sample_id
--     * Slot: Participant_participant_id Description: Autocreated FK slot
--     * Slot: sample_id_sample_id Description: Samples associated with this participant
-- # Class: Participant_external_id
--     * Slot: Participant_participant_id Description: Autocreated FK slot
--     * Slot: external_id Description: Other identifiers for this entity, eg, from the submitting study or in systems link dbGaP
-- # Class: Person_participant_id
--     * Slot: Person_person_id Description: Autocreated FK slot
--     * Slot: participant_id_participant_id Description: The Global ID for the Participant
-- # Class: StudyMembership_participant_id
--     * Slot: StudyMembership_study_membership_id Description: Autocreated FK slot
--     * Slot: participant_id_participant_id Description: The Global ID for the Participant
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
-- # Class: ResearchStudy_study_membership_id
--     * Slot: ResearchStudy_research_study_id Description: Autocreated FK slot
--     * Slot: study_membership_id Description: Study Membership Global ID (group)
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
-- # Class: Sample_processing
--     * Slot: Sample_sample_id Description: Autocreated FK slot
--     * Slot: processing Description: Processing that was applied to the Parent Sample or from the Biospecimen Collection that yielded this distinct sample
-- # Class: Sample_external_id
--     * Slot: Sample_sample_id Description: Autocreated FK slot
--     * Slot: external_id Description: Other identifiers for this entity, eg, from the submitting study or in systems link dbGaP
-- # Class: Aliquot_external_id
--     * Slot: Aliquot_aliquot_id Description: Autocreated FK slot
--     * Slot: external_id Description: Other identifiers for this entity, eg, from the submitting study or in systems link dbGaP
-- # Class: NCPIFile_file_location_id
--     * Slot: NCPIFile_file_global_id Description: Autocreated FK slot
--     * Slot: file_location_id_file_location_id Description: Location details (this is not a global ID)
-- # Class: NCPIFile_file_meta_data_id
--     * Slot: NCPIFile_file_global_id Description: Autocreated FK slot
--     * Slot: file_meta_data_id_file_meta_data_id Description: Representation of file metadata for NCPI
-- # Class: NCPIFile_external_id
--     * Slot: NCPIFile_file_global_id Description: Autocreated FK slot
--     * Slot: external_id Description: Other identifiers for this entity, eg, from the submitting study or in systems link dbGaP
-- # Class: FileMetaData_samples
--     * Slot: FileMetaData_file_meta_data_id Description: Autocreated FK slot
--     * Slot: samples_sample_id Description: e.g., Reference(sample)
-- # Class: Family_external_id
--     * Slot: Family_family_global_id Description: Autocreated FK slot
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
	access_policy_id TEXT NOT NULL,
	description TEXT,
	data_access_type VARCHAR(14) NOT NULL,
	website TEXT,
	consent_scope VARCHAR(15) NOT NULL,
	disease_limitation TEXT,
	status VARCHAR(16) NOT NULL,
	PRIMARY KEY (access_policy_id)
);CREATE INDEX "ix_AccessPolicy_access_policy_id" ON "AccessPolicy" (access_policy_id);
CREATE TABLE "RelativeDateTime" (
	id TEXT NOT NULL,
	"offset" INTEGER NOT NULL,
	offset_end INTEGER,
	offset_type VARCHAR(5) NOT NULL,
	PRIMARY KEY (id)
);CREATE INDEX "ix_RelativeDateTime_id" ON "RelativeDateTime" (id);
CREATE TABLE "Institution" (
	institution_id TEXT NOT NULL,
	name TEXT,
	PRIMARY KEY (institution_id)
);CREATE INDEX "ix_Institution_institution_id" ON "Institution" (institution_id);
CREATE TABLE "Person" (
	person_id TEXT NOT NULL,
	PRIMARY KEY (person_id)
);CREATE INDEX "ix_Person_person_id" ON "Person" (person_id);
CREATE TABLE "Period" (
	period_id TEXT NOT NULL,
	start DATE,
	"end" DATE,
	PRIMARY KEY (period_id)
);CREATE INDEX "ix_Period_period_id" ON "Period" (period_id);
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
CREATE TABLE "FileMetaData" (
	file_meta_data_id TEXT NOT NULL,
	meta_data_type VARCHAR(10) NOT NULL,
	assay_strategy TEXT NOT NULL,
	platform_instrument TEXT NOT NULL,
	library_prep TEXT,
	library_selection TEXT,
	strandedness TEXT,
	target_region TEXT,
	is_paired_end TEXT,
	adaptor_trimmed TEXT,
	reference_genome TEXT,
	workflow_type TEXT,
	workflow_tool TEXT,
	PRIMARY KEY (file_meta_data_id)
);CREATE INDEX "ix_FileMetaData_file_meta_data_id" ON "FileMetaData" (file_meta_data_id);
CREATE TABLE "Family" (
	family_global_id TEXT NOT NULL,
	family_id TEXT NOT NULL,
	family_type VARCHAR(12) NOT NULL,
	description TEXT,
	consanguinity VARCHAR(13),
	family_focus TEXT,
	PRIMARY KEY (family_global_id)
);CREATE INDEX "ix_Family_family_global_id" ON "Family" (family_global_id);
CREATE TABLE "AgeAt" (
	value_type VARCHAR(9) NOT NULL,
	age TEXT,
	age_code TEXT,
	as_date DATE,
	id TEXT NOT NULL,
	PRIMARY KEY (id),
	FOREIGN KEY(age) REFERENCES "RelativeDateTime" (id)
);CREATE INDEX "ix_AgeAt_id" ON "AgeAt" (id);
CREATE TABLE "Participant" (
	participant_id TEXT NOT NULL,
	birthsex VARCHAR(6),
	ethnicity VARCHAR(22) NOT NULL,
	population VARCHAR,
	dob TEXT,
	dob_method VARCHAR(11),
	age_at_last_vital TEXT,
	is_deceased BOOLEAN,
	deceased_rel TEXT,
	patient_knowledge_source VARCHAR(11),
	family_global_id TEXT,
	PRIMARY KEY (participant_id),
	FOREIGN KEY(deceased_rel) REFERENCES "RelativeDateTime" (id),
	FOREIGN KEY(family_global_id) REFERENCES "Family" (family_global_id)
);CREATE INDEX "ix_Participant_participant_id" ON "Participant" (participant_id);
CREATE TABLE "PractitionerRole" (
	institution_id TEXT,
	practitioner_id TEXT,
	period_id TEXT,
	practitioner_role_id TEXT NOT NULL,
	PRIMARY KEY (practitioner_role_id),
	FOREIGN KEY(institution_id) REFERENCES "Institution" (institution_id),
	FOREIGN KEY(period_id) REFERENCES "Period" (period_id)
);CREATE INDEX "ix_PractitionerRole_practitioner_role_id" ON "PractitionerRole" (practitioner_role_id);
CREATE TABLE "StudyMembership" (
	study_membership_id TEXT NOT NULL,
	access_policy_id TEXT NOT NULL,
	PRIMARY KEY (study_membership_id),
	FOREIGN KEY(access_policy_id) REFERENCES "AccessPolicy" (access_policy_id)
);CREATE INDEX "ix_StudyMembership_study_membership_id" ON "StudyMembership" (study_membership_id);
CREATE TABLE "FileLocation" (
	file_location_id TEXT NOT NULL,
	location_uri TEXT NOT NULL,
	file_name TEXT NOT NULL,
	access_policy_id TEXT NOT NULL,
	PRIMARY KEY (file_location_id),
	FOREIGN KEY(access_policy_id) REFERENCES "AccessPolicy" (access_policy_id)
);CREATE INDEX "ix_FileLocation_file_location_id" ON "FileLocation" (file_location_id);
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
);CREATE INDEX "ix_Record_external_id_external_id" ON "Record_external_id" (external_id);CREATE INDEX "ix_Record_external_id_Record_id" ON "Record_external_id" ("Record_id");
CREATE TABLE "AccessPolicy_access_policy_code" (
	"AccessPolicy_access_policy_id" TEXT,
	access_policy_code VARCHAR(11) NOT NULL,
	PRIMARY KEY ("AccessPolicy_access_policy_id", access_policy_code),
	FOREIGN KEY("AccessPolicy_access_policy_id") REFERENCES "AccessPolicy" (access_policy_id)
);CREATE INDEX "ix_AccessPolicy_access_policy_code_AccessPolicy_access_policy_id" ON "AccessPolicy_access_policy_code" ("AccessPolicy_access_policy_id");CREATE INDEX "ix_AccessPolicy_access_policy_code_access_policy_code" ON "AccessPolicy_access_policy_code" (access_policy_code);
CREATE TABLE "Institution_external_id" (
	"Institution_institution_id" TEXT,
	external_id TEXT,
	PRIMARY KEY ("Institution_institution_id", external_id),
	FOREIGN KEY("Institution_institution_id") REFERENCES "Institution" (institution_id)
);CREATE INDEX "ix_Institution_external_id_external_id" ON "Institution_external_id" (external_id);CREATE INDEX "ix_Institution_external_id_Institution_institution_id" ON "Institution_external_id" ("Institution_institution_id");
CREATE TABLE "ResearchStudy_study_focus" (
	"ResearchStudy_research_study_id" TEXT,
	study_focus TEXT,
	PRIMARY KEY ("ResearchStudy_research_study_id", study_focus),
	FOREIGN KEY("ResearchStudy_research_study_id") REFERENCES "ResearchStudy" (research_study_id)
);CREATE INDEX "ix_ResearchStudy_study_focus_study_focus" ON "ResearchStudy_study_focus" (study_focus);CREATE INDEX "ix_ResearchStudy_study_focus_ResearchStudy_research_study_id" ON "ResearchStudy_study_focus" ("ResearchStudy_research_study_id");
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
);CREATE INDEX "ix_ResearchStudy_study_acknowledgement_study_acknowledgement" ON "ResearchStudy_study_acknowledgement" (study_acknowledgement);CREATE INDEX "ix_ResearchStudy_study_acknowledgement_ResearchStudy_research_study_id" ON "ResearchStudy_study_acknowledgement" ("ResearchStudy_research_study_id");
CREATE TABLE "ResearchStudy_study_design" (
	"ResearchStudy_research_study_id" TEXT,
	study_design TEXT,
	PRIMARY KEY ("ResearchStudy_research_study_id", study_design),
	FOREIGN KEY("ResearchStudy_research_study_id") REFERENCES "ResearchStudy" (research_study_id)
);CREATE INDEX "ix_ResearchStudy_study_design_study_design" ON "ResearchStudy_study_design" (study_design);CREATE INDEX "ix_ResearchStudy_study_design_ResearchStudy_research_study_id" ON "ResearchStudy_study_design" ("ResearchStudy_research_study_id");
CREATE TABLE "ResearchStudy_study_membership_id" (
	"ResearchStudy_research_study_id" TEXT,
	study_membership_id TEXT NOT NULL,
	PRIMARY KEY ("ResearchStudy_research_study_id", study_membership_id),
	FOREIGN KEY("ResearchStudy_research_study_id") REFERENCES "ResearchStudy" (research_study_id)
);CREATE INDEX "ix_ResearchStudy_study_membership_id_ResearchStudy_research_study_id" ON "ResearchStudy_study_membership_id" ("ResearchStudy_research_study_id");CREATE INDEX "ix_ResearchStudy_study_membership_id_study_membership_id" ON "ResearchStudy_study_membership_id" (study_membership_id);
CREATE TABLE "ResearchStudy_external_id" (
	"ResearchStudy_research_study_id" TEXT,
	external_id TEXT,
	PRIMARY KEY ("ResearchStudy_research_study_id", external_id),
	FOREIGN KEY("ResearchStudy_research_study_id") REFERENCES "ResearchStudy" (research_study_id)
);CREATE INDEX "ix_ResearchStudy_external_id_external_id" ON "ResearchStudy_external_id" (external_id);CREATE INDEX "ix_ResearchStudy_external_id_ResearchStudy_research_study_id" ON "ResearchStudy_external_id" ("ResearchStudy_research_study_id");
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
);CREATE INDEX "ix_ResearchStudyCollection_external_id_external_id" ON "ResearchStudyCollection_external_id" (external_id);CREATE INDEX "ix_ResearchStudyCollection_external_id_ResearchStudyCollection_research_study_collection_id" ON "ResearchStudyCollection_external_id" ("ResearchStudyCollection_research_study_collection_id");
CREATE TABLE "Family_external_id" (
	"Family_family_global_id" TEXT,
	external_id TEXT,
	PRIMARY KEY ("Family_family_global_id", external_id),
	FOREIGN KEY("Family_family_global_id") REFERENCES "Family" (family_global_id)
);CREATE INDEX "ix_Family_external_id_external_id" ON "Family_external_id" (external_id);CREATE INDEX "ix_Family_external_id_Family_family_global_id" ON "Family_external_id" ("Family_family_global_id");
CREATE TABLE "ParticipantAssertion" (
	participant_id TEXT NOT NULL,
	age_at_event TEXT,
	age_at_assertion TEXT,
	age_at_onset TEXT,
	age_at_resolution TEXT,
	entity_asserter VARCHAR(11),
	other_condition_modifiers TEXT,
	assertion_type VARCHAR(18) NOT NULL,
	assertion_code TEXT NOT NULL,
	assertion_text TEXT,
	assertion_source TEXT,
	value_code TEXT,
	value_string TEXT,
	value_number FLOAT,
	value_units TEXT,
	body_site TEXT,
	body_location TEXT,
	body_laterality TEXT,
	cancer_stage TEXT,
	participant_assertion_id TEXT NOT NULL,
	PRIMARY KEY (participant_assertion_id),
	FOREIGN KEY(participant_id) REFERENCES "Participant" (participant_id),
	FOREIGN KEY(age_at_event) REFERENCES "AgeAt" (id),
	FOREIGN KEY(age_at_assertion) REFERENCES "AgeAt" (id),
	FOREIGN KEY(age_at_onset) REFERENCES "AgeAt" (id),
	FOREIGN KEY(age_at_resolution) REFERENCES "AgeAt" (id)
);CREATE INDEX "ix_ParticipantAssertion_participant_assertion_id" ON "ParticipantAssertion" (participant_assertion_id);
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
CREATE TABLE "Sample" (
	sample_id TEXT NOT NULL,
	parent_sample_id TEXT,
	participant_id TEXT NOT NULL,
	sample_type TEXT NOT NULL,
	age_at_collection TEXT,
	collection_method TEXT,
	collection_site TEXT,
	spatial_qualifier TEXT,
	laterality TEXT,
	availability_status VARCHAR(11),
	storage_method TEXT,
	quantity FLOAT,
	quantity_units TEXT,
	PRIMARY KEY (sample_id),
	FOREIGN KEY(parent_sample_id) REFERENCES "Sample" (sample_id),
	FOREIGN KEY(participant_id) REFERENCES "Participant" (participant_id),
	FOREIGN KEY(age_at_collection) REFERENCES "AgeAt" (id)
);CREATE INDEX "ix_Sample_sample_id" ON "Sample" (sample_id);
CREATE TABLE "NCPIFile" (
	participant_id TEXT NOT NULL,
	file_format TEXT NOT NULL,
	file_size FLOAT NOT NULL,
	file_size_unit TEXT NOT NULL,
	content_version TEXT,
	file_type TEXT NOT NULL,
	file_hash TEXT NOT NULL,
	file_hash_type TEXT,
	description TEXT,
	file_global_id TEXT NOT NULL,
	PRIMARY KEY (file_global_id),
	FOREIGN KEY(participant_id) REFERENCES "Participant" (participant_id)
);CREATE INDEX "ix_NCPIFile_file_global_id" ON "NCPIFile" (file_global_id);
CREATE TABLE "FamilyRelationship" (
	family_relationship_id TEXT NOT NULL,
	patient_id TEXT NOT NULL,
	relative_id TEXT NOT NULL,
	relationship VARCHAR(16) NOT NULL,
	knowledge_source VARCHAR(11) NOT NULL,
	PRIMARY KEY (family_relationship_id),
	FOREIGN KEY(patient_id) REFERENCES "Participant" (participant_id),
	FOREIGN KEY(relative_id) REFERENCES "Participant" (participant_id)
);CREATE INDEX "ix_FamilyRelationship_family_relationship_id" ON "FamilyRelationship" (family_relationship_id);
CREATE TABLE "AgeAt_external_id" (
	"AgeAt_id" TEXT,
	external_id TEXT,
	PRIMARY KEY ("AgeAt_id", external_id),
	FOREIGN KEY("AgeAt_id") REFERENCES "AgeAt" (id)
);CREATE INDEX "ix_AgeAt_external_id_external_id" ON "AgeAt_external_id" (external_id);CREATE INDEX "ix_AgeAt_external_id_AgeAt_id" ON "AgeAt_external_id" ("AgeAt_id");
CREATE TABLE "Participant_race" (
	"Participant_participant_id" TEXT,
	race VARCHAR(35) NOT NULL,
	PRIMARY KEY ("Participant_participant_id", race),
	FOREIGN KEY("Participant_participant_id") REFERENCES "Participant" (participant_id)
);CREATE INDEX "ix_Participant_race_race" ON "Participant_race" (race);CREATE INDEX "ix_Participant_race_Participant_participant_id" ON "Participant_race" ("Participant_participant_id");
CREATE TABLE "Participant_external_id" (
	"Participant_participant_id" TEXT,
	external_id TEXT,
	PRIMARY KEY ("Participant_participant_id", external_id),
	FOREIGN KEY("Participant_participant_id") REFERENCES "Participant" (participant_id)
);CREATE INDEX "ix_Participant_external_id_external_id" ON "Participant_external_id" (external_id);CREATE INDEX "ix_Participant_external_id_Participant_participant_id" ON "Participant_external_id" ("Participant_participant_id");
CREATE TABLE "Person_participant_id" (
	"Person_person_id" TEXT,
	participant_id_participant_id TEXT NOT NULL,
	PRIMARY KEY ("Person_person_id", participant_id_participant_id),
	FOREIGN KEY("Person_person_id") REFERENCES "Person" (person_id),
	FOREIGN KEY(participant_id_participant_id) REFERENCES "Participant" (participant_id)
);CREATE INDEX "ix_Person_participant_id_Person_person_id" ON "Person_participant_id" ("Person_person_id");CREATE INDEX "ix_Person_participant_id_participant_id_participant_id" ON "Person_participant_id" (participant_id_participant_id);
CREATE TABLE "StudyMembership_participant_id" (
	"StudyMembership_study_membership_id" TEXT,
	participant_id_participant_id TEXT NOT NULL,
	PRIMARY KEY ("StudyMembership_study_membership_id", participant_id_participant_id),
	FOREIGN KEY("StudyMembership_study_membership_id") REFERENCES "StudyMembership" (study_membership_id),
	FOREIGN KEY(participant_id_participant_id) REFERENCES "Participant" (participant_id)
);CREATE INDEX "ix_StudyMembership_participant_id_StudyMembership_study_membership_id" ON "StudyMembership_participant_id" ("StudyMembership_study_membership_id");CREATE INDEX "ix_StudyMembership_participant_id_participant_id_participant_id" ON "StudyMembership_participant_id" (participant_id_participant_id);
CREATE TABLE "AssociatedParty" (
	name TEXT,
	role VARCHAR(20),
	associated_party_practitioner_id TEXT,
	associated_party_practitioner_role_id TEXT,
	associated_party_institution_id TEXT,
	id TEXT NOT NULL,
	PRIMARY KEY (id),
	FOREIGN KEY(associated_party_practitioner_id) REFERENCES "Practitioner" (practitioner_id),
	FOREIGN KEY(associated_party_practitioner_role_id) REFERENCES "PractitionerRole" (practitioner_role_id),
	FOREIGN KEY(associated_party_institution_id) REFERENCES "PractitionerRole" (practitioner_role_id)
);CREATE INDEX "ix_AssociatedParty_id" ON "AssociatedParty" (id);
CREATE TABLE "Aliquot" (
	aliquot_id TEXT NOT NULL,
	availability_status VARCHAR(11),
	volume FLOAT,
	volume_units TEXT,
	concentration TEXT,
	sample_id TEXT NOT NULL,
	PRIMARY KEY (aliquot_id),
	FOREIGN KEY(sample_id) REFERENCES "Sample" (sample_id)
);CREATE INDEX "ix_Aliquot_aliquot_id" ON "Aliquot" (aliquot_id);
CREATE TABLE "Practitioner_external_id" (
	"Practitioner_practitioner_id" TEXT,
	external_id TEXT,
	PRIMARY KEY ("Practitioner_practitioner_id", external_id),
	FOREIGN KEY("Practitioner_practitioner_id") REFERENCES "Practitioner" (practitioner_id)
);CREATE INDEX "ix_Practitioner_external_id_external_id" ON "Practitioner_external_id" (external_id);CREATE INDEX "ix_Practitioner_external_id_Practitioner_practitioner_id" ON "Practitioner_external_id" ("Practitioner_practitioner_id");
CREATE TABLE "Participant_sample_id" (
	"Participant_participant_id" TEXT,
	sample_id_sample_id TEXT,
	PRIMARY KEY ("Participant_participant_id", sample_id_sample_id),
	FOREIGN KEY("Participant_participant_id") REFERENCES "Participant" (participant_id),
	FOREIGN KEY(sample_id_sample_id) REFERENCES "Sample" (sample_id)
);CREATE INDEX "ix_Participant_sample_id_sample_id_sample_id" ON "Participant_sample_id" (sample_id_sample_id);CREATE INDEX "ix_Participant_sample_id_Participant_participant_id" ON "Participant_sample_id" ("Participant_participant_id");
CREATE TABLE "Sample_processing" (
	"Sample_sample_id" TEXT,
	processing TEXT,
	PRIMARY KEY ("Sample_sample_id", processing),
	FOREIGN KEY("Sample_sample_id") REFERENCES "Sample" (sample_id)
);CREATE INDEX "ix_Sample_processing_processing" ON "Sample_processing" (processing);CREATE INDEX "ix_Sample_processing_Sample_sample_id" ON "Sample_processing" ("Sample_sample_id");
CREATE TABLE "Sample_external_id" (
	"Sample_sample_id" TEXT,
	external_id TEXT,
	PRIMARY KEY ("Sample_sample_id", external_id),
	FOREIGN KEY("Sample_sample_id") REFERENCES "Sample" (sample_id)
);CREATE INDEX "ix_Sample_external_id_external_id" ON "Sample_external_id" (external_id);CREATE INDEX "ix_Sample_external_id_Sample_sample_id" ON "Sample_external_id" ("Sample_sample_id");
CREATE TABLE "NCPIFile_file_location_id" (
	"NCPIFile_file_global_id" TEXT,
	file_location_id_file_location_id TEXT NOT NULL,
	PRIMARY KEY ("NCPIFile_file_global_id", file_location_id_file_location_id),
	FOREIGN KEY("NCPIFile_file_global_id") REFERENCES "NCPIFile" (file_global_id),
	FOREIGN KEY(file_location_id_file_location_id) REFERENCES "FileLocation" (file_location_id)
);CREATE INDEX "ix_NCPIFile_file_location_id_file_location_id_file_location_id" ON "NCPIFile_file_location_id" (file_location_id_file_location_id);CREATE INDEX "ix_NCPIFile_file_location_id_NCPIFile_file_global_id" ON "NCPIFile_file_location_id" ("NCPIFile_file_global_id");
CREATE TABLE "NCPIFile_file_meta_data_id" (
	"NCPIFile_file_global_id" TEXT,
	file_meta_data_id_file_meta_data_id TEXT,
	PRIMARY KEY ("NCPIFile_file_global_id", file_meta_data_id_file_meta_data_id),
	FOREIGN KEY("NCPIFile_file_global_id") REFERENCES "NCPIFile" (file_global_id),
	FOREIGN KEY(file_meta_data_id_file_meta_data_id) REFERENCES "FileMetaData" (file_meta_data_id)
);CREATE INDEX "ix_NCPIFile_file_meta_data_id_file_meta_data_id_file_meta_data_id" ON "NCPIFile_file_meta_data_id" (file_meta_data_id_file_meta_data_id);CREATE INDEX "ix_NCPIFile_file_meta_data_id_NCPIFile_file_global_id" ON "NCPIFile_file_meta_data_id" ("NCPIFile_file_global_id");
CREATE TABLE "NCPIFile_external_id" (
	"NCPIFile_file_global_id" TEXT,
	external_id TEXT,
	PRIMARY KEY ("NCPIFile_file_global_id", external_id),
	FOREIGN KEY("NCPIFile_file_global_id") REFERENCES "NCPIFile" (file_global_id)
);CREATE INDEX "ix_NCPIFile_external_id_external_id" ON "NCPIFile_external_id" (external_id);CREATE INDEX "ix_NCPIFile_external_id_NCPIFile_file_global_id" ON "NCPIFile_external_id" ("NCPIFile_file_global_id");
CREATE TABLE "FileMetaData_samples" (
	"FileMetaData_file_meta_data_id" TEXT,
	samples_sample_id TEXT,
	PRIMARY KEY ("FileMetaData_file_meta_data_id", samples_sample_id),
	FOREIGN KEY("FileMetaData_file_meta_data_id") REFERENCES "FileMetaData" (file_meta_data_id),
	FOREIGN KEY(samples_sample_id) REFERENCES "Sample" (sample_id)
);CREATE INDEX "ix_FileMetaData_samples_samples_sample_id" ON "FileMetaData_samples" (samples_sample_id);CREATE INDEX "ix_FileMetaData_samples_FileMetaData_file_meta_data_id" ON "FileMetaData_samples" ("FileMetaData_file_meta_data_id");
CREATE TABLE "AssociatedParty_period_id" (
	"AssociatedParty_id" TEXT,
	period_id_period_id TEXT,
	PRIMARY KEY ("AssociatedParty_id", period_id_period_id),
	FOREIGN KEY("AssociatedParty_id") REFERENCES "AssociatedParty" (id),
	FOREIGN KEY(period_id_period_id) REFERENCES "Period" (period_id)
);CREATE INDEX "ix_AssociatedParty_period_id_period_id_period_id" ON "AssociatedParty_period_id" (period_id_period_id);CREATE INDEX "ix_AssociatedParty_period_id_AssociatedParty_id" ON "AssociatedParty_period_id" ("AssociatedParty_id");
CREATE TABLE "AssociatedParty_classifier" (
	"AssociatedParty_id" TEXT,
	classifier VARCHAR(10),
	PRIMARY KEY ("AssociatedParty_id", classifier),
	FOREIGN KEY("AssociatedParty_id") REFERENCES "AssociatedParty" (id)
);CREATE INDEX "ix_AssociatedParty_classifier_classifier" ON "AssociatedParty_classifier" (classifier);CREATE INDEX "ix_AssociatedParty_classifier_AssociatedParty_id" ON "AssociatedParty_classifier" ("AssociatedParty_id");
CREATE TABLE "AssociatedParty_external_id" (
	"AssociatedParty_id" TEXT,
	external_id TEXT,
	PRIMARY KEY ("AssociatedParty_id", external_id),
	FOREIGN KEY("AssociatedParty_id") REFERENCES "AssociatedParty" (id)
);CREATE INDEX "ix_AssociatedParty_external_id_external_id" ON "AssociatedParty_external_id" (external_id);CREATE INDEX "ix_AssociatedParty_external_id_AssociatedParty_id" ON "AssociatedParty_external_id" ("AssociatedParty_id");
CREATE TABLE "ResearchStudy_study_personnel" (
	"ResearchStudy_research_study_id" TEXT,
	study_personnel_id TEXT NOT NULL,
	PRIMARY KEY ("ResearchStudy_research_study_id", study_personnel_id),
	FOREIGN KEY("ResearchStudy_research_study_id") REFERENCES "ResearchStudy" (research_study_id),
	FOREIGN KEY(study_personnel_id) REFERENCES "AssociatedParty" (id)
);CREATE INDEX "ix_ResearchStudy_study_personnel_ResearchStudy_research_study_id" ON "ResearchStudy_study_personnel" ("ResearchStudy_research_study_id");CREATE INDEX "ix_ResearchStudy_study_personnel_study_personnel_id" ON "ResearchStudy_study_personnel" (study_personnel_id);
CREATE TABLE "Aliquot_external_id" (
	"Aliquot_aliquot_id" TEXT,
	external_id TEXT,
	PRIMARY KEY ("Aliquot_aliquot_id", external_id),
	FOREIGN KEY("Aliquot_aliquot_id") REFERENCES "Aliquot" (aliquot_id)
);CREATE INDEX "ix_Aliquot_external_id_external_id" ON "Aliquot_external_id" (external_id);CREATE INDEX "ix_Aliquot_external_id_Aliquot_aliquot_id" ON "Aliquot_external_id" ("Aliquot_aliquot_id");
