#!/usr/bin/env python3
import os
import aws_cdk as cdk
from cdk_s3_simple.cdk_s3_simple_stack import CdkS3SimpleStack
app = cdk.App()
CdkS3SimpleStack(
  app, "CdkS3SimpleStack",
    env=cdk.Environment(
        account=os.getenv('CDK_DEPLOY_ACCOUNT'),
        region=os.getenv('CDK_DEPLOY_REGION')),
    )

app.synth()
