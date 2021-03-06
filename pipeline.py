from aws_cdk import Stack
from constructs import Construct
from aws_cdk import pipelines
from deployment import Deployment


class Pipeline(Stack):
    def __init__(self, scope: Construct, construct_id: str, **kwargs):
        super().__init__(scope, construct_id, **kwargs)

        # Source
        github_repo = pipelines.CodePipelineSource.connection("MarcoCFA/test-pipeline", "master",
                                                              connection_arn="arn:aws:codestar-connections:us-east-1:225342792054:connection/0d952b85-4245-42bc-8619-a03128f24aa9")

        synth_step = pipelines.CodeBuildStep(
            "Synth",
            input=github_repo,
            install_commands=["./scripts/installs.sh"],
            commands=["npx cdk synth"],
            primary_output_directory="cdk.out"
        )

        pipeline = pipelines.CodePipeline(self, "GitHubPipeline", pipeline_name="github-pipeline",
                                          cross_account_keys=False, synth=synth_step)

        # Synth Step with ShellStep
        # pipeline = pipelines.CodePipeline(self, "GitHubPipeline", cross_account_keys=False, synth=pipelines.ShellStep("Synth", input=github_repo,commands=["npm ci", "npm run build", "npx cdk synth"]))

        ## Stages
        # Import deployment stage

        stage = Deployment(self, "DeployStack")

        # Add
        ### Security Check with manual approval
        pipeline.add_stage(stage,
                           pre=[pipelines.ConfirmPermissionsBroadening("Check", stage=stage)]) #, pipelines.ManualApprovalStep("Approve Security Changes")])
