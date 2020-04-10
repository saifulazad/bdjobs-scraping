import boto3
BUCKET_NAME = 'jobstext'
def upload_file(file_name):
    s3 = boto3.client('s3')
    try:
        s3_response = s3.put_object(Bucket=BUCKET_NAME, Key=file_name, Body= open(file_name, 'rb'))
    except Exception as e:
        raise IOError(e)
if __name__ == '__main__':
    upload_file('textfiles/0704.txt')