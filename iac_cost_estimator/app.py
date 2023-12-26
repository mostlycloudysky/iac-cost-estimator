import json


# log the event and return the event in the response
def lambda_handler(event, context):
    print(json.dumps(event, indent=4))

    if "body" in event and event["body"] is not None:
        try:
            body_obj = json.loads(event["body"])
            print("Pretty-printed body:", json.dumps(body_obj, indent=4))

        except json.JSONDecodeError:
            print("Error decoding JSON")

    return {"statusCode": 200, "body": json.dumps(event)}
