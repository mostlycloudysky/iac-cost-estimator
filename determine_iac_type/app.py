import json


# Return cloudformation or terraform
def lambda_handler(event, context):
    # TODO implement
    iac_type = "cloudformation"
    return {"iacType": iac_type}
