import json

from troubleshooter import analyze_error

def lambda_handler(event, context):
    
    return {
        'statusCode': 200,
        'body': json.dumps(analyze_error(event.get("error_log", "")))
    }
