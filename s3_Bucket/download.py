import boto3

s3 = boto3.client("s3")

s3.download_file(
    "prachi-demo-bucket-123456789",  # Bucket name
    "demo.txt",                      # Object key in S3
    "demo.txt"                       # Local filename to save as
)