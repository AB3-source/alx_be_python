# daily_reminder.py

# Prompt for user input
task = input("Enter your task: ")
priority = input("Priority (high/medium/low): ").lower()
time_bound = input("Is it time-bound? (yes/no): ").lower()

# Use match-case to handle different priority levels
match priority:
    case "high":
        message = f"Reminder: '{task}' is a high priority task"
    case "medium":
        message = f"Reminder: '{task}' is a medium priority task"
    case "low":
        message = f"Note: '{task}' is a low priority task"
    case _:
        message = f"'{task}' has an unknown priority level"

# Append time sensitivity message
if time_bound == "yes" and "unknown" not in message:
    message += " that requires immediate attention today!"
elif time_bound == "no" and "unknown" not in message:
    message += ". Consider completing it when you have free time."

# Print final message
print("\n" + message)
