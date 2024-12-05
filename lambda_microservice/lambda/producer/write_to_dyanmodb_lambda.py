from __future__ import print_function

import json
import os
import uuid

import boto3
from botocore.exceptions import ClientError

dynamodb = boto3.resource("dynamodb")
TABLE_NAME = os.environ["TABLE_NAME"]

def lambda_handler(event, context):
    table = dynamodb.Table(TABLE_NAME)

    try:
        username = event["username"]
        password = event["password"]

        table.put_item(
            Item={
                "id": str(uuid.uuid4()),
                "username": username,
                "password": password,
            }
        )

        print("Add user succeeded!")
        return {
            "statusCode": 200,
        }

    except ClientError as e:
        return {
            "statusCode": 500,
            "body": json.dumps(str(e)),
        }