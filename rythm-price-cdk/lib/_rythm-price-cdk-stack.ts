import * as cdk from "@aws-cdk/core";
import * as ec2 from "@aws-cdk/aws-ec2";
import * as ecs from "@aws-cdk/aws-ecs";
import { PriceEcrStack } from "./price-ecr-stack";
import { PriceSvcStack } from "./price-svc-stack";

export class RythmPriceCdkStack extends cdk.Stack {
  constructor(scope: cdk.Construct, id: string, props?: cdk.StackProps) {
    super(scope, id, props);

    const vpc = ec2.Vpc.fromLookup(this, "RythmVpc", {
      tags: {
        application: "rythm",
      },
    });

    const cluster = ecs.Cluster.fromClusterAttributes(this, "id", {
      vpc: vpc,
      clusterName: "rythm-cluster",
      securityGroups: [],
    });

    new cdk.CfnOutput(this, "Cluster ARN", {
      value: cluster.clusterArn,
    });

    const priceEcrStack = new PriceEcrStack(this, "PriceEcrStack", {
      stackName: "price-ecr-stack",
      env: props?.env,
    });

    const priceSvcStack = new PriceSvcStack(this, "PriceSvcStack", {
      stackName: "price-svc-stack",
      env: props?.env,
      cluster: cluster,
    });
  }
}
