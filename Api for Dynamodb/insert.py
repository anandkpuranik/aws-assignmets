import boto3
dynamodb = boto3.resource('dynamodb')
table = dynamodb.Table('StudentRecord')
def lambda_handler(event, context):
    response = table.put_item(
    Item={
        'StudentName':'Anrudhha',
        'English Marks':'80',
         'Maths Marks':'60',
        'Science Marks':'90',
        
        'StudentName':'amey',
        'English Marks':'30',
         'Maths Marks':'35',
        'Science Marks':'60'
        
    }
)
    