from aws_cdk import Stack
from constructs import Construct
from aws_cdk import pipelines

class Pipeline(Stack):
    def __init__(self, scope: Construct, id: str, *, env=None, **kwargs):
        super().__init__(scope, id, **kwargs)

        # Source
        github_repo = pipelines.CodePipelineSource.connection("MarcoCFA/test-pipeline", "master",
                                                              connection_arn="arn:aws:codestar-connections:us-east-1:225342792054:connection/0d952b85-4245-42bc-8619-a03128f24aa9")

        github_pipeline = pipelines.CodePipeline(self, "Pipeline",
                                                 synth=pipelines.ShellStep("Synth",input=github_repo),
                                                 commands=["npm ci", "npm run build", "npx cdk synth"])
