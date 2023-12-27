import json
import hmac
import hashlib
import os


def validate_github_signature(event):
    github_secret = os.environ.get("GITHUB_WEBHOOK_SECRET")
    signature = event["headers"]["X-Hub-Signature-256"]
    if not signature or not github_secret:
        return False

    sha_name, signature = signature.split("=")
    if sha_name != "sha256":
        return False
    mac = hmac.new(
        github_secret.encode(), msg=event["body"].encode(), digestmod=hashlib.sha256
    )
    return hmac.compare_digest(mac.hexdigest(), signature)


# log the event and return the event in the response
def lambda_handler(event, context):
    # Validate github webhook signature
    if not validate_github_signature(event):
        return {"statusCode": 403, "body": "Invalid signature"}

    print(json.dumps(event, indent=4))

    if "body" in event and event["body"] is not None:
        try:
            body_obj = json.loads(event["body"])
            print("Pretty-printed body:", json.dumps(body_obj, indent=4))

        except json.JSONDecodeError:
            print("Error decoding JSON")

    return {"statusCode": 200, "body": "Successfully processed GitHub webhook data"}
