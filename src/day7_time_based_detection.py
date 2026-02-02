# Parse Time-Ordered Events

from datetime import datetime

def parse_log(filename):
    events = []

    with open(filename, "r") as f:
        for line in f:
            parts = line.strip().split()
            event = {}

            for part in parts:
                if part.startswith("timestamp="):
                    event["time"] = datetime.fromisoformat(part.split("=")[1])
                elif part.startswith("user="):
                    event["user"] = part.split("=")[1]
                elif part.startswith("action="):
                    event["action"] = part.split("=")[1]
                elif part.startswith("status="):
                    event["status"] = part.split("=")[1]
                elif part.startswith("file="):
                    event["file"] = part.split("=")[1]

            if "time" in event and "user" in event:
                events.append(event)

    return sorted(events, key=lambda x: x["time"])

# Detect Suspicious Sequences
## Successful login followed by restricted download within 10 minutes

from datetime import timedelta

RESTRICTED_FILES = {"secrets.pdf", "payroll.db"}
TIME_WINDOW = timedelta(minutes=10)

def detect_time_based_threats(events):
    alerts = []
    last_login = {}

    for e in events:
        user = e["user"]

        if e.get("action") == "login" and e.get("status") == "success":
            last_login[user] = e["time"]

        if (
            e.get("action") == "download"
            and e.get("status") == "success"
            and e.get("file") in RESTRICTED_FILES
            and user in last_login
        ):
            if e["time"] - last_login[user] <= TIME_WINDOW:
                alerts.append({
                    "user": user,
                    "login_time": last_login[user],
                    "download_time": e["time"],
                    "file": e["file"],
                })

    return alerts

# Analyst-Readable Output

def print_alerts(alerts):
    print("\nTime-based insider threat alerts:")

    if not alerts:
        print("No suspicious sequences detected")
        return

    for a in alerts:
        print(
            f"ALERT: {a['user']} downloaded {a['file']} "
            f"{(a['download_time'] - a['login_time']).seconds // 60} minutes after login"
        )

# Main Execution Block

if __name__ == "__main__":
    events = parse_log("access.log")
    alerts = detect_time_based_threats(events)
    print_alerts(alerts)



