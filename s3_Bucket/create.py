import boto3

s3 = boto3.client("s3")

bucket_name = "prachi-demo-bucket-123456789"

s3.create_bucket(
    Bucket=bucket_name,
    CreateBucketConfiguration={
        "LocationConstraint": "eu-north-1"
    }
)

print("Bucket created successfully!")