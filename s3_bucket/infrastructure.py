import aws_cdk as cdk
from constructs import Construct
from aws_cdk import aws_s3 as s3

class TestBucket(Construct):
    def __int__(self, scope: Construct, id_: str, *, bucket_name: str, **kwargs):
        super().__int__()(scope, id, **kwargs)

        self.bucket = s3.Bucket(self, bucket_name=self.bucket_name, removal_policy=cdk.RemovalPolicy)
        self.bucket_name = bucket_name





