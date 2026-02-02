import csv

FRAUD_LOGIN_THRESHOLD = 3
RESTRICTED_DOWNLOAD_THRESHOLD = 1


def load_user_activity(filename):
    records = []

    with open(filename, newline="") as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            records.append({
                "user": row["user"],
                "failed_logins": int(row["failed_logins"]),
                "downloads": int(row["downloads"]),
                "restricted_downloads": int(row["restricted_downloads"]),
            })

    return records


def analyze_users(records):
    high_risk = []
    medium_risk = []

    for record in records:
        risk_score = 0
        reasons = []

        if record["failed_logins"] >= FRAUD_LOGIN_THRESHOLD:
            risk_score += 2
            reasons.append("Multiple failed login attempts")

        if record["restricted_downloads"] >= RESTRICTED_DOWNLOAD_THRESHOLD:
            risk_score += 3
            reasons.append("Downloaded restricted files")

        if risk_score >= 4:
            high_risk.append({
                "user": record["user"],
                "risk_score": risk_score,
                "reasons": reasons
            })
        elif risk_score >= 2:
            medium_risk.append({
                "user": record["user"],
                "risk_score": risk_score,
                "reasons": reasons
            })

    return high_risk, medium_risk


def print_report(high_risk, medium_risk):
    print("\nHigh-risk users:")
    if not high_risk:
        print("None detected")
    else:
        for user in high_risk:
            print(f"{user['user']} — Risk Score: {user['risk_score']}")
            for reason in user["reasons"]:
                print(f"  - {reason}")

    print("\nMedium-risk users:")
    if not medium_risk:
        print("None detected")
    else:
        for user in medium_risk:
            print(f"{user['user']} — Risk Score: {user['risk_score']}")
            for reason in user["reasons"]:
                print(f"  - {reason}")


if __name__ == "__main__":
    records = load_user_activity("user_activity.csv")
    high_risk, medium_risk = analyze_users(records)
    print_report(high_risk, medium_risk)
