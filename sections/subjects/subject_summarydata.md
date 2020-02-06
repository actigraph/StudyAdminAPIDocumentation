Subjects
===

Subject Minute Epochs (for Single Day)
---
Returns minute epochs for a given subject on a given day. The `day` argument is required. Daily-level minute epochs returned will be retrieved in the subject's site timezone. 

**Request:**

    GET /v1/subjects/{SubjectId}/dayminutes/{day}

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


Subject Minute Epochs (for Custom Range)
---
Returns minute epochs for a given subject between specified time range. `Start` and `stop` arguments are required. Minute epochs returned will be filtered where time stamp falls on or after the supplied `start` time and before or on the supplied `stop` time. 

##### Filter By Timezone #####
By default the minute epochs returned will be filtered in the subject's timezone. To filter minute epochs in UTC, add trailing 'Z' to the `start` and `stop` arguments. This originates from the ISO 8601 standard to denote UTC time. 

**Additional Notes:** 

- Format of `start` and `stop` is `"yyyy-MM-ddTHH:mm:ss"` which adheres to ISO 8601 standard (example: `2016-06-14T20:46:00` denotes `June 14, 2016 08:46 PM`).
- No more than 7 days of data can be requested at a time.
- x, y and z have been deprecated for AxisXCounts, AxisYCounts and AxisZCounts respectively.

**Request:**

    GET /v1/subjects/{SubjectId}/minutesonrange?start={yyyy-MM-ddTHH:mm:ss}&stop={yyyy-MM-ddTHH:mm:ss}


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


Subject Daily Statistics
---
Returns daily summary statistics on a given subject.

**Request:**

    GET /v1/subjects/{SubjectId}/daystats
    
    
    
#### Request Properties ####

Field|Type|Required|Default Value|Description|Example Request URI
|-----|----|---------|------------|-----------|-------------------|
subjectId|Number|yes||primary key of the subject data record|/v1/subjects/{subjectId}/daystats
startDate|Date|no|`null`|Start Date (in subject's site timezone) to filter daily-aggregated statistics records for requsted subject on or after the given date|/v1/subjects/{subjectId}/daystats?startDate=YYYY-MM-DD
endDate|Date|no|`null`|End Date (in subject's site timezone) to filter daily-aggregated statistics records for requsted subject on or before the given date|/v1/subjects/{subjectId}/daystats?endDate=YYYY-MM-DD


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
            "WearMinutes": 742,
            "AwakeWearMinutes": 309 
        },
        ...
    ]



Subject Overall Statistics
---
Returns overall statistics about a given subject spanning across the entire subject's data collection range.

**Request:**

    GET /v1/subjects/{SubjectId}/stats

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