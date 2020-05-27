
### Connecting to Study Admin API - C# Demo ###

The following is a C# example of the source code necessary to perform a request to the [List Studies](https://github.com/actigraph/StudyAdminAPIDocumentation/blob/master/sections/studies.md#list-studies) API call.
   
```c#
string baseUrl = "https://studyadmin-api.actigraphcorp.com";
string resourceUri = "/v1/studies";
string apiAccessKey = "<Api Access Key>";
string apiSecretKey = "<Api Secret Key>";

HttpResponseMessage resposne = SendRequestAsync(baseUrl, resourceUri, HttpMethod.Get, null, apiAccessKey, apiSecretKey).Result;
```
	
**Example of method Sending Request to Study Admin API**
```c#
public static async Task<HttpResponseMessage> SendRequestAsync(string baseUrl, string resourceUri, HttpMethod httpVerb, string requestContentJson, string apiAccessKey, string apiSecretKey)
{
    string endpointUri = baseUrl + resourceUri;
    
     HttpClient client = client = new HttpClient()
     {
         BaseAddress = new Uri(baseUrl)
     };

     HttpRequestMessage httpRequest = new HttpRequestMessage(httpVerb, endpointUri);
    
    try
    {   
        // If 'post' or 'put' request, set content-type in request header to 'application/json'
        if (httpVerb.Equals(HttpMethod.Post) || httpVerb.Equals(HttpMethod.Put))
        {
            httpRequest.Content = new StringContent(requestContentJson, Encoding.UTF8);
            httpRequest.Content.Headers.ContentType = new System.Net.Http.Headers.MediaTypeHeaderValue("application/json");
        }

        BuildRequestHeader(ref httpRequest, apiAccessKey, apiSecretKey);
        
        return await client.SendAsync(httpRequest);

	}
    catch (Exception)
    {
        throw;
    }
    finally
    {
        httpRequest.Dispose();
        client.Dispose();
    }
}
```

**Example of method building request header**
```c#
public static void BuildRequestHeader(ref HttpRequestMessage requestMessage, string apiAccessKey, string apiSecretKey)
{       
    // set date in the request header (must be done prior to signature generation)
    requestMessage.Headers.Date = DateTime.UtcNow;

    var signature = Sign(requestMessage, apiSecretKey);
    requestMessage.Headers.Authorization = new System.Net.Http.Headers.AuthenticationHeaderValue("AGS", string.Format("{0}:{1}", apiAccessKey, signature));
}
```

**Example of Request Signing method**
```c#
public static string Sign(HttpRequestMessage request, string apiSecretKey)
{
    var md5 = "";
    if (request.Content != null && request.Content.Headers.ContentMD5 != null && request.Content.Headers.ContentMD5.Length > 0)
        md5 = Encoding.UTF8.GetString(request.Content.Headers.ContentMD5);

    var type = "";
    if (request.Content != null && request.Content.Headers.ContentType != null)
        type = request.Content.Headers.ContentType.MediaType;

    var stringToSign = request.Method + "\n" +
        md5 + "\n" +
        type + "\n" +
        (request.Headers.Date.HasValue ? request.Headers.Date.Value.ToString("s") + "Z\n" : "\n") +
        request.RequestUri.ToString();

    return HMACSHA256Base64(apiSecretKey, stringToSign);
}
```

**Example of method performing HMAC SHA256 Encrypted Hash**
```c#
public static string HMACSHA256Base64(string apiSecretKey, string message)
{
    var hash = new HMACSHA256(Encoding.UTF8.GetBytes(apiSecretKey));
    return Convert.ToBase64String(hash.ComputeHash(Encoding.UTF8.GetBytes(message)));
}
```
