users = ["alice", "bob", "charlie", "david"]

print("User list:")
for user in users:
    print("-", user)

user_activity = {
    "alice": 2,
    "bob": 9,
    "charlie": 5,
    "david": 1
}

print("\nUser activity levels:")
for user, activity in user_activity.items():
    print(user, "=>", activity)

print("\nRisk assessment:")
for user, activity in user_activity.items():
    if activity >= 8:
        print(user, "HIGH RISK")
    elif activity >= 4:
        print(user, "MEDIUM RISK")
    else:
        print(user, "LOW RISK")

high_risk_users = []

for user, activity in user_activity.items():
    if activity >= 8:
        high_risk_users.append(user)

print("\nUsers flagged for review:", high_risk_users)

total_activity = 0

for activity in user_activity.values():
    total_activity += activity

average_activity = total_activity / len(user_activity)
print("\nAverage activity level:", average_activity)

