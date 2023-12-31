import json
import boto3
import os


def lambda_handler(event, context):
    stepfunction_client = boto3.client("stepfunctions")
    state_machine_arn = os.environ["STATE_MACHINE_ARN"]

    for record in event["Records"]:
        payload = json.loads(record["body"])
        response = stepfunction_client.start_execution(
            stateMachineArn=state_machine_arn, input=json.dumps(payload)
        )
    return {"statusCode": 200, "body": json.dumps(response)}
