import json
import requests


def get_data_from_url(url):
    response = requests.get(url)
    if response.status_code == 200:
        return response.text
    else:
        raise Exception(f"Error downloading file from {url}")


def lambda_handler(event, context):
    if event.get("changes") and len(event["changes"]) > 0:
        for change in event["changes"]:
            raw_url = change["raw_url"]
            data = get_data_from_url(raw_url)
            print("Downloaded data from URL", data)

    return {
        "statusCode": 200,
        "body": json.dumps("Sucessfully processed cloudformation"),
    }
