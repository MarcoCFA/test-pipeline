#!/usr/bin/env python3
import os

import aws_cdk as cdk
from test_pipeline.test_pipeline_stack import TestPipelineStack
from pipeline import Pipeline

APP_ENV = cdk.Environment(account="225342792054", region="us-east-1")

PIPELINE_ENV = cdk.Environment(account="225342792054", region="us-east-1")

app = cdk.App()

TestPipelineStack(app, "TestPipelineStack",env=APP_ENV)

Pipeline(app,"GitHubPipeline",env=PIPELINE_ENV)


app.synth()
