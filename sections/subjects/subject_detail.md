[<< Back to Subjects](/sections/subjects.md)

Subject Detail and Subject Listing
===

Subject Listing
---


Returns a list of all subjects within a given study.

**Request:**

    GET /v1/studies/{studyId}/subjects

**Response:**

    [
        {
            "Id":123,
            "SubjectIdentifier": "013001",
            "SiteId": 456,
            "DOB": "1974-02-11T00:00:00",
            "Gender": "Male",
            "Timezone": "US/CENTRAL",
            "WearPosition": "Left Wrist",
            "WeightLbs": 120.00,
            "DataCollectionStatus": "Collecting",      
            "DeviceSerial": "TAS1D48341371"
        },
        {
            "Id":125,
            "SubjectIdentifier": "013002",
            "SiteId": 456,
            "DOB": "1988-07-14T00:00:00",
            "Gender": "Male",
            "Timezone": "US/CENTRAL",
            "WearPosition": "Right Wrist",
            "WeightLbs": 150.00,
            "DataCollectionStatus": "No Device Assigned",
            "DeviceSerial": null
        },
        ...
    ]

**Response Properties**

Field|Type|Accepted Values|Description|Notes
-----|----|----------|-----|-----
Id|Number||Primary Key of Subject Id||
Subject Identifier|String||User-specified Subject Identifier that is unique within the study.|The `SubjectIdentifier` field is prefixed with the subject's site identifier (if it exists). For example, a subject with a "001" identifier in a site with a "333" identifier should denote "333001".
DOB|ISO8601 Date||Subject's Date of Birth||
Gender|String|<ul><li>Male</li><li>Female</li></ul>|||
Timezone|String||Subject's Timezone||
Wear Position|String|<ul><li>Non-Dominant Wrist</li><li>Dominant Wrist</li><li>Left Non-Dominant Wrist</li><li>Left Dominant Wrist</li><li>Right Non-Dominant Wrist</li><li>Right Dominant Wrist</li><li>Waist</li><li>Left Wrist</li><li>Right Wrist</li><li>Ankle</li></ul>|| 
Data Collection Status|String|<ul><li>No Device Assigned</li><li>Incomplete Assignment</li><li>Collecting</li><li>Collection Stopped</li></ul>|||
Device Serial|String||The serial number of the activity monitor currently assigned to subject.|If subject is not assigned to a monitor, this field will be set to `null`.|

GET Subject Details (by Primary Key)
---
Returns information about a given subject.

**Request:**

    GET /v1/subjects/{id}

**Response:**

    {
        "Id":123,
        "SubjectIdentifier": "013001",
        "SiteId": 456,
        "DOB": "1974-02-11T00:00:00",
        "Gender": "Female",
        "Timezone": "US/CENTRAL",
        "WearPosition": "Left Wrist",
        "WeightLbs": "105.74",
        "DataCollectionStatus": "Collecting",      
        "DeviceSerial": "TAS1D48341371"
    }

GET Subject Details (by Study Identifier)
---

Returns one (or more) subjects (within requested study) with specific subject identifier. The subject identifier is required field when creating subject data records in the CentrePoint system.

**Request:**

    GET /v1/studies/{studyId}/subjectsbyidentifier/{subjectIdentifier}

**Notes:**  

* The {subjectIdentifier} field should always be **prefixed with the subject's site identifier** (if it exists). For example, a subject with a "001" identifier in a site with a "333" identifier should denote "333001". 
* For subjects in sites where the **site identifier is not set**, the {subjectIdentifier} should denote just the subject identifier without any prefix. For example, a subject with a "001" identifier in a site without a site identifier should denote "001". 
* For subjects where the identifier consists of space character, space characters should be replaced with "%20". For example, a subject with a "S123 AE" identifier should denote "S123%20AE".

**Response:**

    [
        {
            "Id":123,
            "SubjectIdentifier": "013001",
            "SiteId": 456,
            "DOB": "1974-02-11T00:00:00",
            "Gender": "Male",
            "Timezone": "US/CENTRAL",
            "WearPosition": "Left Wrist",
            "WeightLbs": 165.00,
            "DataCollectionStatus": "Collecting",      
            "DeviceSerial": "TAS1D48341371"
        }
    ]


