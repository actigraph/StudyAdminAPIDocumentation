import argparse
import os
import requests
import urllib.parse
from utils import * 

def parse_args():
    args=argparse.ArgumentParser(description="Download raw Actigraph gt3x files from CentrePoint")
    args.add_argument("-baseUrl",default="https://studyadmin-api.actigraphcorp.com")
    args.add_argument("-apiAccessKey")
    args.add_argument("-apiSecretKey")
    args.add_argument("-studyId",help="if unsure, this can be obtained from the output of get_study_id.py")
    args.add_argument("-dirToStoreFiles",help="path to directory on your local machine where data is to be stored")
    args.add_argument("--newFilesOnly",action="store_true",default=False,help="If you set this flag, only .gt3x files that don't currently exist in -dirToStoreFiles will be downloaded")
    return args.parse_args() 

def main():
    args=parse_args()

    #if the directory where files are to be stored does not exist, create it 
    if not os.path.exists(args.dirToStoreFiles):
        os.makedirs(args.dirToStoreFiles)
    
    #get subject metadata
    resource_uri_subject_metadata="v1/studies/"+args.studyId+"/subjects"
    headers_subject_metadata=generate_headers(args,'GET',resource_uri_subject_metadata)
    subject_metadata=requests.get('/'.join([args.baseUrl,resource_uri_subject_metadata]),headers=headers_subject_metadata).json()

    #iterate through the subject id's to download their raw gt3x data
    for subject in subject_metadata:
        #get the subject id 
        subject_id=subject['Id']        
        subject_identifier_for_researchers=subject["SubjectIdentifier"]
        #create output folder for that subject's data
        if not os.path.exists("/".join([args.dirToStoreFiles,subject_identifier_for_researchers])):
            os.makedirs("/".join([args.dirToStoreFiles,subject_identifier_for_researchers]))

        # GET /v1/subjects/{SubjectId}/dataFiles
        resource_uri_subject_rawdata="v1/subjects/"+str(subject_id)+"/dataFiles"
        headers_subject_rawdata=generate_headers(args,'GET',resource_uri_subject_rawdata)
        subject_rawdata=requests.get('/'.join([args.baseUrl,resource_uri_subject_rawdata]),headers=headers_subject_rawdata).json()
        for raw_file in subject_rawdata['RAW']:
            raw_file_id=raw_file['DataFileId']
            
            #get the URL for file download
            resource_uri_rawdata_url="v1/datafiles/"+str(raw_file_id)+"/DownloadUrl"
            headers_rawdata_url=generate_headers(args,'GET',resource_uri_rawdata_url)
            rawdata_url=requests.get('/'.join([args.baseUrl,resource_uri_rawdata_url]),headers=headers_rawdata_url)
            try:
                rawdata_url=rawdata_url.json()
                raw_data_url_string=rawdata_url['DownloadURL']
            except:
                print("failed:")
                print(rawdata_url.text)
                print(str(raw_file_id)) 
                continue 
            #download the gt3x file
            unquoted_url_string=urllib.parse.unquote(raw_data_url_string)
            filename=unquoted_url_string.split("filename=")[-1].strip("\"")
            
            rawfile_request=requests.get(raw_data_url_string,allow_redirects=True)
            output_file='/'.join([args.dirToStoreFiles,subject_identifier_for_researchers,filename])
            
            if (args.newFilesOnly is True) and (os.path.exists(output_file)):
                #the file already exists, skip it
                print("already exists:"+str(output_file))
                continue
            else:
                #write the .gt3x file to disk
                open(output_file,'wb').write(rawfile_request.content)
                print("finished downloading:"+str(output_file))
            
if __name__=="__main__":
    main()
    