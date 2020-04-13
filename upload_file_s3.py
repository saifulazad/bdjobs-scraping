import boto3
import os
BUCKET_NAME = 'jobstext'


def upload_file(file_name):
    s3 = boto3.client('s3')
    key = os.path.join('joblinksfile', os.path.basename(file_name))
    try:
        s3_response = s3.put_object(Bucket=BUCKET_NAME, Key=key, Body=open(file_name, 'rb'))
    except Exception as e:
        raise IOError(e)


if __name__ == '__main__':
    upload_file('textfiles/1304.txt')
