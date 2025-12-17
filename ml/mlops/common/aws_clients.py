import boto3


def s3_client(region_name="ap-southeast-2"):
    return boto3.client("s3", region_name=region_name)
