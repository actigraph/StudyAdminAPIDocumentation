Authentication
==============

After API access has been enabled for your account, ActiGraph will generate you a shared key pair--one public "access key" and one private "secret key."  This key pair is what you will use to authenticate requests to the API as an alternative to using your username and password.  The access key will be included in the request to identify the account associated with the request.  And the secret key will be used to sign the request so ActiGraph can verify the request's integrity when received.  Therefore, your secret key will not be sent over-the-wire with each request.

In Case of Emergency
--------------------
Remember that anyone who has your key can see and change everything you have access to. So you want to guard that as well as you guard your username and password.  If this key pair becomes compromised we can deactivate it and provide you a new one.

Authorized Request
--------------------
All requests will be authorized by including the HTTP authorization header.  The scheme will be "AGS" to indicate ActiGraph's proprietary means of request formatting before implementing [HMAC](http://tools.ietf.org/html/rfc2104) [SHA256](http://tools.ietf.org/html/rfc4634).  The parameter is your access key followed by a colon followed by the signature.  See the following example:

    GET /v1/studies HTTP/1.1
    Host: studyadmin-api.actigraphcorp.com
    Date: Mon, 26 Mar 2007 19:37:58 +0000
    
    Authorization: AGS AKIAIOSFODNN7EXAMPLE:frJIUN8DYpKDtOLCwo//yllqDzg=

Signatures
----------
Following is pseudogrammar that illustrates the construction of the Authorization request header. (In the example, \n means the Unicode code point U+000A, commonly called newline).

    StringToSign = HTTP-Verb + "\n" +
    	Content-MD5 + "\n" +
    	Content-Type + "\n" +
    	Date + "\n" +
    	URLAndQueryString;

    Signature = Base64( HMAC-SHA256( SecretKey, UTF-8-Encoding-Of( StringToSign ) ) );

    Authorization = "AGS" + " " + AccessKey + ":" + Signature;

###GET Example
The following was generated with the access key of "testaccesskey" and the secret key "testsecretkey".

    String to Sign
    --------------
    GET\n\n\n2014-06-19T15:14:31Z\nhttps://studyadmin-api.actigraphcorp.com/v1/studies

    Request "Authorization" Header Value
    ------------------------------------
    AGS testaccesskey:J+9FTQTAkfGmUsaRmB/HBMJOXG+4Xqbo3drXBVQwZ4o=

###Using Base64 Encoding

HMAC request signatures must be Base64 encoded. Base64 encoding converts the signature into a simple ASCII string that can be attached to the request. Characters that could appear in the signature string like plus (+), forward slash (/), and equals (=) must be encoded if used in a URI. For example, if the authentication code includes a plus (+) sign, encode it as %2B in the request. Encode a forward slash as %2F and equals as %3D.
