Study Admin API v1
===============

The ActiGraph Study Admin API provides access to the same core study and de-identified subject data that can be accessed in the [Study Admin](http://studyadmin.actigraphcorp.com) Web Portal.

Enabling API Access
-------------------
Please contact [sales@actigraphcorp.com](mailto:sales@actigraphcorp.com) for more information.

Technology Overview
-------------------
 * [HTTPS](http://tools.ietf.org/html/rfc2818) Any non-HTTPS request will result in a Forbidden response.
 * [JSON](http://tools.ietf.org/html/rfc4627)
 * [HMAC](http://tools.ietf.org/html/rfc2104) [SHA256](http://tools.ietf.org/html/rfc4634)

Authentication
--------------
Refer to the [Authentication](sections/authentication.md) section for specifics and examples on request signing.

Endpoints
---------
 * [Studies](sections/studies.md) Logical structures for grouping data for one or more subjects.
 * [Subjects](sections/subjects.md) Participants in studies.

Limits
------
A maximum requests per day may exist.  Contact [sales@actigraphcorp.com](mailto:sales@actigraphcorp.com) for details.

Formatting
----------
 * All dates will adhere to [ISO 8601](http://www.w3.org/TR/NOTE-datetime) and will be in UTC.
 * When the trailing 'Z' is withheld it will signify that the date should be interpreted in the subject's timezone.