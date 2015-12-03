

Uploads
===

GET Upload Details
---

Retrieve details of an upload by passing an Upload Int ID. 

**Request:**

    GET /v1/uploads/418

**Response:**

    {
    "DeviceUploaded": "CLE2B02130181",
    "SubjectId": "000035",
    "StudyName": "Screening Period",
    "DateUploaded": "2013-10-21T17:36:38Z",
    "DeviceBatteryVoltage": 4.2,
    "DeviceFirmware": "2.2.1",
    "ClientSoftwareName": "ActiSync",
    "ClientOSVersion": "Microsoft Windows NT 6.1.7601 Service Pack 1",
    "DeviceSampleRateHz": 30.0,
    "DeviceState": null,
    "DeviceHaltOrErrorReason": null,
    "TotalFilesUploaded": 1,
    "FilesUploaded": [{
        "FileType": "EPOCH",
        "FileName": null,
        "FileSizeInBytes": 0,
        "TotalRecords": 9956,
        "RecordsInserted": 9956,
        "Failed": false,
        "FailedReason": null
    }]
