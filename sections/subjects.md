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
        "Gender": "Female",
        "WearPosition": "Left Wrist"
    }

Get overall stats for a subject
---
Returns statistics about the requested subject.

* `GET /v1/subjects/{id}/stats`

**Response:**

    {
        "AverageDailyCalories": 1095.6042426509321,
        "AverageDailyCounts": 633700.5,
        "AverageDailyMVPA": 88.6721,
        "AverageDailySteps": 9558.4590163934427,
        "AverageDailyWearFilteredCalories": 1095.5866411630786,
        "AverageDailyWearFilteredCounts": 632821.61475409835,
        "AverageDailyWearFilteredMVPA": 88.6721,
        "AverageDailyWearFilteredSteps": 9550.1557377049176,
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

Get daily stats for a subject
---
Returns daily-level statistics about the requested subject.

* `GET /v1/subjects/{id}/daystats`

**Response:**

    [
        {   
            "Date": "2013-04-15T00:00:00",
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
            "DownProjectedCounts": 868621.0,
            "Epochs": 1440,
            "MVPA": 101,
            "Steps": 14287.0,
            "TotalMinutes": 1440,
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
            "WearFilteredDownProjectedCounts": 867791.0,
            "WearFilteredMVPA": 101,
            "WearFilteredSteps": 14284.0,
            "WearMinutes": 742
        },
        {
            "Date": "2013-04-16T00:00:00",
            "Bouts": [
                { "Name":"10 minutes or more", "Count":2 },
                { "Name":"20 minutes or more", "Count":0 },
                { "Name":"30 minutes or more", "Count":1 },
                { "Name":"40 minutes or more", "Count":0 }
            ],
            "Calories": 1819.3762418797176,
            "Cutpoints": [
                { "Name":"Sedentary", "Count":984 },
                { "Name":"Light", "Count":151 },
                { "Name":"Lifestyle", "Count":157 },
                { "Name":"Moderate", "Count":148 },
                { "Name":"Vigorous", "Count":0 },
                { "Name":"Very Vigorous", "Count":0 }
            ],
            "DownProjectedCounts": 1057931.0,
            "Epochs": 1440,
            "MVPA": 148,
            "Steps": 17365.0,
            "TotalMinutes": 1440,
            "WearFilteredBouts": [
                { "Name":"10 minutes or more", "Count":2 },
                { "Name":"20 minutes or more", "Count":0 },
                { "Name":"30 minutes or more", "Count":1 },
                { "Name":"40 minutes or more", "Count":0 }
            ],
            "WearFilteredCalories": 1819.3707163288436,
            "WearFilteredCutPoints": [
                { "Name":"Sedentary", "Count":186 },
                { "Name":"Light", "Count":151 },
                { "Name":"Lifestyle", "Count":157 },
                { "Name":"Moderate", "Count":148 },
                { "Name":"Vigorous", "Count":0 },
                { "Name":"Very Vigorous", "Count":0 }
            ],
            "WearFilteredDownProjectedCounts": 1057078.0,
            "WearFilteredMVPA": 148,
            "WearFilteredSteps": 17363.0,
            "WearMinutes": 642
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


Get sleep epochs for a subject
---
Returns a range of minute epochs about the requested subject where each is denoted if the subject is asleep or not.

* `GET /v1/subjects/{id}/sleepepochs?inbed={yyyy-MM-ddTHH:mm:ss}&outbed={yyyy-MM-ddTHH:mm:ss}`

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
            "Sleep": false,
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
            "Sleep": false,
            "x": 5424,
            "y": 5222,
            "z": 5031
        },
        ...
    ]


Get sleep score for a subject
---
Returns the score of a subject's data over a sleep period.

* `GET /v1/subjects/{id}/sleepscore?inbed={yyyy-MM-ddTHH:mm:ss}&outbed={yyyy-MM-ddTHH:mm:ss}`

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
