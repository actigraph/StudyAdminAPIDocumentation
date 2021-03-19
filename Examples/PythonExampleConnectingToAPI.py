#import requests
#from requests.auth import HTTPBasicAuth
# Added to remove InsecureRequestWarning
import requests
from requests.packages.urllib3.exceptions import InsecureRequestWarning
# Removed this one
#from requests_oauthlib import OAuth1
import hmac
import hashlib
import base64
import datetime
import time
import array
import json

requests.packages.urllib3.disable_warnings(InsecureRequestWarning)

def BuildRequestHeader( httpMethod, Uri, apiAccessKey, apiSecretKey ):
    "Builds the Request Header Dictionary"
    
    # dictionaty for request header parameters
    headerDictionary = {}
    
    # set content-type for POST and PUT operations
    if httpMethod == 'POST' or httpMethod == 'PUT':
        headerDictionary['content-type'] = 'application/json'

    # retrieve current timestamp in UTC 
    currentUtcTime = datetime.datetime.utcnow()

    # perform signing
    stringToSign = str(httpMethod + "\n\n\n" + currentUtcTime.strftime('%Y-%m-%dT%H:%M:%SZ') + "\n" + Uri).encode('utf-8')
    digest = hmac.new(apiSecretKey, stringToSign, hashlib.sha256).digest()
    signature = base64.b64encode(digest).decode('utf-8')

    # Add authorization property to header dictionary
    headerDictionary['Authorization'] = "AGS" + " " + apiAccessKey + ":" + signature

    # Add date property to header dictionart
    headerDictionary['Date'] = currentUtcTime.strftime('%a, %d %b %Y %H:%M:%S +0000')

    return headerDictionary;

def SendRequest ( httpMethod, Uri, apiAccessKey, apiSecretKey ):
    "Sends request to study admin api and returns response"
    headerDictionary = BuildRequestHeader(httpMethod, Uri, apiAccessKey, apiSecretKey )
    response = requests.get(Uri, headers=headerDictionary, verify=False)
    return response;

baseUri = 'https://studyadmin-api.actigraphcorp.com'
api_access_key = '<api access key>'
api_secret = str('<api access key>').encode('utf-8')

# Get Studies Endppoint (returns list of studies)
resourceUri = '/v1/studies'
response = SendRequest('GET', baseUri + resourceUri, api_access_key, api_secret) 
print ('response: ' )
print ( response.status_code )
print ( response.json() )


## Get Study Endpoint (retuns information on specific study)
#studyId = '<Study Id Goes Here>'
#resourceUri = '/v1/studies/' + studyId 
#response = SendRequest('GET', baseUri + resourceUri, api_access_key, api_secret)
#print ( response.json() )

## Get Study Subjects Endpoint (returns subjects within specific study)
#studyId = '<Study Id Goes Here>'
#resourceUri = '/v1/studies/' + studyId + '/subjects'
#response = SendRequest('GET', baseUri + resourceUri, api_access_key, api_secret)
#print ( response.json() )

## Get Sites Endpoint (returns list of sites) 
#resourceUri = '/v1/sites'
#response = SendRequest('GET', baseUri + resourceUri, api_access_key, api_secret)
#print ( response.json() )

## Get Subject Endpoint (returns information on specific subject)
#subjectId = '<Subject Id goes here>'
#resourceUri = '/v1/subjects/' + subjectId
#response = SendRequest('GET', baseUri + resourceUri, api_access_key, api_secret)
#print ( response.json() )
