#!/usr/bin/env node
import "source-map-support/register";
import * as cdk from "@aws-cdk/core";
import { RythmPriceCdkStack } from "../lib/_rythm-price-cdk-stack";

const app = new cdk.App();
new RythmPriceCdkStack(app, "RythmPriceCdkStack", {
  env: {
    account: "778477161868",
    region: "us-west-2",
  },
});
