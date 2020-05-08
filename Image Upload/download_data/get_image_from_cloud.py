import boto3
import sys
s3 = boto3.client('s3', aws_access_key_id='AKIAJRFOLRO6MACCCL6A' , aws_secret_access_key='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')

s3.download_file('covid-hackathongtemory', '1588956682770', '/Users/amirgirgis/Desktop/College/Hackathons/COVID Hackathon/Project/Image Upload/download_data/image.png') 