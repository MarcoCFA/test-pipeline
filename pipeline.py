
from aws_cdk import core as cdk
from aws_cdk import aws_codepipeline as pipelines
from aws_cdk import aws_codebuild as codebuild


class Pipeline(cdk.Stack):
    def __init__(self, scope: cdk.Construct, id_: str, **kwargs):
        super().__init__(scope, id_, **kwargs)

    # Source
    github_repo = pipelines.CodePipelineSource.connection("MarcoCFA/test-pipeline", "master", connection_arn="arn:aws:codestar-connections:us-east-1:225342792054:connection/0d952b85-4245-42bc-8619-a03128f24aa9")

    # Pipeline
    pipeline = pipelines.CodePipeline(self,"GitHubPipeline",cross_account_keys=False,synth=pipelines.ShellStep("Synth",input=github_repo,commands=["npm ci", "npm run build", "npx cdk synth"]))


