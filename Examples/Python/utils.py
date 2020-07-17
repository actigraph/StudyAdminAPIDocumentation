#dependencies for hashing
import hashlib
import hmac
import base64

#dependencies for date formatting
from datetime import datetime
from email.utils import formatdate

def HMACSHA256Base64(apiSecretKey,message):
    message = bytes(message, 'utf-8')
    secret = bytes(apiSecretKey, 'utf-8')
    signature = base64.b64encode(hmac.new(secret, message, digestmod=hashlib.sha256).digest())
    signature=signature.decode()
    return signature

def generate_headers(args,http_verb,resource_uri):
    '''
    formulate http headers
    '''
    cur_date= formatdate(timeval=None, localtime=False, usegmt=True)
    cur_date_iso=datetime.utcnow().isoformat().split('.')[0]+"Z"
    string_to_sign='\n'.join([http_verb,
                              '',
                              '',
                              cur_date_iso,
                              '/'.join([args.baseUrl,
                                        resource_uri])])
    
    signed_string=HMACSHA256Base64(args.apiSecretKey,string_to_sign)
    
    headers={}
    headers['Authorization']='AGS '+args.apiAccessKey+":"+signed_string
    headers['Date']=cur_date
    return headers
