import boto3

s3 = boto3.client('s3')

s3.upload_file(
    "sample.txt",      # Local file
    "prachi-demo-bucket-123456789",# S3 bucket name
    "demo.txt"         # Object name in S3
)

print("File uploaded successfully!")