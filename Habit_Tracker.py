import json
import os
from datetime import date

FILE_NAME = "habits.json"

def load_habits():
    if os.path.exists(FILE_NAME):
        with open(FILE_NAME, "r") as file:
            return json.load(file)
    return {}

def save_habits(habits):
    with open(FILE_NAME, "w") as file:
        json.dump(habits, file, indent=4)

habits = load_habits()

while True:
    print("\n===== HABIT TRACKER =====")
    print("1. Add Habit")
    print("2. View Habits")
    print("3. Mark Habit Complete")
    print("4. Delete Habit")
    print("5. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        name = input("Enter habit name: ")
        habits[name] = habits.get(name, [])
        save_habits(habits)
        print("Habit added successfully!")

    elif choice == "2":
        if not habits:
            print("No habits found.")
        for name, records in habits.items():
            print(name, "- Completed:", len(records), "days")

    elif choice == "3":
        name = input("Enter habit name: ")
        if name in habits:
            today = str(date.today())
            if today not in habits[name]:
                habits[name].append(today)
                save_habits(habits)
                print("Habit marked complete!")
            else:
                print("Already completed today!")
        else:
            print("Habit not found.")

    elif choice == "4":
        name = input("Enter habit name: ")
        if name in habits:
            del habits[name]
            save_habits(habits)
            print("Habit deleted!")
        else:
            print("Habit not found.")

    elif choice == "5":
        print("Thank you!")
        break

    else:
        print("Invalid choice!")
