import sys
import json
import os
from datetime import datetime, timedelta

LOG_FILE = os.path.expanduser("~/.timeLog.json")

def load_log():
    if os.path.exists(LOG_FILE):
        with open(LOG_FILE, 'r') as file:
            return json.load(file)
    return {}

def save_log(log):
    with open(LOG_FILE, 'w') as file:
        json.dump(log, file, indent=4)

def log_start():
    log = load_log()
    if 'log_start' in log:
        print("Warning: A start time is already logged.")
        return
    log['log_start'] = datetime.now().isoformat()
    save_log(log)
    print("Start time logged.")

def log_stop():
    log = load_log()
    if 'log_start' not in log:
        print("No start time logged.")
        return

    start_time = datetime.fromisoformat(log['log_start'])
    end_time = datetime.now()
    duration = end_time - start_time

    current_date = datetime.now().date().isoformat()
    if current_date in log:
        log[current_date] += duration.total_seconds()
    else:
        log[current_date] = duration.total_seconds()

    del log['log_start']
    save_log(log)
    print("Stop time logged and duration added.")

def round_to_nearest_15_minutes(duration):
    total_minutes = duration.total_seconds() / 60
    rounded_minutes = round(total_minutes / 15) * 15
    return timedelta(minutes=rounded_minutes)

def log_status():
    log = load_log()
    print(f"{'Date':<10} {'Duration':<8} {'Adjusted':<8}")
    print("-" * 30)
    for date, seconds in log.items():
        if date == 'log_start':
            continue
        total_duration = timedelta(seconds=seconds)
        adjusted_duration = round_to_nearest_15_minutes(total_duration * 4 / 3)
        hours, remainder = divmod(total_duration.seconds, 3600)
        minutes, _ = divmod(remainder, 60)
        adj_hours, adj_remainder = divmod(adjusted_duration.seconds, 3600)
        adj_minutes, _ = divmod(adj_remainder, 60)
        print(f"{date:<10} {hours:02}:{minutes:02} {adj_hours:02}:{adj_minutes:02}")

def log_add(time_str):
    try:
        hours, minutes = map(int, time_str.split(':'))
        additional_time = timedelta(hours=hours, minutes=minutes)
    except ValueError:
        print("Invalid time format. Use H:MM.")
        return

    log = load_log()
    current_date = datetime.now().date().isoformat()
    if current_date in log:
        log[current_date] += additional_time.total_seconds()
    else:
        log[current_date] = additional_time.total_seconds()

    save_log(log)
    print(f"Added {hours:02}:{minutes:02} to {current_date}.")

def log_clear():
    log = load_log()
    if 'log_start' in log:
        log = {'log_start': log['log_start']}
    else:
        log = {}
    save_log(log)
    print("All entries cleared.")

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: log [start|stop|status|add|clear] [time]")
        sys.exit(1)

    command = sys.argv[1].lower()
    if command == "start":
        log_start()
    elif command == "stop":
        log_stop()
    elif command == "status":
        log_status()
    elif command == "add":
        if len(sys.argv) != 3:
            print("Usage: log add H:MM")
            sys.exit(1)
        log_add(sys.argv[2])
    elif command == "clear":
        log_clear()
    else:
        print("Unknown command. Use 'start', 'stop', 'status', 'add', or 'clear'.")
