# Popcorn
Popcorn is a command-line tool for managing `.nc` files in the Polarplot dedicated S3 bucket. The script supports uploading and downloading files, listing files, and subscribing to notifications.
## Requirements
- Python 3
- boto3 library

## Features
- Upload and download .nc files to/from the Polarplot dedicated S3 bucket
- List available files in the bucket
- Subscribe to bucket notifications
## Installation
You can either install the tool from pip using ``` pip install d-popcorn``` or by following the steps below : 

- Clone the repository: git clone https://github.com/YOUR_USERNAME/puploader.git
- Change into the directory: cd popcorn
- Install the required libraries: pip install -r requirements.txt
- Add your AWS credentials to your environment variables or to your ~/.aws/credentials file. For example:


``` shell
aws_access_key_id = YOUR_ACCESS_KEY_ID
aws_secret_access_key = YOUR_SECRET_ACCESS_KEY
```

## Usage
### Upload a file
To upload a file, use the following command:


```shell
popcorn /path/to/file.nc upload --project PROJECT_CODE --file-description "Description of the file" --client CLIENT_NAME --project-description "One sentence project description" file_to_upload.nc 
```
Replace PROJECT_CODE, CLIENT_NAME, and /path/to/file.nc with the appropriate values for your file.

PROJECT_CODE should respect the prefixes used internally : ["SCE", "RDX", "RDI", "RDS", "OCX", "SQD", "RBK", "SHY", "THX", "FG"]


### List uploaded files
To list all uploaded files and their metadata, use the following command:


```shell
popcorn list
```
This will display a list of all files that have been uploaded to the bucket, along with their metadata.

You can also list specific project files:

```shell
popcorn list --project PROJECT_CODE
```

### Download a file
```shell
popcorn download HASH_VALUE --output /path/to/output/directory
```

### Subscribe to bucket notifications  

```shell
popcorn subscribe --email your-email@example.com
```

### Remove a subscription

```shell
popcorn subscribe --remove your-email@example.com
```

### List active subscriptions

```shell
popcorn subscribe --list
```

## License
This tool is licensed under the MIT License. See the LICENSE file for details.

Copyright (c) D-ICE ENGINEERING