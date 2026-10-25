import json
import unittest
from botocore.exceptions import ClientError
from unittest.mock import patch
from lambda_function import lambda_handler

class TestLambdaFunction(unittest.TestCase):
    def test_unknown_error_uses_ai(self):
        with patch("bedrock_client.analyze_with_ai", return_value="AI:n testivastaus") as mock_ai:
            response = lambda_handler({"error_log": "Connection refused"}, None)

        body = json.loads(response["body"])

        self.assertEqual(response["statusCode"], 200)
        self.assertEqual(body["recommendation"], "AI:n testivastaus")
        mock_ai.assert_called_once_with("Connection refused")
        
    def test_lambda_handles_ai_failure(self):
        error = ClientError(
            {"Error": {"Code": "AccessDeniedException", "Message": "Test error"}},
            "Converse"
        )

        with patch("bedrock_client.analyze_with_ai", side_effect=error):
            response = lambda_handler({"error_log": "Connection refused"}, None)

        body = json.loads(response["body"])

        self.assertEqual(
            body["recommendation"],
            "Tekoälyanalyysi ei ole saatavilla. Tarkista CloudWatch-lokit."
        )

