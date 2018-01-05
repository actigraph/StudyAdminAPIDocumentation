Subjects
===

Study Subjects
---


Returns a list of all subjects within the requested study.

**Request:**

    GET /v1/studies/{studyId}/subjects

**Response:**

    [
        {
            "Id":123,
            "SubjectIdentifier": "013001",
            "DOB": "1974-02-11T00:00:00",
            "Gender": "Male",
            "Timezone": "(GMT -6:00) Central Time (US & Canada), Mexico City",
            "WearPosition": "Left Wrist",      
            "DataCollectionStatus": "Collecting",      
            "DeviceSerial": "TAS1D48341371"
        },
        {
            "Id":125,
            "SubjectIdentifier": "013002",
            "DOB": "1988-07-14T00:00:00",
            "Gender": "Male",
            "Timezone": "(GMT -6:00) Central Time (US & Canada), Mexico City",
            "WearPosition": "Right Wrist",
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
Wear Position|String|<ul><li>Left Wrist</li><li>Right Wrist</li><li>Waist</li></ul>|| 
Data Collection Status|String|<ul><li>No Device Assigned</li><li>Collecting</li><li>Collection Stopped</li></ul>|||
Device Serial|String||The serial number of the activity monitor currently assigned to subject.|If subject is not assigned to a monitor, this field will be set to `null`.|

Subject Details
---
Returns detailed information about the requested subject.

**Request:**

    GET /v1/subjects/{id}

**Response:**

    {
        "Id":123,
        "SubjectIdentifier": "013001",
        "DOB": "1974-02-11T00:00:00",
        "Gender": "Female",
        "Timezone": "(GMT -6:00) Central Time (US & Canada), Mexico City",
        "WearPosition": "Left Wrist",
        "WeightLbs": "105.74",
 	"DataCollectionStatus": "Collecting",      
        "DeviceSerial": "TAS1D48341371"
    }

Subject(s) By Identifier
---

Returns one or more subjects (within requested study) with specific subject identifier. The subject identifer is required field when creating subject data records in the CentrePoint system.

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
            "DOB": "1974-02-11T00:00:00",
            "Gender": "Male",
            "Timezone": "(GMT -6:00) Central Time (US & Canada), Mexico City",
            "WearPosition": "Left Wrist",      
            "DataCollectionStatus": "Collecting",      
            "DeviceSerial": "TAS1D48341371"
        }
    ]


Add Subject
---
Creates a new subject.  Subjects are created at the site level.  List sites to find out which you can access.  You must have CanAddSubjects=true for a Site in order to create a subject in it.  The new Subject's Id is returned upon successful creation along with a 201 Created response.

### Request: ###

    POST /v1/subjects
    Content-Type:application/json
    {
        "SubjectIdentifier": "000071",
        "SiteId": 224,
        "WearPosition": "Waist",
        "DOB": "1988-08-01",
        "Gender": "Male",
        "WeightLbs": "198",
	"DeviceSerial": "TAS1D48341371"
    }



**Request Properties**


Field|Type|Min|Max|Required|Accepted Values|Description|Notes
-----|----|---|---|--------|---------------|-----------|-----
DOB|ISO8601 Date||day before present day|Yes|||must be day before present day
Gender|String|||Yes|<ul><li>Male</li><li>Female</li></ul>||Study/site shall be configured to utilize this field
SiteId|Number|||Yes|||Site write access enforced. Therefore API user must have appropriate permissions to add subjects to given site.
SubjectIdentifier|String|||Yes||User specified Subject Identifier that is unique within study|Subject Identifier should NOT be prefixed with Site Identifier.|
WearPosition|String|||Yes|<ul><li>Left Wrist</li><li>Right Wrist</li><li>Waist</li></ul>||Study/site shall be configured in order to utilize this field
WeightLbs|Number|1|2000|Yes|||Study/site shall be configured to utilize this field
DeviceSerial|String|||No||Activity Monitor's serial number to assign to subject for data collection.|Study/site shall be configured in order to utilize this field. If blank or `null`, monitor assignment will not be attempted. 


**Additional Notes** 

- Depending on the study/site configuration of subject being added, the **Gender**, **DOB**, and/or **WeightLBS** fields may or may not be allowed. If the fields are allowed, then they will be required. If not allowed, then these fields must be excluded from the JSON request.
- Depending on the study/site configuration of subject being added, the **WearPosition** may or may not limit to utilize only one of the following values: 
	- Left Wrist
	- Right Wrist
	- Waist 
- Depending on the study/site configuration of subject being added, the **DeviceSerial** may or may not be allowed in order to perform an activity monitor assignment to subject

### Response: ###

    201 Created
    {
        "SubjectId":789
    }

Edit Subject
---
Modifies an existing subject.  List sites to find out which you can access.  You must have CanEditSubjects=true for a Site in order to edit a subject in it.  A 200 OK response is returned for a successfully edited subject.

### Request: ###

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
	"DeviceSerial": "TAS1D48341371"
    }

**Request Properties** 

Field|Type|Min|Max|Required|Accepted Values|Description|Notes
-----|----|---|---|--------|---------------|-----------|-----
DOB|ISO8601 Date||day before present day|Yes|||must be day before present day
Gender|String|||Yes|<ul><li>Male</li><li>Female</li></ul>||Study/site shall be configured to utilize this field
SiteId|Number|||Yes|||Site write access enforced
SubjectId|Number|||Yes|||Site write access enforced
SubjectIdentifier|String|||Yes|||Unique within study
WearPosition|String|||Yes|<ul><li>Left Wrist</li><li>Right Wrist</li><li>Waist</li></ul>||Study/site shall be configured to utilize this field
WeightLbs|Number|1|2000|Yes|||Study/site shall be configured to utilize this field
ChangeReason|String|||Yes|||Study/site shall be configured to utilize this field. Captured in operator audit record in accordance  with FDA 21 CFR Part 11. 
DeviceSerial|String|||No||Activity Monitor's serial number to assign to subject for data collection.|Study/site shall be configured in order to utilize this field. If blank or `null`, monitor assignment will not be attempted.|

**Additional Notes** 

- Depending on the study/site configuration of subject being edited, the **Gender**, **DOB**, and/or **WeightLBS** fields may or may not be allowed. If the fields are allowed, then they will be required. If not allowed, then these fields must be excluded from the JSON request.
- Depending on the study/site configuration of subject being edited, the **WearPosition** may or may not limit to utilize only one of the following values: 
	- Left Wrist
	- Right Wrist
	- Waist
- **ChangeReason** is required for all study configurations in CentrePoint created after 2017-11-30. 
- Depending on the study/site configuration of subject being edited, the **DeviceSerial** may or may not be allowed in order to perform an activity monitor assignment to subject 

### Response: ###

    200 OK

Subject Weight History
---
Returns all weight entries for a subject.

**Request:**

    GET /v1/subjects/{id}/weighthistory

**Response:**

    200 OK
    [
        {
            "DateAdded": "2013-07-26T15:02:34Z",
            "WeightLbs": 165.00
        },
        {
            "DateAdded": "2013-08-01T12:09:55Z",
            "WeightLbs": 173.00
        },
        ...
    ]

Subject Stats (overall)
---
Returns statistics about the requested subject.

**Request:**

    GET /v1/subjects/{id}/stats

**Response:**

    {
        "AverageDailyCalories": 1095.6042426509321,
        "AverageDailyMVPA": 88.6721,
        "AverageDailySteps": 9558.4590163934427,
        "AverageDailyWearFilteredCalories": 1095.5866411630786,
        "AverageDailyWearFilteredMVPA": 88.6721,
        "AverageDailyWearFilteredSteps": 9550.1557377049176,
        "AxisXAverageDailyCounts": 4411.156774332323,
        "AxisYAverageDailyCounts": 1286.232321552524,
        "AxisZAverageDailyCounts": 1900.443311432239,
        "AverageWearPercentage": 28.32022974,
        "Bouts": [
            { "Name":"10 minutes or more", "Count":194 },
            { "Name":"20 minutes or more", "Count":54 },
            { "Name":"30 minutes or more", "Count":27 },
            { "Name":"40 minutes or more", "Count":30 }
        ],
        "Cutpoints": [
            { "Name":"Sedentary", "Count":136545 },
            { "Name":"Light", "Count":11135 },
            { "Name":"Lifestyle", "Count":12390 },
            { "Name":"Moderate", "Count":10818 },
            { "Name":"Vigorous", "Count":0 },
            { "Name":"Very Vigorous", "Count":0 }
        ],
        "DaysWithAtLeastOneNonZeroEpoch": 122.0,
        "DaysWithGreaterThanFiftyPercentWear": 24.0,
        "FirstDayOfData": "2013-03-21T00:00:00",
        "LastDayOfData": "2013-08-04T00:00:00",
        "TotalDays": 137,
        "WearFilteredAxisXAverageDailyCounts": 3876.156774332323,
        "WearFilteredAxisYAverageDailyCounts": 999.232321552524,
        "WearFilteredAxisZAverageDailyCounts": 1645.443311432239,
        "WearFilteredBouts": [
            { "Name":"10 minutes or more", "Count":194 },
            { "Name":"20 minutes or more", "Count":54 },
            { "Name":"30 minutes or more", "Count":27 },
            { "Name":"40 minutes or more", "Count":30 }\
        ],
        "WearFilteredCutpoints": [
            { "Name":"Sedentary", "Count":14781 },
            { "Name":"Light", "Count":11135 },
            { "Name":"Lifestyle", "Count":12390 },
            { "Name":"Moderate", "Count":10818 },
            { "Name":"Vigorous", "Count":0 },
            { "Name":"Very Vigorous", "Count":0 }
        ]
    }

Subject Day Stats
---
Returns daily-level statistics about the requested subject.

**Request:**

    GET /v1/subjects/{id}/daystats

**Response:**

    [
        {
            "Date": "2013-04-15T00:00:00",
            "AxisXCounts": "44144",
            "AxisYCounts": "38873",
            "AxisZCounts": "11123",
            "Bouts": [{"Name":"10 minutes or more","Count":3},{"Name":"20 minutes or more","Count":0},{"Name":"30 minutes or more","Count":0},{"Name":"40 minutes or more","Count":0}],
            "Calories": 1601.1461012482916,
            "Cutpoints": [
                { "Name":"Sedentary", "Count":912},
                { "Name":"Light", "Count":224 },
                { "Name":"Lifestyle", "Count":201 },
                { "Name":"Moderate", "Count":101 },
                { "Name":"Vigorous", "Count":0 },
                { "Name":"Very Vigorous", "Count":0 }
            ],
            "Epochs": 1440,
            "MVPA": 101,
            "Steps": 14287.0,
            "TotalMinutes": 1440,
            "WearFilteredAxisXCounts": "37888",
            "WearFilteredAxisYCounts": "32443",
            "WearFilteredAxisZCounts": "9123",
            "WearFilteredBouts": [
                { "Name":"10 minutes or more", "Count":3 },
                { "Name":"20 minutes or more", "Count":0 },
                { "Name":"30 minutes or more", "Count":0 },
                { "Name":"40 minutes or more", "Count":0 }
            ],
            "WearFilteredCalories": 1601.1461012482916,
            "WearFilteredCutPoints": [
                { "Name":"Sedentary", "Count":214 },
                { "Name":"Light", "Count":224 },
                { "Name":"Lifestyle","Count":201 },
                { "Name":"Moderate", "Count":101 },
                { "Name":"Vigorous", "Count":0 },
                { "Name":"Very Vigorous","Count":0 }
            ],
            "WearFilteredMVPA": 101,
            "WearFilteredSteps": 14284.0,
            "WearMinutes": 742
        },
        ...
    ]

Subject Day Minutes
---
Returns daily-level minute epochs for the requested subject. The `day` argument is required. Daily-level minute epochs returned will be filtered in the subject's timezone. 

**Request:**

    GET /v1/subjects/{id}/dayminutes/{day}

**Additional Notes** 

- Format of {day} is "yyyy-MM-dd". Example: `2012-12-01` denotes December 1, 2012 and `2012-01-30` denotes January 30, 2013.
- x, y and z have been deprecated for AxisXCounts, AxisYCounts and AxisZCounts respectively.

**Response:**

    [
        {
            "Timestamp": "2013-03-21T16:59:00",
            "Calories": 6.88872851708981,
            "HR": 0.0,
            "Lux": 46.0,
            "Steps": 45.0,
            "Wear": true,
            "AxisXCounts": 4922,
            "AxisYCounts": 4392,
            "AxisZCounts": 3775,
            "x": 4922,
            "y": 4392,
            "z": 3775
        },
        ...
    ]


Subject Minutes on Range
---
Returns minute epochs for subject between specified time range. `Start` and `stop` arguments are required. Minute epochs returned will be filtered where time stamp falls on or after the supplied `start` time and before or on the supplied `stop` time. 

##### Filter By Timezone #####
By default the minute epochs returned will be filtered in the subject's timezone. To filter minute epochs in UTC, add trailing 'Z' to the `start` and `stop` arguments. This originates from the ISO 8601 standard to denote UTC time. 

**Additional Notes:** 

- Format of `start` and `stop` is `"yyyy-MM-ddTHH:mm:ss"` which adheres to ISO 8601 standard (example: `2016-06-14T20:46:00` denotes `June 14, 2016 08:46 PM`).
- No more than 7 days of data can be requested at a time.
- x, y and z have been deprecated for AxisXCounts, AxisYCounts and AxisZCounts respectively.

**Request:**

    GET /v1/subjects/{id}/minutesonrange?start={yyyy-MM-ddTHH:mm:ss}&stop={yyyy-MM-ddTHH:mm:ss}


**Response:**

    [
        {
            "TimestampUTC": "2013-07-27T21:40:00Z",
    	    "TimestampSubjectTZ": "2013-07-27T16:40:00",
            "Calories": 6.88872851708981,
            "HR": 0.0,
            "Lux": 46.0,
            "Steps": 45.0,
            "Wear": true,
            "x": 4922,
            "y": 4392,
            "z": 3775,
	    "AxisXCounts": 4922,
            "AxisYCounts": 4392,
            "AxisZCounts": 3775
        },
        ...
    ]


Subject Sleep Epochs [v1.1]
---
Returns a range of minute epochs about the requested subject where each is denoted if the subject is asleep or not.

**Request:**

    GET /v1/subjects/{id}/sleepepochs?inbed={yyyy-MM-ddTHH:mm:ss}&outbed={yyyy-MM-ddTHH:mm:ss}

**Note:** x, y and z have been deprecated for AxisXCounts, AxisYCounts and AxisZCounts respectively.

**Response:**

    [
        {
            "Timestamp": "2013-03-21T16:59:00",
            "Calories": 6.88872851708981,
            "HR": 0.0,
            "Lux": 46.0,
            "Steps": 45.0,
            "Wear": true,
            "Sleep": false,
            "AxisXCounts": 4922,
            "AxisYCounts": 4392,
            "AxisZCounts": 3775,
            "x": 4922,
            "y": 4392,
            "z": 3775
        },
        ...
    ]

Subject Sleep Score [v1.1]
---
Returns the score of a subject's data over a sleep period.

**Request:**

    GET /v1/subjects/{id}/sleepscore?inbed={yyyy-MM-ddTHH:mm:ss}&outbed={yyyy-MM-ddTHH:mm:ss}

**Response:**

    {
        "InBedTime": "2013-03-21T20:00:00",
        "OutBedTime": "2013-03-22T06:30:00",
        "Onset": "2013-03-21T20:00:00",
        "LatencyInMinutes": 0.0,
        "AvgAwakeningInMinutes": 0.0,
        "AwakeningCount": 0.0,
        "Efficiency": 1.0,
        "TimeAsleepInMinutes": 631.0,
        "TimeAwakeInMinutes": 0.0,
        "TimeInBedInMinutes": 631.0,
        "WakeAfterOnsetInMinutes": 0.0,
        "TotalCounts": 20
    }

Subject Bouts [v1.2]
---
Returns a list of wear filtered and non-wear filtered bout periods for subject.  `Start` and `Stop` arguments are optional.  If `Start` is supplied, bouts returned will be filtered where the begin time falls on or after the supplied `Start` time.  If `Stop` is supplied, bouts returned will be filtered where the begin time falls before the supplied `Stop` time.

**Request:**

    GET /v1/subjects/{id}/bouts?start={yyyy-MM-ddTHH:mm:ss}&stop={yyyy-MM-ddTHH:mm:ss}

**Response:**

    {
        "WearFilteredBouts": [
            {
                "Start": "2013-03-21T12:00:00",
                "Stop": "2013-03-21T12:17:00"
            },
            {
                "Start": "2013-03-21T12:25:00",
                "Stop": "2013-03-22T12:35:00"
            }
        ],
        "NonWearFilteredBouts": [
            {
                "Start": "2013-03-21T12:00:00",
                "Stop": "2013-03-21T12:17:00"
            },
            {
                "Start": "2013-03-21T12:25:00",
                "Stop": "2013-03-22T12:35:00"
            }
        ]
    ]

Subject Sleep Periods
---
 Returns a list of sleep periods for a subject.  `Start` and `stop` arguments are optional.  If `start` argument is supplied, sleep periods returned will be filtered where the In Bed Time falls on or after the supplied `start` time.  If `stop` is supplied, sleep periods returned will be filtered where the In Bed Time falls before the supplied `stop` time. If the `AutoDetected` field (in the response) denotes `true`, the sleep period was automatically detected otherwise it was manually entered.

**Request:**

    GET /v1/subjects/{id}/bedtimes?start={yyyy-MM-ddTHH:mm:ss}&stop={yyyy-MM-ddTHH:mm:ss}

**Response:**

    [
        {
            "SubjectId": 114,
            "InBedTime": "2013-03-21T20:00:00",
            "OutBedTime": "2013-03-22T08:25:00",
            "AutoDetected": true
        },
        {
            "SubjectId": 114,
            "InBedTime": "2013-03-22T20:15:00",
            "OutBedTime": "2013-03-23T08:05:00",
            "AutoDetected": true
        }
        ...
    ]

Subject Data Files
---
 Returns a list of previously uploaded data files for a specific subject. The 'dataType' argument is optional. By default, the data files returned will only be of the 'RAW' data type.

**Request:**

	GET /v1/subjects/{id}/dataFiles

**Response:**

	 {
	  "RAW": [
	    {
	      "DataFileId": 5319,
	      "UploadId": 5468,
	      "FileType": "RAW",
	      "FileSizeInBytes": "76698",
	      "UploadedDate": "2015-01-14T22:54:08Z",
	      "Metadata": {
	        "Filename": "MOS2A13510263_2015-01-14___16-54-07.gt3x",
	        "BeginOfData": "2015-01-14T16:19:00Z",
	        "EndOfData": "2015-01-14T22:54:07Z"
	      }
	    },
	    {
	      "DataFileId": 5323,
	      "UploadId": 5478,
	      "FileType": "RAW",
	      "FileSizeInBytes": "1447186",
	      "UploadedDate": "2015-01-15T21:10:00Z",
	      "Metadata": {
	        "Filename": "MOS2A13510263_2015-01-15___15-09-58.gt3x",
	        "BeginOfData": "2015-01-14T22:56:00Z",
	        "EndOfData": "2015-01-15T21:09:59Z"
	      }
	    }...
	 }


Data File Download Url
---

Returns a Pre-Signed Url where a specific data file can be downloaded. The Url's expiration date is also included within the response.

**Request:**

    GET /v1/datafiles/{dataFileId}/DownloadUrl

**Response:**

    
    {
        "DownloadURL": https://s3.amazonaws.com/acticloud ...,
        "URLExpirationDate": "2015-02-03T06:42:40.1654394Z"
    }


Stop Data Collection for Subject
---

Stops data collection for requested subject by removing the subject's active monitor assignment.
  
### Request: ###

    PUT /v1/subjects/RemoveDeviceAssignment
	Content-Type:application/json
	{
	    "SubjectId": 3792
	    "DeviceSerial": "TAS2A13510263"
	}

#### Request Properties ####

Field|Type|Required|Description
-----|----|--------|-----------------
SubjectId|number|yes|Subject's Primary Key in which API user wishes to stop activity monitor data collection
DeviceSerial|string|yes|Activity monitor serial in which to stop collecting data for given subject


### Response: ###

    200 OK
