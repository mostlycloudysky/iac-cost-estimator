import json


# Return cloudformation or terraform
def lambda_handler(event, context):
    # TODO implement
    default_iac_type = "unknown"

    if event.get("changes") and len(event["changes"]) > 0:
        first_change = event["changes"][0]
        iac_type = first_change.get("file_type", default_iac_type)
    else:
        iac_type = default_iac_type

    event["iacType"] = iac_type
    return event
