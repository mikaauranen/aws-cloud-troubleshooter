import json

from troubleshooter import analyze_error_with_ai

def lambda_handler(event, context):
    
    print("AWS Cloud Troubleshooter: Analyysi aloitettu")
        
    return {
        'statusCode': 200,
        'body': json.dumps(analyze_error_with_ai(event.get("error_log", "")))
    }
