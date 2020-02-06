Subjects
===

Subject Data Files
---
 Returns a list of previously uploaded data files for a specific subject. The 'dataType' argument is optional. By default, the data files returned will only be of the 'RAW' data type.

**Request:**

	GET /v1/subjects/{SubjectId}/dataFiles

**Response:**

	 {
	  "RAW": [
	    {
	      "DataFileId": 5319,
	      "UploadId": 5468,
	      "FileType": "RAW",
	      "FileSizeInBytes": "76698",
	      "UploadedDate": "2015-01-14T22:54:08Z",
	      "UploadStatus": "Upload Not Processed",
	      "Metadata": {
	        "Filename": "MOS2A13510263_2015-01-14___16-54-07.gt3x",
	        "BeginOfData": "2015-01-14T16:19:00Z",
	        "EndOfData": "2015-01-14T22:54:07Z"
	      }
	    },
	    {
	      "DataFileId": 5323,
	      "UploadId": 5478,
	      "FileType": "RAW",
	      "FileSizeInBytes": "1447186",
	      "UploadedDate": "2015-01-15T21:10:00Z",
	      "UploadStatus": "Upload Not Processed",
	      "Metadata": {
	        "Filename": "MOS2A13510263_2015-01-15___15-09-58.gt3x",
	        "BeginOfData": "2015-01-14T22:56:00Z",
	        "EndOfData": "2015-01-15T21:09:59Z"
	      }
	    }, 
	    ...
	  ]
	 }


Data File Download Url
---

Returns a Pre-Signed Url where a specific data file can be downloaded. The Url's expiration date is also included within the response.

**Request:**

    GET /v1/datafiles/{dataFileId}/DownloadUrl

**Response:**

    
    {
        "DownloadURL": "https://acticlouduploadsdev.blob.core.windows.net/study ...",
        "URLExpirationDate": "2015-02-03T06:42:40.1654394Z"
    }