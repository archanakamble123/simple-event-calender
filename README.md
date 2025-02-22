# Event Calendar

This Python program loads and displays events from a CSV file, allowing users to filter events by date and search for specific keywords.

## Features
- Load events from a CSV file (`events.csv`).
- Format event dates for better readability.
- Display all events.
- Retrieve events for a specific date.
- Search events by title or description.

## Requirements
- Python 3.x
- Pandas

## Installation
1. Clone this repository:
   ```sh
   git clone https://github.com/yourusername/event-calendar.git
   cd event-calendar
   ```
2. Install dependencies:
   ```sh
   pip install pandas
   ```

## Usage
Run the script using:
```sh
python event_calendar.py
```

### Interactions
- The script will display all events.
- It will then check for events scheduled for tomorrow and display them.
- You can input a keyword to search for matching events.

## CSV File Format (`events.csv`)
Ensure your CSV file follows this format:
```csv
date,title,description
2025-02-23,Meeting,Project discussion with team
2025-02-24,Workshop,AI and ML training session
```



## Contributions
Feel free to submit issues or pull requests to improve the project!

