import json


# Sample lambda to show sucessful processing of cloudformation
def lambda_handler(event, context):
    # TODO implement
    return {
        "statusCode": 200,
        "body": json.dumps("Sucessfully processed cloudformation"),
    }
