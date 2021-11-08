from aws_cdk import Stack
from constructs import Construct
from aws_cdk import aws_s3 as s3

class TestPipelineStack(Stack):

    def __init__(self, scope: Construct, construct_id: str, **kwargs) -> None:
        super().__init__(scope, construct_id, **kwargs)

        # The code that defines your stack goes here
        bucket = s3.Bucket(self, "my-test-bucket-1",bucket_name="my-test-bucket")
