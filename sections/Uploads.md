

Uploads
===

GET Upload Details
---

Retrieve details of an upload by passing an Upload Int ID. 

**Request:**

    GET /v1/UploadDetails/418

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
    
POST Upload
---

Add an upload to a subject by providing the required fields
- Device Data (Epoch Data)
- Activity Monitor serial number 
- Activity Monitor firmware version
- Client Software Name. 

Other fields may be added to further assist with debugging of any possible problems. 
    
**Request:**

    POST https://studyadmin-api.actigraphcorp.com/v1/Uploads
    
     {
    "ActivityFiles": [{
        "DeviceData": "HhBYhlxWCQC8tV5PyWX6SgEpHhCUhlxWCQBoO2cWuP22fgFO",
        "FileType": "EPOCH"
    }],
    "ClientDetails": {
        "SoftwareName": "Demo Client",
        "SoftwareVersion": "1.0",
        "OSVersion": "Windows 10",
        "CultureName": "English (United States)",
        "MachineName": "AGPC33",
        "Username": "Josh",
        "DatetimePattern": "dddd, MMMM d, yyyy h:mm:ss tt"
    },
    "DeviceDetails": {
        "SerialNumber": "TASFAKED03238",
        "BatteryVoltage": 4.15,
        "SampleRate": 30.0,
        "DownloadedDate": "2015-11-30T17:26:40.5766326Z",
        "StartDate": "2015-11-30T17:16:40.5766326Z",
        "StopDate": null,
        "FirmwareVersion": "1.4.0",
        "WatchdogResets": null,
        "HardFaultResets": null,
        "UnexpectedResets": null,
        "HaltorErrorReason": null,
        "TimeOfDay": "2015-11-30T17:26:40.5766326Z",
        "State": "Collecting"
    }
    }


**Response:**

       201 Created
       {
            "UploadId": 123
       }
       
       
   
    
    
