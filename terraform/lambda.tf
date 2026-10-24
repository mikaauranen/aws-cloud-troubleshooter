# __generated__ by Terraform
# Please review these resources and move them into your main configuration files.

# __generated__ by Terraform
resource "aws_lambda_function" "troubleshooter" {


  lifecycle {
    prevent_destroy = true
    ignore_changes  = [filename]
  }


  architectures = ["x86_64"]
  filename      = "${path.module}/../lambda-deployment.zip"

  function_name                  = "aws-cloud-troubleshooter"
  handler                        = "lambda_function.lambda_handler"
  layers                         = []
  memory_size                    = 128
  package_type                   = "Zip"
  region                         = "eu-north-1"
  reserved_concurrent_executions = -1
  role                           = aws_iam_role.troubleshooter_execution.arn
  runtime                        = "python3.13"
  skip_destroy                   = false
  tags                           = {}
  tags_all                       = {}
  timeout                        = 30
  ephemeral_storage {
    size = 512
  }
  logging_config {
    log_format = "Text"
    log_group  = "/aws/lambda/aws-cloud-troubleshooter"
  }
  tracing_config {
    mode = "PassThrough"
  }
}
