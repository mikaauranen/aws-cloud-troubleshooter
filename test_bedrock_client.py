import unittest
from botocore.exceptions import ClientError
from unittest.mock import patch
from troubleshooter import analyze_error_with_ai
from bedrock_client import build_prompt

class TestBedrockClient(unittest.TestCase):
    def test_prompt_contains_error(self):
        prompt = build_prompt("Connection refused")
        self.assertIn("Connection refused", prompt)
    
    def test_unknown_error_uses_ai(self):
        with patch("bedrock_client.analyze_with_ai", return_value="AI:n testivastaus") as mock_ai:
            result = analyze_error_with_ai("Connection refused")

        self.assertEqual(result["recommendation"], "AI:n testivastaus")
        mock_ai.assert_called_once_with("Connection refused")
        
    def test_known_error_does_not_use_ai(self):
        with patch("bedrock_client.analyze_with_ai") as mock_ai:
            result = analyze_error_with_ai("AccessDenied")

        self.assertEqual(result["type"], "IAM-käyttöoikeusongelma")
        mock_ai.assert_not_called()
    
    def test_ai_failure_returns_fallback(self):
        error = ClientError(
            {"Error": {"Code": "AccessDeniedException", "Message": "Test error"}},
            "Converse"
        )

        with patch("bedrock_client.analyze_with_ai", side_effect=error):
            result = analyze_error_with_ai("Connection refused")

        self.assertEqual(
            result["recommendation"],
            "Tekoälyanalyysi ei ole saatavilla. Tarkista CloudWatch-lokit."
        )



