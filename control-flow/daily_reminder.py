task = input("Enter your task: ").strip()
priority = input("Priority (high/medium/low): ").strip()
time_bound = input("Is it time-bound? (yes/no): ").strip()

match priority:
    case "high":
        if time_bound == "yes":
            print(f"Reminder: '{task}' is a high priority task that requires immediate attention today!")
        elif time_bound == "no":
            print(f"Reminder: '{task}' is a high priority task. Consider completing it when you have free time.")
        else:
            print("please enter either (yes/no)!")
    case "low":
        if time_bound == "yes":
            print(f"Note: '{task}' is a low priority task that requires immediate attention today!")
        elif time_bound == "no":
            print(f"Note: '{task}' is a low priority task. Consider completing it when you have free time.")
        else:
            print("please enter either (yes/no)!")
