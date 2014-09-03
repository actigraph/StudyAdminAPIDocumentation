Subjects
===

Study Subjects
---

Returns a list of all subjects within the requested study.

**Request:**

    GET /v1/studies/{id}/subjects

**Response:**

    [
        {
            "Id":123,
            "SubjectIdentifier": "013001",
            "DOB": "1974-02-11T00:00:00",
            "Timezone": "(GMT -6:00) Central Time (US & Canada), Mexico City",
            "Gender": "Female",
            "WearPosition": "Left Wrist",
            "WeightLbs": "105.74",
        },
        {
            "Id":125,
            "SubjectIdentifier": "013002",
            "DOB": "1988-07-14T00:00:00",
            "Timezone": "(GMT -6:00) Central Time (US & Canada), Mexico City",
            "Gender": "Male",
            "WearPosition": "Right Wrist"
            "WeightLbs": "198",
        },
        ...
    ]

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
        "Timezone": "(GMT -6:00) Central Time (US & Canada), Mexico City",
        "Gender": "Female",
        "WearPosition": "Left Wrist",
        "WeightLbs": "105.74",
    }

Add Subject
---
Creates a new subject.  Subjects are created at the site level.  List sites to find out which you can access.  You must have CanAddSubjects=true for a Site in order to create a subject in it.  The new Subject's Id is returned upon successful creation along with a 201 Created response.

**Request:**

    POST /v1/subjects
    Content-Type:application/json

    SubjectIdentifier=000071&SiteId=224&WearPosition=Waist&DOB=1988-08-01&Gender=Male&WeightLbs=199

Field|Type|Min|Max|Required|Notes
-----|----|---|---|--------|-----
DOB|ISO8601 Date|n/a|Yesterday|Yes|Must be before today
Gender|String|n/a|n/a|Yes|Male, Female
SiteId|Number|n/a|n/a|Yes|Must have permission
SubjectIdentifier|String|1|50|Yes|Unique within study
WearPosition|String|n/a|n/a|Yes|Left Wrist, Right Wrist, Waist
WeightLbs|Number|1|2000|Yes|-

**Response:**

    201 Created
    {
        "SubjectId":789
    }

Edit Subject
---
Modifies an existing subject.  List sites to find out which you can access.  You must have CanEditSubjects=true for a Site in order to edit a subject in it.  A 200 OK response is returned for a successfully edited subject.

**Request:**

    PUT /v1/subjects
    Content-Type:application/json

    SubjectId=789&SubjectIdentifier=000071&SiteId=224&WearPosition=Waist&DOB=1988-08-01&Gender=Male&WeightLbs=205

Field|Type|Min|Max|Required|Notes
-----|----|---|---|--------|-----
DOB|ISO8601 Date|n/a|Yesterday|Yes|Must be before today
Gender|String|n/a|n/a|Yes|Male, Female
SiteId|Number|n/a|n/a|Yes|Must have permission
SubjectId|Number|n/a|n/a|Yes|Must have permission
SubjectIdentifier|String|1|50|Yes|Unique within study
WearPosition|String|n/a|n/a|Yes|Left Wrist, Right Wrist, Waist
WeightLbs|Number|1|2000|Yes|-

**Response:**

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
Returns daily-level minute epochs about the requested subject.

**Request:**

    GET /v1/subjects/{id}/dayminutes/{day}

**Note:** Format of {day} is "yyyy-MM-dd" Examples: `2012-12-01` and Dec. 1, 2012 and `2012-01-30` for Jan. 30, 2013.

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
            "AxisXCounts": 4922,
            "AxisYCounts": 4392,
            "AxisZCounts": 3775,
            "x": 4922,
            "y": 4392,
            "z": 3775
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
Returns a list of wear filtered and non-wear filtered bout periods for a range of subject's data.  `Start` and `stop` arguments are optional.  If `start` is supplied, bed times returned will be filtered where the In Bed Time falls on or after the supplied `start` time.  If `stop` is supplied, bed times returned will be filtered where the In Bed Time falls before the supplied `stop` time.

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

Subject Bed Times [v1.3
---
 Returns a list of bed times for a subject.  `Start` and `stop` arguments are optional.  If `start` is supplied, bed times returned will be filtered where the In Bed Time falls on or after the supplied `start` time.  If `stop` is supplied, bed times returned will be filtered where the In Bed Time falls before the supplied `stop` time.

**Request:**

    GET /v1/subjects/{id}/bedtimes?start={yyyy-MM-ddTHH:mm:ss}&stop={yyyy-MM-ddTHH:mm:ss}

**Response:**

    [
        {
            "SubjectId": 114,
            "InBedTime": "2013-03-21T20:00:00",
            "OutBedTime": "2013-03-22T08:25:00"
        },
        {
            "SubjectId": 114,
            "InBedTime": "2013-03-22T20:15:00",
            "OutBedTime": "2013-03-23T08:05:00"
        }
        ...
    ]
