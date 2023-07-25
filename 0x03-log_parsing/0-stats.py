#!/usr/bin/env python3

import sys

def compute_metrics():
    total_size = 0
    status_codes = {}

    try:
        line_count = 0
        for line in sys.stdin:
            line_count += 1

            # Parse the line using regex
            match = re.match(r'^(\S+) - \[.*\] "GET /projects/260 HTTP/1.1" (\d+) (\d+)$', line.strip())
            if not match:
                continue

            ip_address, status_code, file_size = match.groups()

            # Update total file size
            total_size += int(file_size)

            # Update status code count
            if status_code in status_codes:
                status_codes[status_code] += 1
            else:
                status_codes[status_code] = 1

            # Print metrics after every 10 lines
            if line_count % 10 == 0:
                print_metrics(total_size, status_codes)

    except KeyboardInterrupt:
        # Print final metrics if keyboard interruption occurs
        print_metrics(total_size, status_codes)

def print_metrics(total_size, status_codes):
    print(f"Total file size: File size: {total_size}")
    for status_code in sorted(status_codes.keys()):
        print(f"{status_code}: {status_codes[status_code]}")

if __name__ == "__main__":
    compute_metrics()
