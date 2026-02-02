# Variables
case_id = 10234
suspect_name = "John Doe"
risk_score = 7.5
active_case = True
analyst = 441

print("Case ID:", case_id)
print("Suspect:", suspect_name)
print("Risk Score:", risk_score)
print("Active Case:", active_case)

analyst = input("Enter Your Badge Number: ")
print("Welcome Detective Sheppard.")

if analyst < 441:
    print("Unauthorized User") 
elif analyst > 441:
    print("Unauthorized User")          


if risk_score >= 8:
    print("High risk — escalate case.")
elif risk_score >= 5:
    print("Medium risk — monitor closely.")
else:
    print("Low risk — routine review.")

risk_score = risk_score + 1
print("Updated Risk Score:", risk_score)

if not active_case:
    print("Case is closed.")
else:
    print("Case remains open.")

