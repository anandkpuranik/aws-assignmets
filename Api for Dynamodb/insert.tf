
data "archive_file" "lambda1" {
  type        = "zip"
  source_file = "insert.py"
  output_path = "output/lambda1.zip"
}


resource "aws_lambda_function" "test_lambda1" {
  filename      = "output/lambda1.zip"
  function_name = "AddToTable1"
  role          = "arn:aws:iam::783323902162:role/aws-lambda-dynamodb"
  handler       = "insert.lambda_handler"

  # The filebase64sha256() function is available in Terraform 0.11.12 and later
  # For Terraform 0.11.11 and earlier, use the base64sha256() function and the file() function:
  # source_code_hash = "${base64sha256(file("lambda_function_payload.zip"))}"
  #source_code_hash = "${filebase64sha256("lambda_function_payload.zip")}"

  runtime = "python3.8"

}

