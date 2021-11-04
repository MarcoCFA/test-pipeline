from aws_cdk import Stack
from constructs import Construct
from aws_cdk import pipelines

class Pipeline(Stack):
    def __init__(self, scope: Construct, construct_id: str, **kwargs):
        super().__init__(scope, construct_id, **kwargs)

        # Source
        github_repo = pipelines.CodePipelineSource.connection("MarcoCFA/test-pipeline", "master",
                                                              connection_arn="arn:aws:codestar-connections:us-east-1:225342792054:connection/0d952b85-4245-42bc-8619-a03128f24aa9")

        pipeline = pipelines.CodePipeline(self, "GitHubPipeline", cross_account_keys=False,
                                          synth=pipelines.ShellStep("Synth", input=github_repo,
                                                                    commands=["npm ci", "npm run build", "npx cdk synth"]))
