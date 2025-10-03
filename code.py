import json
import os
import matplotlib as plt 
from datetime import datetime, timedelta

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

#graphing previous 7 days
def plot_7_days():
    data = load_data
    today = datetime.today().date()
    last_7_days = [(today - timedelta(days=i)).isoformat() for i in range (6,-1,-1)]

    daily_totals = []
    for day in last_7_days:
        if day in data:
            daily_totals.append(sum(data[day].values()))
        else: 
            daily_totals.append(0)

    avg_hours = sum(daily_totals)/7
    peak_hours = max(daily_totals)

    plt.bar(last_7_days, daily_totals, color="skyblue")
    plt.xticks(rotation=45)
    plt.xlabel("Date")
    plt.ylabel("Hours Studied")
    plt.title(f"Study Hours (Last 7 Days)\n Average: {avg_hours:.2f} hrs | Peak: {peak_hours:.2f} hrs")
    plt.tight_layout()
    plt.show

#weekly prediction:
def predict():
    data = load_data()
    today = datetime.today().date()
    week_begin = today - timedelta(days=today.weekday())
    week_days = [(week_begin + timedelta(days=i)).isoformat() for i in range(7)]
    

def main():
    while True:
        print("\n1. Add study hours")
        print("2. View Stats")
        print("3. Show Graph")
        print("4. Exit")
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
        elif choice == "3":
            plot_7_days()
        elif choice =="4":
            print("Goodbye")
            return
        else:
            print("Invalid choice")
        
if __name__ == "__main__":
    main()
