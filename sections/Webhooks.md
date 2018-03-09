
Webhooks
===

Webhooks History
---

Returns a history log of Webhook requests for a given study.

**Request:**

    GET /v1/webhooks/history?studyId=<studyId>

#### Request Properties ####

Field|Type|Required|Default Value|Description|Example Request URI
|-----|----|---------|------------|-----------|-------------------|
startDate|DateTime|no|`null`|Start Date (UTC) to filter webhook requests on or after the given date/time|/v1/webhooks/history?studyId=9&startDate=YYYY-MM-DDTHH:MM:SS|
endDate|DateTime|no|`null`|End  Date (UTC) to filter webhook requests on or before the given date/time|/v1/webhooks/history?studyId=9&endDate=YYYY-MM-DDTHH:MM:SS
IncludeResponseCodes|Number|no|`null`|Filter to include webhooks requests with only specified response codes|/v1/webhooks/history?studyId=9&IncludeResponseCodes=200
ExcludeResponseCodes|Number|no|`null`|Filter to exclude webhook requests with specified response codes|/v1/webhooks/history?studyId=9&&ExcludeResponseCodes=200



**Response:**
[
    {
      "Id": 3924,
      "WebhookId": 14,
      "WebhookDeliveryHash": "0f9G3fde-8Baf-0c83-1591-517307kpp19c",
      "WebhookEvent": "upload",
      "Request": {
        "Headers": "{\"Content-Type\":[\"application/json\"],\"User-Agent\":[\"ActiGraph-Hookshot/1.0\"],\"X-ActiGraph-Webhook-id\":[\"14\"],\"X-ActiGraph-Event\":[\"upload\"],\"X-ActiGraph-Delivery\":[\"0f9G3fde-8Baf-0c83-1591-517307kpp19c\"],\"X-Client-Cert-Used\":[\"false\"],\"Host\":[\"hostaddress.host.com\"],\"Content-Length\":[\"272\"],\"Expect\":[\"100-continue\"]}",
        "Body": "{\"status\":\"completed\",\"firstEpochUTC\":\"2018-03-08T00:20:00.0000000\",\"firstEpochSubjectTZ\":\"2018-03-08T05:50:00.0000000\",\"lastEpochUTC\":\"2018-03-08T00:34:00.0000000\",\"lastEpochSubjectTZ\":\"2018-03-08T06:04:00.0000000\",\"uploadId\":\"362288\",\"studyId\":\"8\",\"subjectId\":\"2358\"}"
      },
      "Response": {
        "ResponseCode": 200,
        "Headers": "{\"Connection\":[\"keep-alive\"],\"Content-Length\":[\"0\"],\"Date\":[\"Thu, 08 Mar 2018 00:37:55 GMT\"],\"Server\":[\"Apache-Coyote/1.1\"]}",
        "Body": ""
      },
      "Created": "2018-03-08T00:37:55"
    },
  ...
]
