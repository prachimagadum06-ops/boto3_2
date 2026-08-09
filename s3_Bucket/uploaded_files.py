import boto3

s3 = boto3.client('s3')

response = s3.list_objects_v2(
    Bucket = "prachi-demo-bucket-123456789"
)

if "Contents" in response:
    for obj in response['Contents']:
        print(obj['Key'])
else:
    print("No")