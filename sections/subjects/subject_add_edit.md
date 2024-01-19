[<< Back to Subjects](/sections/subjects.md)

## Add/Edit Subject and Assign/Un-assign Activity Monitor

===

### Include Subject Height & Height Unit (32714, 32715)

Height and height unit are included in the response when calling POST & PUT /v1/subjects.

### Add Subject (w/ Ability to Assign Activity Monitor)

---
Creates a new subject with option to assign an activity monitor to the newly created subject.  

Subjects are created within the context of a site, therefore the 'SiteId' property is required upon creating a new subject. The [List Sites](/sections/sites.md) API call will provide a listing of sites in which you have access to. 

The new Subject's Id is returned upon successful creation along with a 201 Created response.

**Request:**

    POST /v1/subjects
    Content-Type:application/json
    {
        "SubjectIdentifier": "000071",
        "SiteId": 224,
        "WearPosition": "Waist",
        "DOB": "1988-08-01",
        "Gender": "Male",
        "WeightLbs": "198",
        "DeviceSerial": "TAS1D48341371",
        "HeightCm": "180"
    }

**Request Properties**

Field|Type|Min|Max|Required|Accepted Values|Description|Notes
-----|----|---|---|--------|---------------|-----------|-----
DOB|ISO8601 Date||day before present day|Yes|||must be day before present day
Gender|String|||Yes|<ul><li>Male</li><li>Female</li></ul>||Study/site shall be configured to utilize this field
SiteId|Number|||Yes|||Site write access enforced. Therefore API user must have appropriate permissions to add subjects to given site.
SubjectIdentifier|String|||Yes||Study-specific subject identifier that is unique within study|Subject Identifier should NOT be prefixed with Site Identifier.|
WearPosition|String|||Yes|<ul><li>Non-Dominant Wrist</li><li>Dominant Wrist</li><li>Left Non-Dominant Wrist</li><li>Left Dominant Wrist</li><li>Right Non-Dominant Wrist</li><li>Right Dominant Wrist</li><li>Waist</li><li>Left Wrist</li><li>Right Wrist</li><li>Ankle</li></ul>||Study/site shall be configured in order to utilize this field
WeightLbs|Number|1|2000|Yes|||Study/site shall be configured to utilize this field
DeviceSerial|String|||No||Activity Monitor's serial number to assign to subject for data collection.|Study/site shall be configured in order to utilize this field. If blank or `null`, monitor assignment will not be attempted. Once monitor assignment is created, the monitor will need to be docked (via USB) to complete the assignment and begin data collection.<br /><br />To view listing of assignable activity monitors in your study, utilize the [List Study Devices](https://github.com/actigraph/StudyAdminAPIDocumentation/blob/master/sections/studies.md#study-devices) API call.
HeightCm|Number|1|300|Yes|||Study/site shall be configured to utilize this field

**Additional Notes** 

- Depending on the study/site configuration of subject being added, the **Gender**, **DOB**, **WeightLBS**, and/or **HeightCm** fields may or may not be allowed. If the fields are allowed, then they will be required. If not allowed, then these fields must be excluded from the JSON request.
- Depending on the study/site configuration of subject being added, the **WearPosition** may or may not limit to utilize only one of the following values: 
	- Left Non-Dominant Wrist
	- Right Non-Dominant Wrist
	- Left Dominant Wrist
	- Right Dominant Wrist
	- Non-Dominant Wrist
	- Dominant Wrist
	- Left Wrist
	- Right Wrist
	- Waist 
	- Ankle

- Depending on the study/site configuration of subject being added, the **DeviceSerial** may or may not be allowed in order to perform an activity monitor assignment to subject

**Response:**

    201 Created
    {
        "SubjectId":789
    }

### Edit Subject (w/ Ability to Assign Activity Monitor)

---
Modifies an existing subject with option to assign an activity monitor to existing subject.  The [List Sites](/sections/sites.md) API call will provide a listing of sites in which you have access to. A 200 OK response is returned for a successfully edited subject.

**Request:**

    PUT /v1/subjects
    Content-Type:application/json
    {
        "SubjectId" : 123,
        "SubjectIdentifier": "000071",
        "SiteId": 224,
        "WearPosition": "Waist",
        "DOB": "1988-08-01",
        "Gender": "Male",
        "WeightLbs": "198",
        "ChangeReason":"Performing monitor assignment to existing subject",
        "DeviceSerial": "TAS1D48341371",
        "HeightCm": "180"
    }

**Request Properties**

Field|Type|Min|Max|Required|Accepted Values|Description|Notes
-----|----|---|---|--------|---------------|-----------|-----
SubjectId|Number|||Yes||System-wide primary key of subject data record|Site write access enforced
SubjectIdentifier|String|||Yes||Study-specific subject identifier that is Unique within given study|
SiteId|Number|||Yes|||Site write access enforced
DOB|ISO8601 Date||day before present day|Yes||Subject's Date of Birth|must be day before present day
Gender|String|||Yes|<ul><li>Male</li><li>Female</li></ul>||Study/site shall be configured to utilize this field
WearPosition|String|||Yes|<ul><li>Non-Dominant Wrist</li><li>Dominant Wrist</li><li>Left Non-Dominant Wrist</li><li>Left Dominant Wrist</li><li>Right Non-Dominant Wrist</li><li>Right Dominant Wrist</li><li>Waist</li><li>Left Wrist</li><li>Right Wrist</li><li>Ankle</li></ul>||Study/site shall be configured to utilize this field
WeightLbs|Number|1|2000|Yes|||Study/site shall be configured to utilize this field
ChangeReason|String|||Yes|||Study/site shall be configured to utilize this field. Captured in operator audit record in accordance  with FDA 21 CFR Part 11. 
DeviceSerial|String|||No||Activity Monitor's serial number to assign to subject for data collection.|Study/site shall be configured in order to utilize this field. If blank or `null`, monitor assignment will not be attempted. Once assignment has been created, the activity monitor will need to be docked (via USB) to complete assignment and begin data collection.<br /><br />To view listing of assignable activity monitors in your study, utilize the [List Study Devices](https://github.com/actigraph/StudyAdminAPIDocumentation/blob/master/sections/studies.md#study-devices) API call.
HeightCm|Number|1|300|Yes|||Study/site shall be configured to utilize this field

**Additional Notes**

- Depending on the study/site configuration of subject being edited, the **Gender**, **DOB**,  **WeightLBS**, and/or **HeightCm** fields may or may not be allowed. If the fields are allowed, then they will be required. If not allowed, then these fields must be excluded from the JSON request.
- Depending on the study/site configuration of subject being edited, the **WearPosition** may or may not limit to utilize only one of the following values: 
  - Left Non-Dominant Wrist
  - Right Non-Dominant Wrist
  - Left Dominant Wrist
  - Right Dominant Wrist
  - Non-Dominant Wrist
  - Dominant Wrist
  - Left Wrist
  - Right Wrist
  - Waist
  - Ankle
- **ChangeReason** is required for all study configurations in CentrePoint created after 2017-11-30.
- Depending on the study/site configuration of subject being edited, the **DeviceSerial** may or may not be allowed in order to perform an activity monitor assignment to subject.

**Response:**

    200 OK

### Un-Assign Activity Monitor From Subject

---

Starts the process to un-assign an activity monitor from a given subject. The un-assignment is then completed upon "docking" the monitor (via USB).
  
**Request:**

PUT /v1/subjects/RemoveDeviceAssignment
   Content-Type:application/json
   {
      "SubjectId": 3792,
      "DeviceSerial": "TAS2A13510263"
   }

**Request Properties**

Field|Type|Required|Default Value|Description
-----|----|--------|-----------------|-------
SubjectId|number|yes||Subject's Primary Key in which API user wishes to stop activity monitor data collection
DeviceSerial|string|yes||Activity monitor serial in which to stop collecting data for given subject
ForcefullyEndAssignment|bool|no|`false`|Determines whether to forcefully un-assign monitor from subject without recovering any data on monitor

**Response:**

    200 OK
