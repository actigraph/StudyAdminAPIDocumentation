Studies
===

List Studies
---

* `GET /v1/studies` returns a list of studies that are within your organization

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

* `GET /v1/studies/{id}` returns detailed information about the requested study

**Response:**

    {
        "Id": 1,
        "Name": "Example Study",
        "DateCreated": "2013-03-04T08:00:00Z"
    }


Study Subjects
---

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
