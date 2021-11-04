#!/usr/bin/env python3
import os

import aws_cdk as cdk
from test_pipeline.test_pipeline_stack import TestPipelineStack
from pipeline import Pipeline

PIPELINE_ENV = cdk.Environment(account="225342792054", region="us-east-1")

app = cdk.App()

TestPipelineStack(app, "TestPipelineStack",

    env=cdk.Environment(account="225342792054", region=os.getenv("us-east-1"))


    )

Pipeline(app,"GitHubPipeline",env=PIPELINE_ENV)


app.synth()
