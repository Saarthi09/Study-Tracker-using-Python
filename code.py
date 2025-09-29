import json
import os

filename = "Study_Tracker.json"

#loading data:
def load_data():
    if os.path.exists(filename):
        with open(filename, "r") as file:
            return json.load(file)
    return{}

#saving data:
def save_data(data):
    with open(filename, "w") as file:
        json.dump(data, file, indent=4)

#adding study hours;
def add_hours(subject, hours):
    data = load_data()
    if subject in data:
        data[subject] += hours
    else: 
        data[subject] = hours
    save_data(data)
    print(f"Added {hours} hours to {subject}. Total = {data[subject]} hrs")

#viewing stats:
def view_stats():
    data = load_data()
    if not data:
        print("No hours logged yet")
        return
    total = 0
    for subject, hours in data.items():
        print(f"- {subject}: {hours} hrs")
        total += hours
    print(f"\n total study time: {total}hrs")

def main():
    while True:
        print("\n1. Add study hours")
        print("2. View Stats")
        print("3. Exit")
        choice = input("Choose: ")

        if choice == "1":
            subject = input("Enter subject name: ").strip()
            try:
                hours = float(input("Enter hours studied:"))
                add_hours(subject, hours)
            except ValueError:
                print("Please enter a valid number")
        elif choice == "2":
            view_stats()
        elif choice =="3":
            print("Goodbye")
        else:
            print("Invalid choice")
        
if __name__ == "__main__":
    main()
