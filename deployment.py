from s3_bucket.infrastructure import TestBucket
import aws_cdk as cdk
from aws_cdk import Stack
from constructs import Construct


class Deployment(Stage):
    def __init__(self, scope: Construct, id_: str, *, test_bucket_name: str, **kwargs):
        super().__int__()(scope, id, **kwargs)

        deployStack = Stack(self, "deployStack")

        test_bucket_name = 'my-test-bucket-1981'

        # Add bucket to the stack
        test_bucket = TestBucket(deployStack, test_bucket_name)
