Webhooks
===

GET Webhook History Listing
---

Retrieve the history of webhooks that were called for a study, starting from a given date. 

**Request:**

```
GET /v1/Webhooks/History?studyId=12345&startDate=2015-12-13T14:52:00Z
```

**Response:**
```json
[
  {
    "Id": 76,
    "WebhookId": 23,
    "WebhookDeliveryHash": "232f0706-83e3-42ba-4b63-09504d25e5c7",
    "WebhookEvent": "upload",

    "Request": {
      "Headers": "{\"Content-Type\":[\"application/json\"],\"X-ActiGraph-Webhook-id\":[\"23\"],\"X-ActiGraph-Event\":[\"upload\"],\"X-ActiGraph-Delivery\":[\"232f0706-83e3-42ba-4b63-09504d25e5c7\"],\"X-ActiGraph-Signature\":[\"w9ysWVQTwZiwVj+EaNEBk4Eh0/XKvEf56CxrMw7L5eM=\"],\"User-Agent\":[\"ActiGraph-Hookshot/1.0\"],\"Host\":[\"requestb.in\"],\"Content-Length\":[\"86\"],\"Expect\":[\"100-continue\"]}",
      "Body": "{\"random_guid\":\"f38146bd-583f-4a3c-a59c-ace063684b4b\",\"webhook_id\":\"23\",\"test\":\"ping\"}"
    },

    "Response": {
      "ResponseCode": 200,
      "Headers": "{\"Connection\":[\"keep-alive\"],\"Sponsored-By\":[\"https://www.runscope.com\"],\"Content-Length\":[\"2\"],\"Content-Type\":[\"text/html; charset=utf-8\"],\"Date\":[\"Mon, 14 Dec 2015 18:20:16 GMT\"],\"Server\":[\"gunicorn/19.3.0\"],\"Via\":[\"1.1 vegur\"]}",
      "Body": "ok"
    },

    "Created": "2015-12-14T18:20:05Z"

  },
]
```

**Fields:**

Field|Type|Description
-----|----|-----------
Id|int|The unique ID of this webhook history entry.
WebhookId|int|The unique ID of the webhook that made this entry.
WebhookDeliveryHash|string|The unique hash of this webhook history entry.
WebhookEvent|string|The name of the event that triggered this webhook.
Request|object|Contains the headers and body of the request that ActiGraph sent to the webhook's URL
Request.Headers|string|A serialized JSON string of the request headers.
Request.Body|string|The body of the request sent, typically in JSON.  
Response|object|Contains the response code, headers and body of the response ActiGraph received from the webhook's URL.
Response.ResponseCode|int|The HTTP Code received from the webhook's URL. For more information about HTTP codes, [click here](http://www.w3.org/Protocols/rfc2616/rfc2616-sec10.html "HTTP Codes").
Response.Headers|string|A serialized JSON string of the response headers.
Response.Body|string|The body of the response received, mixed values expected.
Created|string|The date and time this webhook was triggered. The format is:  "yyyy-MM-ddTHH:mm:ssZ"