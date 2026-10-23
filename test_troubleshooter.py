import unittest
from troubleshooter import analyze_error

class TestTroubleshooter(unittest.TestCase):
    def test_access_denied(self):
        result = analyze_error("AccessDenied")
        
        self.assertEqual(result["type"], "IAM-käyttöoikeusongelma")
        
    def test_lambda_timeout(self):
        
        result = analyze_error("Task timed out after 3.00 seconds")
                
        self.assertEqual(result["type"], "AWS Lambda Timeout")
        
    def test_unknown_error(self):
        
        result = analyze_error("ConnectionError: Connection refused")
        
        self.assertEqual(result["type"], "Tuntematon virhe")
        
