Subjects
===

Get all subjects
---

A list of subjects can only be obtained within the context of a study. Refer to the [Study](studies.md#get-all-subjects-within-a-study) documentation.

Get a subject
---
Returns detailed information about the requested subject.

* `GET /v1/subjects/#{id}`

**Response:**

    {
        "Id":123,
        "SubjectIdentifier": "013001",
        "DOB": "1974-02-11T00:00:00",
        "Timezone": "(GMT -6:00) Central Time (US & Canada), Mexico City"
    }

Get overall stats for a subject
---
Returns statistics about the requested subject.

* `GET /v1/subjects/#{id}/stats`

**Response:**

    {
        "AverageDailyCalories": 1030.4035705500314,
        "AverageDailyCounts": 600741.525,
        "AverageDailyMVPA": 114.1833,
        "AverageDailySteps": 8988.8583333333336,
        "AverageDailyWearFilteredCalories": 1030.3872242719622,
        "AverageDailyWearFilteredCounts": 600020.4916666667,
        "AverageDailyWearFilteredMVPA": 114.1833,
        "AverageDailyWearFilteredSteps": 8986.0416666666661,
        "AverageWearPercentage": 28.66101518,
        "Bouts": "[
            {"Name":"10 minutes or more","Count":295},
            {"Name":"20 minutes or more","Count":74},
            {"Name":"30 minutes or more","Count":27},
            {"Name":"40 minutes or more","Count":49}
        ]",
        "Cutpoints": "[
            {"Name":"Sedentary","Count":134169},
            {"Name":"Light","Count":10493},
            {"Name":"Lifestyle","Count":11559},
            {"Name":"Moderate","Count":9937},
            {"Name":"Vigorous","Count":0},
            {"Name":"Very Vigorous","Count":0}
        ]",
        "DaysWithAtLeastOneNonZeroEpoch": 120.0,
        "DaysWithGreaterThanFiftyPercentWear": 20.0,
        "FirstDayOfData": "2013-03-21T00:00:00",
        "LastDayOfData": "2013-08-20T00:00:00",
        "TotalDays": 153,
        "WearFilteredBouts": "[
            {"Name":"10 minutes or more","Count":213},
            {"Name":"20 minutes or more","Count":73},
            {"Name":"30 minutes or more","Count":24},
            {"Name":"40 minutes or more","Count":41}
        ]",
        "WearFilteredCutpoints": "[
            {"Name":"Sedentary","Count":132155},
            {"Name":"Light","Count"9233},
            {"Name":"Lifestyle","Count":10324},
            {"Name":"Moderate","Count":10144},
            {"Name":"Vigorous","Count":0},
            {"Name":"Very Vigorous","Count":0}
        ]",
    }

Get daily stats for a subject
---
Returns daily-level statistics about the requested subject.

* `GET /v1/subjects/#{id}/daystats`

**Response:**

    {[
        {
            "Date": "2013-03-21T00:00:00",
            "Bouts": "[
                {"Name":"10 minutes or more","Count":0},
                {"Name":"20 minutes or more","Count":0},
                {"Name":"30 minutes or more","Count":1},
                {"Name":"40 minutes or more","Count":0}
            ]",
            "Calories": 676.08246139605058,
            "Cutpoints": "[
                {"Name":"Sedentary","Count":331},
                {"Name":"Light","Count":44},
                {"Name":"Lifestyle","Count":45},
                {"Name":"Moderate","Count":67},
                {"Name":"Vigorous","Count":0},
                {"Name":"Very Vigorous","Count":0}
            ]",
            "DownProjectedCounts": 446907.0,
            "Epochs": 487,
            "MVPA": 78,
            "Steps": 7262.0,
            "WearFilteredBouts": "[
                {"Name":"10 minutes or more","Count":0},
                {"Name":"20 minutes or more","Count":0},
                {"Name":"30 minutes or more","Count":1},
                {"Name":"40 minutes or more","Count":0}
            ]",
            "WearFilteredCalories": 676.08246139605058,
            "WearFilteredCutPoints": "[
                {"Name":"Sedentary","Count":74},
                {"Name":"Light","Count":44},
                {"Name":"Lifestyle","Count":45},
                {"Name":"Moderate","Count":67},
                {"Name":"Vigorous","Count":0},
                {"Name":"Very Vigorous","Count":0}
            ]",
            "WearFilteredDownProjectedCounts": 866954.0,
            "WearFilteredMVPA": 0,
            "WearFilteredSteps": 0.0,
            "WearMinutes": 0,
        },
        ...
    ]}

Get daily minutes for a subject
---
Returns daily-level minute epochs about the requested subject.

* `GET /v1/subjects/#{id}/dayminutes`

**Response:**

    {[
        {
            "Timestamp": "2013-07-14T00:00:00",
            "Calories": :0.0,
            "DownProjectedCounts": 0.0,
            "DownX": 0.992125984251969,
            "DownY": 0.047244094488189,
            "DownZ": -0.102362204724409,
            "HR": 0.0,
            "Lux": 9.0,
            "Steps": 123,
            "Wear": 1,
            "x": 0,
            "y": 0,
            "z": 0
        },
        ...
    ]}
