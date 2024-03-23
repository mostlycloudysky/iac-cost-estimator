import json
import boto3


def get_pricing_service_codes():
    pricing_client = boto3.client("pricing", region_name="us-east-1")
    service_codes = []
    response = pricing_client.get_paginator("list_services")
    for page in response.paginate():
        for service in page["Services"]:
            service_codes.append(service["ServiceCode"])
    return service_codes


# Lambda to fetch services codes from AWS pricing API and write them to S3 bucket
def lambda_handler(event, context):
    bucket_name = "iac-cost-estimator-pricing-list-mapping"
    file_name = "service_code_mapping.json"

    # Fetch Service codes using AWS pricing API
    service_codes = get_pricing_service_codes()
    print(service_codes)
    return {
        "statusCode": 200,
        "body": json.dumps("Successfully processed service code extractor"),
    }
