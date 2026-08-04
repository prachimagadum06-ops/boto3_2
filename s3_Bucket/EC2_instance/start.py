import boto3

ec2 = boto3.client("ec2")

ec2.start_instances(
    InstanceIds=["i-0123456789abcdef0"]
)

print("Instance started")