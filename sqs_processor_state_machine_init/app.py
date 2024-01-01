import json
import boto3
import os


def lambda_handler(event, context):
    stepfunction_client = boto3.client("stepfunctions")
    sqs_client = boto3.client("sqs")
    state_machine_arn = os.environ["STATE_MACHINE_ARN"]
    queue_url = os.environ["SQS_QUEUE_URL"]

    for record in event["Records"]:
        try:
            payload = json.loads(record["body"])
            response = stepfunction_client.start_execution(
                stateMachineArn=state_machine_arn, input=json.dumps(payload)
            )
            # Delete the message from SQS queue
            sqs_client.delete_message(
                QueueUrl=queue_url, ReceiptHandle=record["receiptHandle"]
            )
        except Exception as e:
            print(f"Error processing message: {e}")

    return {"statusCode": 200, "body": "Processed messages"}
