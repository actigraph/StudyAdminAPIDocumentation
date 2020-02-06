[<< Home](/README.md)

Sites
===

List Sites
---

A list of sites you can access.  Explicit read/write permissions are included in each response. 

**Request:**

    GET /v1/sites

**Response:**

    [
        {
            "SiteId": 11231,
            "SiteName": "East Patients",
            "StudyId": 512,
            "StudyName": "Example Study 1",
            "OrganizationId": 1,
            "OrganizationName": "ActiGraph"
        },
        {
            "SiteId": 11232,
            "SiteName": "West Patients",
            "StudyId": 512,
            "StudyName": "Example Study 1",
            "OrganizationId": 1,
            "OrganizationName": "ActiGraph"
        },
        ...
    ]
