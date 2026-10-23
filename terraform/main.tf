terraform {
  required_version = ">= 1.16.0, < 2.0.0"

  required_providers {
    aws = {
      source  = "hashicorp/aws"
      version = "~> 6.0"
    }
  }
}

provider "aws" {
  region = "eu-north-1"
}

data "aws_lambda_function" "existing" {
  function_name = "aws-cloud-troubleshooter"
}

import {
  to = aws_lambda_function.troubleshooter
  id = "aws-cloud-troubleshooter"
}

