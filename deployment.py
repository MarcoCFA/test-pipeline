from s3_bucket.infrastructure import TestBucket
from aws_cdk import Stage
from aws_cdk import Stack
from constructs import Construct

class Deployment(Stage):
    def __init__(self, scope: Construct, construct_id: str, **kwargs):
        super().__init__(scope, construct_id, **kwargs)

        deployStack = Stack(self, "deployStack")

        test_bucket_name = 'my-test-bucket-1981'

        # Add bucket to the stack
        test_bucket = TestBucket(deployStack, test_bucket_name)
