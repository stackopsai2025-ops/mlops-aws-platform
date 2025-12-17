from aws_cdk import Stack
from constructs import Construct


class DataStack(Stack):
    def __init__(self, scope: Construct, construct_id: str, **kwargs):
        super().__init__(scope, construct_id, **kwargs)
        # TODO: S3 buckets, Glue, Athena
from aws_cdk import Stack
from constructs import Construct


class DataStack(Stack):
    def __init__(self, scope: Construct, construct_id: str, **kwargs):
        super().__init__(scope, construct_id, **kwargs)
        # TODO: Add S3 buckets / Glue / Athena resources
