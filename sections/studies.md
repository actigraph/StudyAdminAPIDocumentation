Studies
===

List Studies
---

Returns a list of studies that are within your organization.

**Request:**

    GET /v1/studies

**Response:**

    [
        {
            "Id": 1,
            "Name": "Example Study",
            "DateCreated": "2013-03-04T08:00:00Z"
        },
        {
            "Id": 2,
            "Name": "Another Example Study",
            "DateCreated": "2013-04-01T08:00:00Z"
        },
        ...
    ]

Study Details
---

Returns detailed information about the requested study.

**Request:**

    GET /v1/studies/{id}

**Response:**

    {
        "Id": 1,
        "Name": "Example Study",
        "DateCreated": "2013-03-04T08:00:00Z"
    }


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
