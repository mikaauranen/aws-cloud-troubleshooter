def analyze_error(error_log):

    if "AccessDenied" in error_log:
        return {
            "type": "IAM-käyttöoikeusongelma",
            "cause": "Puuttuvat käyttöoikeudet",
            "recommendation": "Tarkista IAM-roolin oikeudet"
        }
        
        
    elif "Task timed out" in error_log or "Status: timeout" in error_log:
        return {
            "type": "AWS Lambda Timeout",
            "cause": "Funktion suoritus ylitti asetetun aikarajan",
            "recommendation": "Tarkista CloudWatch-lokit ja Lambdan timeout-asetus"
        }

    else:
        return {
            "type": "Tuntematon virhe",
            "cause": "Virheilmoitus ei vastaa ohjelman tunnistamia virhetyyppejä",
            "recommendation": "Tarkista virheilmoituksen tarkka sisältö ja AWS CloudWatch -lokit"
        }
        
    
def analyze_error_with_ai(error_log):
    result = analyze_error(error_log)

    if result["type"] == "Tuntematon virhe":
        from bedrock_client import analyze_with_ai
        result["recommendation"] = analyze_with_ai(error_log)

    return result

        
if __name__ == "__main__":
        
    print("AWS Troubleshooter")

    error_log = input("Syötä virheilmoitus: ")

    print("\nAnalysoitava virhe:")
    print(error_log)

    print(analyze_error_with_ai(error_log))

