import unittest
from bedrock_client import build_prompt

class TestBedrockClient(unittest.TestCase):
    def test_prompt_contains_error(self):
        prompt = build_prompt("Connection refused")
        self.assertIn("Connection refused", prompt)
