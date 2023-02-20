'''
This python program is a basic example of how use the AWS S3.
This method will do the basic options with S3.

This program assumes you have already setup the followings:
1. AWS account with IAM user + Access Keys with S3 full acces Permission
'''

import boto3
from datetime import date

#refer to the aws boto3 documentation for more details.
def connect():
    mys3Obj = boto3.resource("s3", region_name="us-east-1", aws_access_key_id='PUT YOUR KEY', aws_secret_access_key='PUT YOUR SECRET')
    bucket = mys3Obj.Bucket('saran-myfiles')
    if bucket.creation_date:
        print("The bucket exists")
    else:
        print("The bucket does not exist")
    return mys3Obj


#After the successful conection lets upload a file from the local computer to S3 with the specific filename (aka KEY)
def create(mys3Obj):
    mys3Obj.Bucket('saran-myfiles').upload_file('/Users/saran/Desktop/dummy.pdf', 'dummy.pdf')

#After the successful coneection lets download a file from the local computer to S3 with the specific filename (aka KEY)
def read(mys3Obj):
    try:
        myFile = mys3Obj.Bucket('saran-myfiles').Object('dummy.pdf').get()
        print("file found")
    except:
        print("file not found")

#After the successful coneection lets modify a file from the local computer to S3 with the specific filename (aka KEY)
def update(mys3Obj):
    mys3Obj.Bucket('saran-myfiles').upload_file('/Users/saran/Desktop/multiplication-3-digits-by-1-digit-5.pdf', 'dummy.pdf')


#After the successful coneection lets delete a file from the local computer to S3 with the specific filename (aka KEY)
def delete(mys3Obj):
    mys3Obj.Bucket('saran-myfiles').delete_objects(Delete={"Objects": [{"Key": "dummy.pdf"}]})

#After the successful coneection lets download a file from the local computer to S3 with the specific filename (aka KEY)
def download(mys3Obj):
    mys3Obj.Bucket('saran-myfiles').download_file(Key="dummy.pdf", Filename="/Users/saran/Desktop/download-aws.pdf")


'''
All python program starts from the main functions as follows
'''            
if __name__ == "__main__":
    #As it starts, this program creates DynamoDB refer by the following connect method.
    mys3Obj = connect()
    #create(mys3Obj)    
    #read(mys3Obj)
    #update(mys3Obj)
    #delete(mys3Obj)
    download(mys3Obj)
    