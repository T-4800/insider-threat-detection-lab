# Same User Activity Data Code From Days 5-6

import csv

def load_user_activity(filename):
    records = []
    with open(filename, newline="") as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            records.append({
                "user": row["user"],
                "failed_logins": int(row["failed_logins"]),
                "restricted_downloads": int(row["restricted_downloads"]),
            })
    return records

# This Section of Code Computes Baseline Behavior (What is normal)

def compute_baseline(records):
    total_failed = 0
    total_restricted = 0

    for r in records:
        total_failed += r["failed_logins"]
        total_restricted += r["restricted_downloads"]

    count = len(records)

    return {
        "avg_failed_logins": total_failed / count,
        "avg_restricted_downloads": total_restricted / count,
    }

# This Section of Code Calculates Anomaly Distance (How far a user is from average behavior)

def detect_anomalies(records, baseline):
    anomalies = []

    for r in records:
        login_anomaly = abs(
            r["failed_logins"] - baseline["avg_failed_logins"]
        )
        
        data_anomaly = abs(
            r["restricted_downloads"] - baseline["avg_restricted_downloads"]
        )
        
        anomalies.append({
            "user": r["user"],
            "login_anomaly": round(login_anomaly, 2),
            "data_anomaly": round(data_anomaly, 2),
            "failed_logins": r["failed_logins"],
            "restricted_downloads": r["restricted_downloads"],
        })

    return anomalies

# This Section of Code Ranks Users By Their Unusualness

def print_anomaly_report(anomalies):
    print("\nDirectional anomaly analysis):")
    
    for u in anomalies:
        print(
            f"{u['user']} | "
            f"login_anomaly={u['login_anomaly']} | "
            f"data_anomaly={u['data_anomaly']} | "
            f"failed_logins={u['failed_logins']} | "
            f"restricted_downloads={u['restricted_downloads']}"
        )

# Main Exxecution Block That Puts It All Together

if __name__ == "__main__":
    records = load_user_activity("user_activity.csv")
    baseline = compute_baseline(records)
    anomalies = detect_anomalies(records, baseline)
    print_anomaly_report(anomalies)
