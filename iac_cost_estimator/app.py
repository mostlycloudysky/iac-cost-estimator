import json

# log the event and return the event in the response
def lambda_handler(event, context):
    print(json.dumps(event))
    return {"statusCode": 200, "body": json.dumps(event)}
