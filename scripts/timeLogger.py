import argparse
import json
import os
from datetime import datetime, timedelta
import re  # Import for regex validation

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
    current_day_sec = 0
    if 'log_start' in log:
        start_time = datetime.fromisoformat(log['log_start'])
        current_day_sec += (datetime.now() - start_time).total_seconds()
    for date, seconds in log.items():
        if date == 'log_start':
            continue
        if date == datetime.now().date().isoformat():
            seconds += current_day_sec
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

def log_subtract(time_str):
    try:
        hours, minutes = map(int, time_str.split(':'))
        subtract_time = timedelta(hours=hours, minutes=minutes)
    except ValueError:
        print("Invalid time format. Use H:MM.")
        return

    log = load_log()
    current_date = datetime.now().date().isoformat()
    if current_date in log:
        log[current_date] -= subtract_time.total_seconds()
        if log[current_date] < 0:
            log[current_date] = 0  # Ensure no negative time
    else:
        print(f"No time logged for {current_date} to subtract from.")
        return

    save_log(log)
    print(f"Subtracted {hours:02}:{minutes:02} from {current_date}.")

def log_clear():
    log = load_log()
    if 'log_start' in log:
        log = {'log_start': log['log_start']}
    else:
        log = {}
    save_log(log)
    print("All entries cleared.")

def validate_time_format(value):
    """Validate that the time argument is in the format H:MM."""
    if not re.match(r"^\d+:\d{2}$", value):
        raise argparse.ArgumentTypeError(f"Invalid time format: '{value}'. Use H:MM.")
    return value

def main():
    parser = argparse.ArgumentParser(description="Time logging utility.")
    subparsers = parser.add_subparsers(dest="command", required=True)

    subparsers.add_parser("start", help="Start a logging session.")
    subparsers.add_parser("stop", help="Stop the current logging session.")
    subparsers.add_parser("status", help="Display the status of logged times.")

    add_parser = subparsers.add_parser("add", help="Add time to the current day.")
    add_parser.add_argument("time", type=validate_time_format, help="Time to add in H:MM format.")

    subtract_parser = subparsers.add_parser("subtract", help="Subtract time from the current day.")
    subtract_parser.add_argument("time", type=validate_time_format, help="Time to subtract in H:MM format.")

    subparsers.add_parser("clear", help="Clear all logged times except the current session.")

    args = parser.parse_args()

    if args.command == "start":
        log_start()
    elif args.command == "stop":
        log_stop()
    elif args.command == "status":
        log_status()
    elif args.command == "add":
        log_add(args.time)
    elif args.command == "subtract":
        log_subtract(args.time)
    elif args.command == "clear":
        log_clear()

if __name__ == "__main__":
    main()
