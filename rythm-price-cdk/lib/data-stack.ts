import * as cdk from "@aws-cdk/core";
import * as ec2 from "@aws-cdk/aws-ec2";
import * as ecs from "@aws-cdk/aws-ecs";
import * as ecr from "@aws-cdk/aws-ecr";
import * as iam from "@aws-cdk/aws-iam";

export class PriceEcrStack extends cdk.Stack {
  constructor(scope: cdk.Construct, id: string, props?: cdk.StackProps) {
    super(scope, id, props);

    // Create repositories in ECR.
    const priceSvcRepo = new ecr.Repository(this, "priceSvcRepo", {
      repositoryName: "rythm-svc-price",
    });
  }
}
