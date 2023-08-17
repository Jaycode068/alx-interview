import re
import sys

def compute_metrics(lines):
    total_size = 0
    status_count = {}

    for line in lines:
        match = re.match(r'(\S+) - \[([^\]]+)\] "GET /projects/260 HTTP/1.1" (\d+) (\d+)', line)
        if match:
            _, _, _, status_code, file_size = match.groups()
            total_size += int(file_size)
            status_count[status_code] = status_count.get(status_code, 0) + 1

    return total_size, status_count

def print_statistics(total_size, status_count):
    print("Total file size:", total_size)
    for status_code in sorted(status_count.keys()):
        if status_code in ['200', '301', '400', '401', '403', '404', '405', '500']:
            print(f"{status_code}: {status_count[status_code]}")

if __name__ == "__main__":
    lines = []
    try:
        for line in sys.stdin:
            lines.append(line.strip())
            if len(lines) == 10:
                total_size, status_count = compute_metrics(lines)
                print_statistics(total_size, status_count)
                lines = []
    except KeyboardInterrupt:
        total_size, status_count = compute_metrics(lines)
        print_statistics(total_size, status_count)
        sys.exit(0)

