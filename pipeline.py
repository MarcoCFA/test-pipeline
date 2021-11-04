from aws_cdk import Stack
from constructs import Construct
from aws_cdk import pipelines

class Pipeline(Stack):
    def __init__(self, scope: Construct, construct_id: str, **kwargs):
        super().__init__(scope, construct_id, **kwargs)



