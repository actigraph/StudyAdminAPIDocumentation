Subjects
===

Get all subjects (in context of a study)
---

A list of subjects can only be obtained within the context of a study.

* `GET /v1/studies/{id}/subjects` returns a list of all subjects within the requested study

**Response:**

    [
        {
			"Id":123,
			"SubjectIdentifier": "013001",
			"DOB": "1974-02-11T00:00:00",
			"Timezone": "(GMT -6:00) Central Time (US & Canada), Mexico City"
			"Gender": "Female",
			"WearPosition": "Left Wrist"
        },
        {
			"Id":125,
			"SubjectIdentifier": "013002",
			"DOB": "1988-07-14T00:00:00",
			"Timezone": "(GMT -6:00) Central Time (US & Canada), Mexico City"
			"Gender": "Male",
			"WearPosition": "Right Wrist"
        },
        ...
    ]

Get a subject
---
Returns detailed information about the requested subject.

* `GET /v1/subjects/{id}`

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

* `GET /v1/subjects/{id}/stats`

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

* `GET /v1/subjects/{id}/daystats`

**Response:**

    [
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
    ]

Get daily minutes for a subject
---
Returns daily-level minute epochs about the requested subject.

* `GET /v1/subjects/{id}/dayminutes/{day}`

**Note:** Format of {day} is "yyyy-MM-dd" Examples: `2012-12-01` and Dec. 1, 2012 and `2012-01-30` for Jan. 30, 2013.

**Response:**

    [
        {
            "Timestamp": "2013-03-21T16:59:00",
            "Calories": 6.88872851708981,
            "DownProjectedCounts": 3972.0,
            "DownX": -0.68503937007874,
            "DownY": 0.181102362204724,
            "DownZ": 0.700787401574803,
            "HR": 0.0,
            "Lux": 46.0,
            "Steps": 45.0,
            "Wear": true,
            "x": 4922,
            "y": 4392,
            "z": 3775
        },
        {
            "Timestamp": "2013-03-21T17:00:00",
            "Calories": 6.91655624935538,
            "DownProjectedCounts": 4765.0,
            "DownX": -0.322834645669291,
            "DownY": 0.259842519685039,
            "DownZ": 0.913385826771654,
            "HR": 0.0,
            "Lux": 37.0,
            "Steps": 67.0,
            "Wear": true,
            "x": 5424,
            "y": 5222,
            "z": 5031
        },
        ...
    ]
