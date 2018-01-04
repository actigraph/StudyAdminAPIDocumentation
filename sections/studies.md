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
            "WearPosition": "Left Wrist",
            "WeightLbs": "105.74",
        },
        {
            "Id":125,
            "SubjectIdentifier": "013002",
            "DOB": "1988-07-14T00:00:00",
            "Timezone": "(GMT -6:00) Central Time (US & Canada), Mexico City"
            "Gender": "Male",
            "WearPosition": "Right Wrist"
            "WeightLbs": "198",
        },
        ...
    ]


Study Devices
---

Returns a list of all study devices within the requested study's inventory

**Request:**

	GET /v1/studies/{id}/devices?assignmentStatus={assignmentStatus}

**Response:**

	[
		{
			"DeviceSerial":"TAS1D48341371",
			"DataHubSerial":"CDM1448341371",
			"Assignment": {
							"Status": "Assigned",
							"SubjectId": 09234
						  }
		},
		{
			"DeviceSerial":"TAS1D48341372",
			"DataHubSerial":"CDM1448341371",
			"Assignment": {
							"Status": "Not Assigned",
							"SubjectId": null
						  }
		}
	]



**Additional Notes** 

- ``DeviceSerial`` denotes the activity monitor's serial number
- ``DataHubSerial`` denotes the CentrePoint DataHub (CDH) device's serial number packaged with activity monitor that is distributed to subject. 
- ``assignmentStatus`` parameter is optional. If not specified, all devices within the study's inventory will be returned
- Available options for ``Status`` field in the ``Assignment`` object are:
	- Assigned (denotes if monitor is actively assigned to subject)
	- Not Assigned (denotes if monitor is NOT actively assigned to subject)
- ``SubjectId`` field in the ``Assignment`` object denotes the subject in which the monitor is actively assigned to. If monitor is not actively assigned, ``SubjectId`` will be return as ``null``.