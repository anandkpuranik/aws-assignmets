
resource "aws_dynamodb_table_item" "itemName" {
  table_name = "${aws_dynamodb_table.StudentRecord.name}"
  hash_key   = "${aws_dynamodb_table.StudentRecord.hash_key}"

  item = <<ITEM
    {
    "studentName": {"S": "Anandp"},
    "englishMarks": {"N": "80"},
    "scienceMarks": {"N": "90"},
    "mathsMarks": {"N": "100"}
    }
ITEM
}

resource "aws_dynamodb_table" "StudentRecord" {
  name           = "StudentRecord"
  billing_mode   = "PROVISIONED"
  read_capacity  = 2
  write_capacity = 2
  hash_key       = "studentName"

  attribute {
    name = "studentName"
    type = "S"
  }
}
