import boto3
from boto3.dynamodb.conditions import Attr

dynamodb = boto3.resource('dynamodb')
table = dynamodb.Table('stocks')

response = table.scan(
    FilterExpression=Attr('productId').eq("138695381")
)

items = response['Items']

if len(items) == 0:


print(item)
