#!/usr/bin/env python3
import os

import aws_cdk as cdk

from test_pipeline.test_pipeline_stack import TestPipelineStack
from pipeline import Pipeline

PIPELINE_ENV = cdk.Environment(account="222222222222", region="us-east-1")

app = cdk.App()

TestPipelineStack(app, "TestPipelineStack",

    env=cdk.Environment(account=os.getenv('CDK_DEFAULT_ACCOUNT'), region=os.getenv('CDK_DEFAULT_REGION'))


    )

Pipeline(app,"GitHubPipeline",env=PIPELINE_ENV)

app.synth()
