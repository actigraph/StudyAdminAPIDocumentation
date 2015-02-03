Data Files
===

Download Url
---

Returns a pre-signed url along with the url expiration date to download a data file.

**Request:**

    GET /v1/datafiles/{dataFileId}/DownloadUrl

**Response:**

    
        {
            "DownloadURL": https://s3.amazonaws.com/acticloud ...,
            "URLExpirationDate": "2015-02-03T06:42:40.1654394Z"
        }
