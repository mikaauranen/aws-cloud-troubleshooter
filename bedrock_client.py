import boto3

MODEL_ID = "amazon.nova-lite-v1:0"

def get_bedrock_client():
    return boto3.client("bedrock-runtime", region_name="eu-north-1")

def build_prompt(error_log):
    return (
        "Analyze this AWS error. "
        "Explain the likely cause and suggest one solution in 3 short sentences.\n\n"
        f"Error: {error_log}"
    )

def build_messages(error_log):
    prompt = build_prompt(error_log)

    return [
        {
            "role": "user",
            "content": [{"text": prompt}]
        }
    ]

def analyze_with_ai(error_log):
    client = get_bedrock_client()
    messages = build_messages(error_log)

    response = client.converse(
        modelId=MODEL_ID,
        messages=messages,
        inferenceConfig={
            "maxTokens": 200,
            "temperature": 0.2
        }
    )

    return response["output"]["message"]["content"][0]["text"]
