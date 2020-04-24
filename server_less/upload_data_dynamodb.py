import boto3
import json


def upload_company_information(event, context):
    dynamodb = boto3.resource('dynamodb')
    table = dynamodb.Table('it_company_address')
    table.put_item(
        Item= event
    )


