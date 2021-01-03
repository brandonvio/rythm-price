import * as cdk from "@aws-cdk/core";
import * as ec2 from "@aws-cdk/aws-ec2";
import * as ecs from "@aws-cdk/aws-ecs";
import * as ecr from "@aws-cdk/aws-ecr";
import * as iam from "@aws-cdk/aws-iam";

interface PriceSvcStackProps extends cdk.StackProps {
  cluster: ecs.Cluster;
}

export class PriceSvcStack extends cdk.Stack {
  constructor(scope: cdk.Construct, id: string, props: PriceSvcStackProps) {
    super(scope, id, props);

    const repo = ecr.Repository.fromRepositoryName(this, "PriceSvcRepo", "rythm-svc-price");

    // Create the role to run Tasks.
    const priceTaskRole = new iam.Role(this, "PriceTaskRole", {
      assumedBy: new iam.ServicePrincipal("ecs-tasks.amazonaws.com"),
      roleName: "rythm-price-svc-role",
      managedPolicies: [
        iam.ManagedPolicy.fromManagedPolicyArn(
          this,
          "SecretsManager",
          "arn:aws:iam::aws:policy/SecretsManagerReadWrite"
        ),
      ],
    });

    // Price Service Task.
    const taskDefinition = new ecs.TaskDefinition(this, "PriceTaskDef", {
      memoryMiB: "512",
      cpu: "256",
      networkMode: ecs.NetworkMode.AWS_VPC,
      compatibility: ecs.Compatibility.EC2_AND_FARGATE,
      taskRole: priceTaskRole,
    });

    taskDefinition.addContainer("PriceContainer", {
      image: ecs.ContainerImage.fromEcrRepository(repo, "latest"),
      memoryLimitMiB: 512,
      logging: new ecs.AwsLogDriver({ streamPrefix: "PriceService" }),
      environment: {
        STAGE: "prod",
      },
    });

    const service = new ecs.FargateService(this, "PriceService", {
      serviceName: "rythm-price-service",
      cluster: props.cluster,
      taskDefinition,
      desiredCount: 1,
    });
  }
}
