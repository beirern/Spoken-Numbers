import boto3
import os

from dotenv import load_dotenv

class S3:
    def __init__(self):
        load_dotenv()
        self.client = boto3.client('s3', 
            aws_access_key_id=os.environ["AWS_ACCESS_KEY_ID"],
            aws_secret_access_key=os.environ["AWS_SECRET_ACCESS_KEY"], 
            region_name='us-east-1'
        )

    def get_presigned_url(self, s3_uri, bucket):
        last_index = s3_uri.rindex('/')
        object_key = s3_uri[last_index+1:]
        
        print(bucket)
        presigned_url = self.client.generate_presigned_url(
            ClientMethod='get_object',
            Params={
                'Bucket': bucket,
                'Key': object_key
            },
            ExpiresIn=3600
        )

        return presigned_url