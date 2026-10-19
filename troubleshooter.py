print("AWS Troubleshooter")

error_log = input("Syötä virheilmoitus: ")

print("\nAnalysoitava virhe:")
print(error_log)

if "AccessDenied" in error_log:
    print("\nVirheen tyyppi: IAM-käyttöoikeusongelma")
    print("Mahdollinen syy: Puuttuvat käyttöoikeudet")
    print("Suositus: Tarkista IAM-roolin oikeudet")
    
elif "Task timed out" in error_log or "Status: timeout" in error_log:
    print("Virheen tyyppi: AWS Lambda Timeout")
    print("Mahdollinen syy: Funktion suoritus ylitti asetetun aikarajan")
    print("Suositus: Tarkista CloudWatch-lokit ja Lambdan timeout-asetus")

else:
    print("\nVirhettä ei tunnistettu")
