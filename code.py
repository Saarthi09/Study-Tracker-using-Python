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
    with open(FILENAME, "w") as file:
        json.dump(data, file, indent=4)

#adding study hours;
def add_hours(subjects, hours):
    data = load_data
    if subject in data:
        data[subject] += hours
    else: 
        data[subject] = hours
    save_data(data)
    print(f"Added {hours} hours to {subjects}. Total = {data[subject]} hrs")

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
    print{f"\n total study time: {total}hrs"}
