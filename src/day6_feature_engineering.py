# Reused CSV Loader Code

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

# Feature Engineering Function
# Converts behaviors into numerical indicators and creates binary flags for ML.

def generate_features(records):
    feature_rows = []

    for record in records:
        login_flag = 1 if record["failed_logins"] >= FRAUD_LOGIN_THRESHOLD else 0
        restricted_flag = 1 if record["restricted_downloads"] >= RESTRICTED_DOWNLOAD_THRESHOLD else 0

        total_risk_score = (
            login_flag * 2 +
            restricted_flag * 3
        )

        feature_rows.append({
            "user": record["user"],
            "failed_login_count": record["failed_logins"],
            "restricted_download_count": record["restricted_downloads"],
            "login_risk_flag": login_flag,
            "restricted_access_flag": restricted_flag,
            "total_risk_score": total_risk_score
        })

    return feature_rows

# Print Feature Table

def print_features(feature_rows):
    print("\nGenerated ML Features:\n")

    for row in feature_rows:
        print(
            f"{row['user']} | "
            f"failed_logins={row['failed_login_count']} | "
            f"restricted_downloads={row['restricted_download_count']} | "
            f"login_flag={row['login_risk_flag']} | "
            f"restricted_flag={row['restricted_access_flag']} | "
            f"risk_score={row['total_risk_score']}"
        )

# Main Execution Block

if __name__ == "__main__":
    records = load_user_activity("user_activity.csv")
    features = generate_features(records)
    print_features(features)

