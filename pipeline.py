
from aws_cdk import Stack
from aws_cdk import pipelines
from aws_cdk import aws_codepipeline
from aws_cdk import aws_codebuild as codebuild


class Pipeline(Stack):
    def __init__(self, scope, id, *, env=None, synthesizer=None):
        super().__init__(scope, id, env=env, synthesizer=synthesizer)

        # Source
        github_repo = pipelines.CodePipelineSource.connection("MarcoCFA/test-pipeline", "master",
                                                              connection_arn="arn:aws:codestar-connections:us-east-1:225342792054:connection/0d952b85-4245-42bc-8619-a03128f24aa9")

        github_pipeline = pipelines.CodePipeline(self, "Pipeline",
                                                 synth=pipelines.ShellStep("Synth",input=github_repo),
                                                 commands=["npm ci", "npm run build", "npx cdk synth"])
