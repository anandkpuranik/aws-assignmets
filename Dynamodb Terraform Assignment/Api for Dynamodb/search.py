import boto3
from boto3.dynamodb.conditions import Key,Attr
dynamodb = boto3.resource('dynamodb')
table = dynamodb.Table('StudentRecord')
def lambda_handler(event, context):
    percent = event['percent']
    Student_Records = table.scan(FilterExpression = Attr('Percentage').eq(percent))['Items']
    return Student_Records