

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
    "ClientSoftwareVersion": "3.7.0.0",
    "ClientOSVersion": "Microsoft Windows NT 6.1.7601 Service Pack 1",
    "DeviceSampleRateHz": 30.0,
    "DeviceState": null,
    "DeviceHaltOrErrorReason": null,
    "TotalFilesUploaded": 1,
    "FilesUploaded": [{
        "DataFileId": 1286,
        "FileType": "EPOCH",
        "FileName": null,
        "FileSizeInBytes": 0,
        "TotalRecords": 9956,
        "RecordsInserted": 9956,
        "Failed": false,
        "FailedReason": null,
        "UploadStatus": "Upload Processing Completed"
    }]
    }

**Additional Note:**  The {SubjectId} field in this endpoint's response denotes the 'Subject Identifier' of the subject who performed the upload sync.


POST Upload
---

Add an upload to a subject by providing the required fields:
- Device Data (Epoch Data)
- Activity Monitor serial number 
- Activity Monitor firmware version
- Client Software Name

Other fields may be added to further assist with debugging of any possible problems. 

| Field         | Type         | Min  | Max  | Required      | Accepted Values  | Notes  |
| ------------- |--------------| -----| --------- |-------------| -------| -------------------|
| ActivityFiles|List<ActivityFile>|n/a|n/a|Yes||A List of the Activity Files that contains the epoch data
| ClientDetails|ClientDetails|n/a|n/a|Yes||An object that contains the details for a client
| DeviceDetails|DeviceDetails|n/a|n/a|Yes||An object that contains the details for an ActiGraph Activity Monitor
| DeviceData|String|> 0 bytes|10 MB|Yes||Base64 encoded string that holds the bytes of epoch data
| FileType|String|n/a|n/a|No|"EPOCH"|The type of epoch data. Upload Defaults as "EPOCH" file type if not filled in. 
| SoftwareName|String|n/a|n/a|Yes||The name of the software that is uploading the data
| SoftwareVersion|String|n/a|n/a|No||The version of the software that is uploading the data
| OSVersion|String|n/a|n/a|No||The version of the client's operating system
| CultureName|String|n/a|n/a|No||The culture of the client's computer
| MachineName|String|n/a|n/a|No||The name of the client's computer
| Username|String|n/a|n/a|No||The user of the client's computer
| DatetimePattern|String|n/a|n/a|No||The datetime pattern used by the client's computer
| SerialNumber|String|n/a|n/a|No||The unique identifier for an ActiGraph Activity Monitor
| BatteryVoltage|double|~3|~4.2|No||The battery voltage for an ActiGraph Activity Monitor
| SampleRate|double|n/a|n/a|No|30,40,50,60,70,80,90,100|The Sample Rate of the Activity Monitor
| DownloadedDate|DateTime|n/a|n/a|No||The date the epoch data was downloaded
| StartDate|DateTime|n/a|n/a|No| |The date the data collection started on the activity monitor
| StopDate|DateTime|n/a|n/a|No||The date the data  collection stopped on the activity monitor
| FirmwareVersion|String|n/a|n/a|Yes||The firmware version of the activity monitor
| HaltorErrorReason|String|n/a|n/a|No||The reason the activity monitor went into HALT mode (stopped collection of data)
| TimeOfDay|DateTime|n/a|n/a|No||The current time of the activity monitor
| State|String|n/a|n/a|No|"RESET","DELAY", "ACTIVE", "HALT", "CALIBRATE", "ERROR", "MOTHBALL", "DFU" |The state of the activity monitor


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
       
  
       
   
    
    
