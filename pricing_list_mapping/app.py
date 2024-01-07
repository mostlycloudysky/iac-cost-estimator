import json


# Sample lambda to show sucessful processing of terraform
def lambda_handler(event, context):
    # TODO implement
    return {
        "statusCode": 200,
        "body": json.dumps("Pricing List Mapping is running successfully"),
    }
