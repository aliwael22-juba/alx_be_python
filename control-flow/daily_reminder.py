task = input("Enter the task description: ")
priority = input("Enter the task priority (high, medium, low): ").lower()
time_bound = input("Is the task time-bound? (yes/no): ").lower()

reminder = f"Reminder: '{task}' is a {priority} priority task"
    
match priority:
        case "high":
            reminder += " that requires urgent attention."
        case "medium":
            reminder += " that should be addressed soon."
        case "low":
            reminder += " that can be handled later."
        case _:
            print("Invalid priority entered. Please use high, medium, or low.")
            exit()

if time_bound == "yes":
        reminder += " It requires immediate attention today!"
elif time_bound != "no":
        print("Please enter 'yes' or 'no' for time-bound status.")
        exit()

print(reminder)