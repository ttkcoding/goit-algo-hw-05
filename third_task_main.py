import sys
#create a dict with keys-values
def parse_log_line(line: str) -> dict:
    parts = line.split()
    return {
        'Date': parts[0],
        'Time': parts[1],
        'Level': parts[2],
        'Message': ' '.join(parts[3:])
    }
#open log file, use func(parse_log_line) for creating list with dict
def load_logs(file_path: str) -> list:
    logs = []
    with open(file_path, 'r') as file:
        for line in file:
            logs.append(parse_log_line(line))
    return logs
#use list comprehension for filter and print all files by arguments
def filter_logs_by_level(logs: list, level: str) -> list:
    return [log for log in logs if log['Level'].upper() == level.upper()]

#use this function for count all same values in the same keys
def count_logs_by_level(logs: list) -> dict:
    counts = {}
    for log in logs:
        level = log['Level']
        counts[level] = counts.get(level, 0) + 1
    return counts
#use this function for print all resault in (count_logs_by_level) function
def display_log_counts(counts: dict):
    print("Рівень логування | Кількість")
    print("-----------------|----------")
    for level, count in counts.items():
        print(f"{level:<16} | {count}")
#use this for display all log if user input log key
def display_log_details(logs: list):
    for log in logs:
        print(f"{log['Date']} {log['Time']} - {log['Message']}")
#main function where i use all function for give result for user arguments
def main():
    if len(sys.argv) < 2:
        print("Використання: python3 third_task_main.py path/to/example.log [level]")
        sys.exit(1)
    #argument number 1 is a file path
    file_path = sys.argv[1]
    try:
        logs = load_logs(file_path)
        counts = count_logs_by_level(logs)

        display_log_counts(counts)
    except FileNotFoundError:
        print('File didn`t find')
    #if user gives 3 argument, use (filter_logs) and (display_log) for print information for Level in logs
    if len(sys.argv) == 3:
        level = sys.argv[2]
        filtered_logs = filter_logs_by_level(logs, level)
        print(f"\nДеталі логів для рівня '{level.upper()}':")
        display_log_details(filtered_logs)

if __name__ == "__main__":
    main()