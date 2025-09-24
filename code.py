import json
import os

filename = "Study_Tracker.json"

#loading data:
def load_data():
    if os.path.exists(filename):
        with open(filename, "r") as file:
            return json.load(file)
        return{}
    