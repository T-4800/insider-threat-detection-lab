# --- Policy Configuration ---
RESTRICTED_FILES = {"secrets.pdf", "payroll.db"}


# --- Parsing Functions ---
def parse_log_line(line):
    """
    Parse a single log line into structured fields.
    Returns a dict or None if malformed.
    """
    if "user=" not in line or "status=" not in line:
        return None

    fields = {
        "user": None,
        "action": None,
        "status": None,
        "file": None,
    }

    for part in line.split():
        if "=" in part:
            key, value = part.split("=", 1)
            if key in fields:
                fields[key] = value

    return fields


# --- Detection Logic ---
def process_logs(filename):
    failed_logins = {}
    successful_logins = set()
    policy_violations = set()

    with open(filename, "r") as log_file:
        for raw_line in log_file:
            line = raw_line.strip()

            parsed = parse_log_line(line)
            if not parsed:
                print(f"Skipping malformed line: {line}")
                continue

            user = parsed["user"]
            action = parsed["action"]
            status = parsed["status"]
            file = parsed["file"]

            # Failed login detection
            if user and action == "login" and status == "fail":
                failed_logins[user] = failed_logins.get(user, 0) + 1

            # Successful login tracking
            if user and action == "login" and status == "success":
                successful_logins.add(user)

            # Restricted file download detection
            if (
                user
                and action == "download"
                and status == "success"
                and file in RESTRICTED_FILES
                and user in successful_logins
            ):
                policy_violations.add(user)

    return failed_logins, policy_violations


# --- Output / Reporting ---
def print_report(failed_logins, policy_violations):
    print("\nFailed login summary:")
    if not failed_logins:
        print("None detected")
    else:
        for user, count in failed_logins.items():
            print(f"{user}: {count}")

    print("\nRestricted file policy violations:")
    if not policy_violations:
        print("None detected")
    else:
        for user in policy_violations:
            print(
                f"ALERT: {user} downloaded a restricted file after successful login"
            )


# --- Main Execution ---
if __name__ == "__main__":
    failed, violations = process_logs("access.log")
    print_report(failed, violations)
