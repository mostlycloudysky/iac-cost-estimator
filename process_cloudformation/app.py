import json
import requests
import boto3

bedrock = boto3.client(service_name="bedrock-runtime")


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
            print(data)

            body = json.dumps(
                {
                    "prompt": "Output list of JSON array format for the AWS resources types in the format AWS::Serverless::Function, AWS::IAM::Role etc. and list should include all the resource type defined in the template:\n"
                    + data,
                    "max_tokens": 400,
                    "temperature": 0.75,
                    "p": 0.01,
                    "k": 0,
                }
            )
            print("body: ", body)

            model_id = "cohere.command-text-v14"
            accept = "application/json"
            content_type = "application/json"

            response = bedrock.invoke_model(
                body=body, modelId=model_id, accept=accept, contentType=content_type
            )

            response_body = json.loads(response.get("body").read())
            print("response_body: ", response_body)
            text_object = response_body["generations"][0]["text"]
            formatted_text = (
                text_object.replace("```json", "").replace("```", "").strip()
            )
            response_json = json.loads(formatted_text)

    return {
        "statusCode": 200,
        "body": response_json,
    }
