from aws_cdk import (
    Stack,
    aws_s3 as _s3,
    RemovalPolicy
)
from constructs import Construct


class CdkS3SimpleStack(Stack):

  def __init__(self, scope: Construct, construct_id: str, **kwargs) -> None:
    super().__init__(scope, construct_id, **kwargs)

    _s3.Bucket(
      self, "Bucket",
      auto_delete_objects=True,
      removal_policy=RemovalPolicy.DESTROY
    )
