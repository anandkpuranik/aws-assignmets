import boto3

from boto3.dynamodb.conditions import Key,Attr

def lambda_handler(event, context):
    client = boto3.resource("dynamodb")
    table = client.Table("StudentRecord")
    StudentRecord = table.scan(FilterExpression = Attr('StudentName').eq('Anand'))['Items']
    for user in StudentRecord:
        
        Total = int(user['Science Marks']) + int(user['Maths Marks']) + int(user['English Marks'])
        Percentage = int((Total/300)*100)
        Average = Total//3
        
    print('Total Marks : ',Total)    
    print('Average Marks : ',Average)
    print('Percentage : ',Percentage)
    
    table.update_item(
        
    Key={'StudentName': 'Anand'},
    UpdateExpression='SET Average = :avg, Percentage = :per',
                    ExpressionAttributeValues={
                        ':avg': Average,
                        ':per': Percentage
                    }
)
    

