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
			"DataCollectionStatus": "Collection Stopped",
			"DeviceSerial": null
        },
        {
            "Id":125,
            "SubjectIdentifier": "013002",
            "DOB": "1988-07-14T00:00:00",
            "Timezone": "(GMT -6:00) Central Time (US & Canada), Mexico City"
            "Gender": "Male",
            "WearPosition": "Right Wrist"
            "WeightLbs": "198",
			"DataCollectionStatus": "Collecting",
			"DeviceSerial": "TAS1D48341371"
        },
        ...
    ]


Study Devices
---

Returns a list of the activity monitors within the requested study's inventory

### Request: ###

	GET /v1/studies/{id}/devices

#### Request Properties ####

Field|Type|Required|Accepted Values|Default Value|Description|Example Request URI
-----|----|---------|--------------|-------------|-----------|-------------------
isAssignableFilter|bool|no|<ul><li>true</li><li>false</li></ul>|null|Allows API user to filter activity monitors on whether the device is eligible to be assigned to a subject. If not provided, all study's devices will be returned|/v1/studies/{id}/devices?isAssignableFilter={isAssignableValue}


### Response: ###

	[
		{
			"Id" = 101,
			"DeviceSerial": "TAS1D48341371",
			"DataHubSerial": "CDM1448341371",
			"IsAssignable": true,
			"AssignmentStatus": "Not Assigned",
			"SiteName": "University of South Dakota"
		},
		{
			"Id" = 102,
			"DeviceSerial": "TAS1D48341372",
			"DataHubSerial": "CDM1448341373",
			"IsAssignable": false,
			"AssignmentStatus": "Incomplete Assignment",
			"SiteName": "University of West Florida"
		}
		...
	]


#### Response Properties ####

Field|Type|Accepted Values|Description
-----|----|----------|-----|
Id|number||Primary Key of Study Device Id
DeviceSerial|string||Activity monitor's serial number
DataHubSerial|string||The CentrePoint DataHub (CDH) device serial number that was packaged/distributed with the activity monitor
IsAssignable|bool|<ul><li>true</li><li>false</li></ul>|Boolean that determines if activity monitor can be assigned to a new or existing subject for data collection|
AssignmentStatus|string|<ul><li>Assigned</li><li>NotAssigned</li><li>IncompleteAssignment</li></ul>|Assignment status of activity monitor
SiteName|string||Site name in which activity monitor resides
