Data Files
===

Subject Data Files
---
 Returns a list of previously uploaded data files for a specific subject. The 'dataType' argument is optional. By default, the data files returned will only be of the 'RAW' data type.

**Request:**

	GET /v1/subjects/{subjectId}/dataFiles

**Response:**

	 {
	  "RAW": [
	    {
	      "DataFileId": 5319,
	      "FileType": "RAW",
	      "FileSizeInBytes": "76698",
	      "UploadedDate": "2015-01-14T22:54:08Z",
	      "Metadata": {
	        "Filename": "MOS2A13510263_2015-01-14___16-54-07.gt3x",
	        "BeginOfData": "2015-01-14T16:19:00Z",
	        "EndOfData": "2015-01-14T22:54:07Z"
	      }
	    },
	    {
	      "DataFileId": 5323,
	      "FileType": "RAW",
	      "FileSizeInBytes": "1447186",
	      "UploadedDate": "2015-01-15T21:10:00Z",
	      "Metadata": {
	        "Filename": "MOS2A13510263_2015-01-15___15-09-58.gt3x",
	        "BeginOfData": "2015-01-14T22:56:00Z",
	        "EndOfData": "2015-01-15T21:09:59Z"
	      }
	    }...
	 }


Data File Download Url
---

Returns a pre-signed Url along with the Url's expiration date to download a specific data file.

**Request:**

    GET /v1/datafiles/{dataFileId}/DownloadUrl

**Response:**

    
    {
        "DownloadURL": https://s3.amazonaws.com/acticloud ...,
        "URLExpirationDate": "2015-02-03T06:42:40.1654394Z"
    }
