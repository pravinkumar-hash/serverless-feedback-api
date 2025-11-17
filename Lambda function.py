import json

def lambda_handler(event, context):
    try:
        body = json.loads(event.get("body", "{}"))
    except json.JSONDecodeError:
        return {
            "statusCode": 400,
            "body": json.dumps({"error": "Invalid JSON in request body"})
        }

    name = body.get("name")
    email = body.get("email")
    role = body.get("role")
    message = body.get("message")

    if not name or not email or not message:
        return {
            "statusCode": 400,
            "body": json.dumps({"error": "name, email, and message are required"})
        }

    print("=== New Feedback Received ===")
    print(f"Name   : {name}")
    print(f"Email  : {email}")
    print(f"Role   : {role}")
    print(f"Message: {message}")

    return {
        "statusCode": 200,
        "body": json.dumps({
            "status": "ok",
            "message": "Feedback received. Thank you!"
        })
    }
