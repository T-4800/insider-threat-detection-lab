failed_logins = {}
restricted_files = {"secrets.pdf", "payroll.db"}

successful_logins = set()
policy_violations = set()

with open("data/access.log", "r") as log_file:
    for line in log_file:
        line = line.strip()

        if "user=" not in line or "status=" not in line:
            print(f"Skipping malformed line: {line}")
            continue

        parts = line.split()
        user = None
        status = None
        action = None
        file = None

        for part in parts:
            if part.startswith("user="):
                user = part.split("=")[1]
            elif part.startswith("status="):
                status = part.split("=")[1]
            elif part.startswith("action="):
                action = part.split("=")[1]
            elif part.startswith("file="):
                file = part.split("=")[1]

        # Failed login tracking
        if user and status == "fail":
            failed_logins[user] = failed_logins.get(user, 0) + 1

        # Successful login tracking
        if user and action == "login" and status == "success":
            successful_logins.add(user)

        # Restricted file download detection
        if (
            user
            and action == "download"
            and status == "success"
            and file in restricted_files
            and user in successful_logins
        ):
            policy_violations.add(user)

print("\nFailed login summary:")
for user, count in failed_logins.items():
    print(f"{user}: {count}")

print("\nRestricted file policy violations:")
if not policy_violations:
    print("None detected")
else:
    for user in policy_violations:
        print(f"ALERT: {user} downloaded a restricted file after successful login")

  
