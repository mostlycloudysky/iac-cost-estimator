import json


def lambda_handler(event, context):
    for record in event["Records"]:
        payload = json.loads(record["body"])
        print(payload)
    return {"statusCode": 200, "body": "Successfully Downloaded SQS data"}
