# Study Tracker

A simple command-line study tracker built with Python.

The application allows users to log study hours by subject, stores the data locally in JSON format, and provides summary statistics along with a visual representation of study activity over the previous seven days.

## Features

- Log study hours by subject
- Automatic daily tracking
- View cumulative study statistics
- 7-day bar chart of study hours
- Weekly study time prediction
- Local JSON data storage

## Tech Stack

- Python
- JSON
- Matplotlib
- datetime

## Project Structure

```
.
├── Study_Tracker.py
├── Study_Tracker.json
└── README.md
```

## Requirements

```bash
pip install matplotlib
```

## Run

```bash
python Study_Tracker.py
```

## Example

```
1. Add Study Hours
2. View Statistics
3. Show Last 7 Days Graph
4. Weekly Prediction
5. Exit
```

## Data Format

Study sessions are stored by date:

```json
{
    "2026-07-22": {
        "Math": 2,
        "Physics": 1.5
    }
}
```

## Notes

- Data is stored locally in `Study_Tracker.json`.
- If no data exists for a day, it is displayed as 0 hours in the graph.
- Weekly prediction is based on the average study time over the previous seven days.
