Studies
===

Get all studies
---

* `GET /v1/studies` returns a list of studies that are within your organization

**Response:**

    {[
        {
            "Id": 1,
            "Name": "Example Study",
            "DateCreated": "2013-03-04T08:00:00Z"
        },
        ...
    ]}

Get a study
---

* `GET /v1/studies/#{id}` returns detailed information about the requested study

**Response:**

    {
        "Id": 1,
        "Name": "Example Study",
        "DateCreated": "2013-03-04T08:00:00Z"
    }


Get all subjects within a study
---

* `GET /v1/studies/#{id}/subjects` returns a list of all subjects within the requested study

**Response:**

    {[
        {
			"Id":123,
			"SubjectIdentifier": "013001",
			"DOB": "1974-02-11T00:00:00",
			"Timezone": "(GMT -6:00) Central Time (US & Canada), Mexico City"
        },
        ...
    ]}