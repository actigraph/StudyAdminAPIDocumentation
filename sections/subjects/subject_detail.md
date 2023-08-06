[<< Back to Subjects](/sections/subjects.md)

Subject Details and Subject Listing
===

Subject Listing
---


Returns a list of all subjects within a given study. To retrieve a listing of studies refer to the [List Studies](/sections/studies.md#list-studies) API call.

**Request:**

    GET /v1/studies/{StudyId}/subjects

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
            "HeightCm": 299.99,
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
            "HeightCm": 199.99,
            "DataCollectionStatus": "No Device Assigned",
            "DeviceSerial": null
        },
        ...
    ]

**Response Properties**

Field|Type|Accepted Values|Description|Notes
-----|----|----------|-----|-----
Id|Number||System-wide primary Key of subject data record (aka as 'SubjectId')||
Subject Identifier|String||Study-specific Subject Identifier that is unique within the context of a study.|The `SubjectIdentifier` field is prefixed with the subject's site identifier (if it exists). For example, a subject with a "001" identifier in a site with a "333" identifier should denote "333001".
DOB|ISO8601 Date||Subject's Date of Birth||
Gender|String|<ul><li>Male</li><li>Female</li></ul>|||
Timezone|String||The Subject's timezone identifier from the IANA Timezone database|To view list of ALL IANA timezones goto: https://en.wikipedia.org/wiki/List_of_tz_database_time_zones|
Wear Position|String|<ul><li>Non-Dominant Wrist</li><li>Dominant Wrist</li><li>Left Non-Dominant Wrist</li><li>Left Dominant Wrist</li><li>Right Non-Dominant Wrist</li><li>Right Dominant Wrist</li><li>Waist</li><li>Left Wrist</li><li>Right Wrist</li><li>Ankle</li></ul>|| 
WeightLbs|Decimal||Weight ranges between 0 lbs to 2000 lbs||
HeightCm|Decimal||Height ranges between 0 cm to 300 cm||
Data Collection Status|String|<ul><li>No Device Assigned</li><li>Incomplete Assignment</li><li>Collecting</li><li>Collection Stopped</li></ul>|||
Device Serial|String||The serial number of the activity monitor that is actively assigned to subject.|If subject is not assigned to a monitor, this field will be set to `null`.|

GET Subject Details (by system-wide primary key)
---
Returns information about a given subject from the internal system-wide primary key.

**Request:**

    GET /v1/subjects/{SubjectId}

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
        "HeightCm": 199.99,
        "DataCollectionStatus": "Collecting",      
        "DeviceSerial": "TAS1D48341371"
    }

GET Subject Details (by study-specific subject identifier)
---

Returns subject(s) within given study with study-specific subject identifier. The subject identifier is required field when creating subject data records in the CentrePoint system. To retrieve a listing of studies refer to the [List Studies](/sections/studies.md#list-studies) API call.

**Request:**

    GET /v1/studies/{StudyId}/subjectsbyidentifier/{SubjectIdentifier}

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
            "HeightCm": 199.99,
            "DataCollectionStatus": "Collecting",      
            "DeviceSerial": "TAS1D48341371"
        }
    ]


