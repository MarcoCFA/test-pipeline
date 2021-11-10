from s3_bucket.infrastructure import TestBucket
from aws_cdk import Stage
from aws_cdk import Stack
from constructs import Construct

class Deployment(Stage):
    def __init__(self, scope: Construct, construct_id: str, bucket_name: str, **kwargs):
        super().__init__(scope, construct_id, **kwargs)

        deployStack = Stack(self, "deployStack")

        # Add bucket to the stack
        my_bucket = TestBucket(deployStack, bucket_name)
