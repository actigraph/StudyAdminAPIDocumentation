These scripts utilize the [CentrePoint V2 API](https://github.com/actigraph/StudyAdminAPIDocumentation) do download raw Actigraph .gt3x files


### Step 1: Identify the ID of your study of interest

```
python get_study_id.py -apiAccessKey xxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx -apiSecretKey xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxx -outf studies.txt
```

In [studies.txt](Python/Studies.txt) , you will see the following:

```
[
  {
    "Id": xxx,
    "Name": "MyStudyName",
    "DateCreated": "2017-09-12T18:09:21.827Z",
    "OrganizationName": "MyOrganization"
  }
]
```

### Step 2: Download gt3x data files

Refer to [download_data.py](Python/download_data.py), [get_study_id.py](Python/get_study_id.py), and [utils.py](Python/utils.py)

Now that you have identified the study id of interest (the "Id" entry in the above-generated studies.txt), you can retrieve the raw .gt3x files for all subjects associated with that study:



```
python download_data.py -apiAccessKey xxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx -apiSecretKey xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxx -studyId xxx -dirToStoreFiles myOutputDir

#optionally add the --newFilesOnly flag to only download files that don't exist in myOutputDir. This is useful if additional files are added to the study between downloads.
python download_data.py -apiAccessKey xxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx -apiSecretKey xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxx -studyId xxx -dirToStoreFiles myOutputDir --newFilesOnly

```
* Pass the "Id" value from your studies.txt file to the `-studyId` flag
* "dirToStoreFiles" is a path on your machine where the gt3x files will be stored, if this path does not exist, the code will create it.

The output files will be organized by subject in "myOutputDir" (substitute this with your download location).

