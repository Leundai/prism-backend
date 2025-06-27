import json
from pydantic import ValidationError
from models import Tweet
from typing import Any


def lambda_handler(event, context):
    """Sample pure Lambda function

    Parameters
    ----------
    event: dict, required
        API Gateway Lambda Proxy Input Format

        Event doc: https://docs.aws.amazon.com/apigateway/latest/developerguide/set-up-lambda-proxy-integrations.html#api-gateway-simple-proxy-for-lambda-input-format

    context: object, required
        Lambda Context runtime methods and attributes

        Context doc: https://docs.aws.amazon.com/lambda/latest/dg/python-context-object.html

    Returns
    ------
    API Gateway Lambda Proxy Output Format: dict

        Return doc: https://docs.aws.amazon.com/apigateway/latest/developerguide/set-up-lambda-proxy-integrations.html
    """
    try:
        http_method = event.get("httpMethod", "")
        path = event.get("path", "")

        if http_method == "POST" and path == "/tweets/report":
            return handle_tweets_report(event)
        elif http_method == "GET" and path == "/hello":
            return handle_hello()
        else:
            return {
                "statusCode": 404,
                "body": json.dumps({"error": "Not found"}),
            }
    except Exception as e:
        return {
            "statusCode": 500,
            "body": json.dumps({"error": f"Internal server error {e}"}),
        }


def validate_tweets(raw_tweets: list[dict[str, Any]]) -> list[Tweet]:
    validated_tweets = []
    for tweet_data in raw_tweets:
        try:
            validated_tweet = Tweet(**tweet_data)
            validated_tweets.append(validated_tweet)
        except ValidationError as validation_error:
            return {
                "statusCode": 400,
                "body": json.dumps(
                    {
                        "error": "Invalid tweet data",
                        "validation_errors": validation_error.errors(),
                    }
                ),
            }
    return validated_tweets


def handle_tweets_report(event):
    try:
        body = json.loads(event.get("body", r"{}"))
    except json.JSONDecodeError:
        return {
            "statusCode": 400,
            "body": json.dumps({"error": "Invalid JSON in request body"}),
        }

    if not isinstance(body, dict):
        return {
            "statusCode": 400,
            "body": json.dumps({"error": "Request body must be an object"}),
        }
    elif "tweets" not in body:
        return {
            "statusCode": 400,
            "body": json.dumps({"error": "'tweets' field is missing from body"}),
        }

    try:
        tweets = validate_tweets(body["tweets"])
    except KeyError as e:
        return {
            "statusCode": 400,
            "body": json.dumps({"error": f"Missing required field: {e}"}),
        }

    tweets_count = len(tweets)
    return {
        "statusCode": 200,
        "body": json.dumps({"tweets_received": tweets_count}),
    }


def handle_hello():
    # try:
    #     ip = requests.get("http://checkip.amazonaws.com/")
    # except requests.RequestException as e:
    #     # Send some context about this error to Lambda Logs
    #     print(e)

    #     raise e

    return {
        "statusCode": 200,
        "body": json.dumps(
            {
                "message": "hello world",
                # "location": ip.text.replace("\n", "")
            }
        ),
    }
