from constructs import Construct
from aws_cdk import aws_s3 as s3

class TestBucket(Construct):
    def __int__(self, scope: Construct, id_: str, *, test_bucket_name: str):
        super().__int__()(scope,id)

        self.bucket_name = test_bucket_name




