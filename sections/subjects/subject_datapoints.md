[<< Back to Subjects](/sections/subjects.md)

Retrieval of Subject Data Points (Sleep, Wear, etc.)
===

Subject Sleep Periods
---
 Returns a list of sleep periods for a subject.  `start` and `stop` arguments are optional.  If `start` argument is supplied, sleep periods returned will be filtered where the In Bed Time falls on or after the supplied `start` time.  If `stop` is supplied, sleep periods returned will be filtered where the In Bed Time falls before the supplied `stop` time. If the `AutoDetected` field (in the response) denotes `true`, the sleep period was automatically detected otherwise it was manually entered.

**Request:**

    GET /v1/subjects/{SubjectId}/bedtimes?start={yyyy-MM-ddTHH:mm:ss}&stop={yyyy-MM-ddTHH:mm:ss}

**Response:**

```json
200 OK
[
	{
		"SubjectId": 114,
		"InBedTime": "2013-08-06T01:42:00",
		"OutBedTime": "2013-08-06T15:30:00",
		"InBedTimeUtc": "2013-08-06T06:42:00+05:30",
		"OutBedTimeUtc": "2013-08-06T20:30:00+05:30",
		"AutoDetected": true
	},
	{
		"SubjectId": 114,
		"InBedTime": "2013-08-06T19:28:00",
		"OutBedTime": "2013-08-06T22:33:00",
		"InBedTimeUtc": "2013-08-07T00:28:00+05:30",
		"OutBedTimeUtc": "2013-08-07T03:33:00+05:30",
		"AutoDetected": true
	}
]
```


Subject Sleep Epochs 
---
Returns a range of minute epochs about the requested subject where each is denoted if the subject is asleep or not.

**Request:**

    GET /v1/subjects/{SubjectId}/sleepepochs?inbed={yyyy-MM-ddTHH:mm:ss}&outbed={yyyy-MM-ddTHH:mm:ss}

**Note:** x, y and z have been deprecated for AxisXCounts, AxisYCounts and AxisZCounts respectively.

**Response:**


```json
200 OK
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
	{
	    "Timestamp": "2013-03-21T17:00:00",
	    "Calories": 6.88872851708981,
	    "HR": 0.0,
	    "Lux": 47.0,
	    "Steps": 43.0,
	    "Wear": true,
	    "Sleep": false,
	    "AxisXCounts": 4901,
	    "AxisYCounts": 4298,
	    "AxisZCounts": 2775,
	    "x": 4901,
	    "y": 4298,
	    "z": 2775
	}
	
]
```

Subject Weight History
---
Returns all weight entries for a subject.

**Request:**

    GET /v1/subjects/{SubjectId}/weighthistory

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




Subject Sleep Score 
---
Returns the score of a subject's data over a sleep period.

**Request:**

    GET /v1/subjects/{SubjectId}/sleepscore?inbed={yyyy-MM-ddTHH:mm:ss}&outbed={yyyy-MM-ddTHH:mm:ss}

**Response:**

	{
		"InBedTime": "2013-07-25T23:40:00",
		"OutBedTime": "2013-07-26T06:28:00",
		"Onset": "2013-07-25T23:40:00",
		"InBedTimeUtc": "2013-07-26T04:40:00Z",
		"OutBedTimeUtc": "2013-07-26T11:28:00Z",
		"OnsetUtc": "2013-07-26T04:40:00Z",
		"LatencyInMinutes": 0.0,
		"AvgAwakeningInMinutes": 0.0,
		"AwakeningCount": 0.0,
		"Efficiency": 1.0,
		"TimeAsleepInMinutes": 408.0,
		"TimeAwakeInMinutes": 0.0,
		"TimeInBedInMinutes": 408.0,
		"WakeAfterOnsetInMinutes": 0.0,
		"TotalCounts": 0
	}


Subject Bouts 
---
Returns a list of wear filtered and non-wear filtered bout periods for subject.  `Start` and `Stop` arguments are optional.  If `Start` is supplied, bouts returned will be filtered where the begin time falls on or after the supplied `Start` time.  If `Stop` is supplied, bouts returned will be filtered where the begin time falls before the supplied `Stop` time.

**Request:**

    GET /v1/subjects/{SubjectId}/bouts?start={yyyy-MM-ddTHH:mm:ss}&stop={yyyy-MM-ddTHH:mm:ss}

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



	
Subject Milestones
---
Returns milestones for a given subject

### Request: ###

    GET /v1/subjects/{id}/milestones

### Response: ###
	[
	  {
		"Id": 108,
		"SubjectIdentifier": "000055",
		"TimestampUTC": "2013-08-02T04:59:59",
		"TimestampSubjectTZ": "2013-08-01T23:59:59",
		"MilestoneName": "Visit One"
	  },
	  ...
	]

Subject Wear Periods
---
Returns wear periods for the requested subject.

**Request:**

    GET /v1/subjects/{id}/wearperiods
    
    
    
#### Request Properties ####

Field|Type|Required|Default Value|Description|Example Request URI
|-----|----|---------|------------|-----------|-------------------|
id|Number|yes||primary key of the subject data record|/v1/subjects/{id}/wearperiods
start|Date|no|`null`|Start date to filter wear periods for the requsted subject on or after the date specified|/v1/subjects/{subjectId}/wearperiods?start={yyyy-MM-ddTHH:mm:ss}
stop|Date|no|`null`|Stop date to filter wear periods for the requsted subject on or before the date specified|/v1/subjects/{subjectId}/wearperiods?stop={yyyy-MM-ddTHH:mm:ss}


**Response:**

    [
          {
			"Id": 22422,
			"SubjectId": 8851,
			"Start": "2017-03-27T20:22:00Z",
			"Stop": "2017-03-27T20:28:00Z",
            "StartSubjectTZ": "2017-03-27T14:22:00",
            "StopSubjectTZ": "2017-03-27T14:28:00"
		},
		{
			"Id": 22423,
			"SubjectId": 8851,
			"Start": "2017-03-29T18:56:00Z",
			"Stop": "2017-03-29T20:00:00Z",
            "StartSubjectTZ": "2017-03-29T12:56:00",
            "StopSubjectTZ": "2017-03-29T14:00:00"
		},
		{
			"Id": 22424,
			"SubjectId": 8851,
			"Start": "2017-03-31T19:39:00Z",
			"Stop": "2017-03-31T19:40:00Z",
            "StartSubjectTZ": "2017-03-31T13:39:00",
            "StopSubjectTZ": "2017-03-31T13:40:00"
		},
		{
			"Id": 22425,
			"SubjectId": 8851,
			"Start": "2017-04-03T13:27:00Z",
			"Stop": "2017-04-03T13:28:00Z",
            "StartSubjectTZ": "2017-04-03T07:27:00",
            "StopSubjectTZ": "2017-04-03T07:28:00"
		},
		{
			"Id": 22426,
			"SubjectId": 8851,
			"Start": "2017-04-03T21:25:00Z",
			"Stop": "2017-04-03T21:27:00Z",
            "StartSubjectTZ": "2017-04-03T15:25:00",
            "StopSubjectTZ": "2017-04-03T15:27:00"
		},
		{
			"Id": 22427,
			"SubjectId": 8851,
			"Start": "2017-04-04T18:47:00Z",
			"Stop": "2017-04-04T18:48:00Z",
            "StartSubjectTZ": "2017-04-04T12:47:00",
            "StopSubjectTZ": "2017-04-04T12:47:00"
		},
        ...
    ]
