#!/usr/bin/env python3
import os

import aws_cdk as cdk
from deployment import Deployment
from pipeline import Pipeline

APP_ENV = cdk.Environment(account="225342792054", region="us-east-1")

PIPELINE_ENV = cdk.Environment(account="225342792054", region="us-east-1")

app = cdk.App()

# Add deployment to app
Deployment(app, "TestPipelineStack", env=APP_ENV)

# Add app to pipeline
Pipeline(app, "GitHubPipeline", env=PIPELINE_ENV)


app.synth()
