import argparse
import os
import requests
import urllib.parse
from utils import *
import json

def parse_args():
    args=argparse.ArgumentParser(description="Download raw Actigraph gt3x files from CentrePoint")
    args.add_argument("-baseUrl",default="https://studyadmin-api.actigraphcorp.com")
    args.add_argument("-apiAccessKey")
    args.add_argument("-apiSecretKey")
    args.add_argument("-outf") 
    return args.parse_args() 

def main():
    args=parse_args()

    #get metadata for studies the user has access to 
    resource_uri_study_metadata="v1/studies"
    headers_study_metadata=generate_headers(args,'GET',resource_uri_study_metadata)
    study_metadata=requests.get('/'.join([args.baseUrl,resource_uri_study_metadata]),headers=headers_study_metadata).json()
    with open(args.outf,'w') as f:
        f.write(json.dumps(study_metadata,indent=2)) 
            
if __name__=="__main__":
    main()
    