#!/usr/bin/python3
import sys

# Initialize variables to store total file size and line count
total_size = 0
count = 0

# Dictionary to store counts of different status codes
# The keys are the status codes, and the values are the counts initialized to 0
codes = {'200': 0, '301': 0, '400': 0, '401': 0, '403': 0, '404': 0, '405': 0, '500': 0}

# Function to print the total file size and counts of each status code
def print_stats():
    print("File size: {}".format(total_size))
    for key, val in codes.items():
        if val:
            print("{}: {}".format(key, val))

try:
    # Read lines from the standard input (stdin)
    for line in sys.stdin:
        # Split the line into values based on spaces
        values = line.split(" ")

        # Check if the line has more than 2 elements (assuming input format)
        if len(values) > 2:
            # Extract the status code and file size from the line
            code = values[-2]
            size = int(values[-1])

            # Check if the status code is one of the specified ones
            if code in codes:
                # Increment the count for the status code and add the size to total_size
                codes[code] += 1
                total_size += size

            # Increment the line count
            count += 1

            # Check if 10 lines have been processed
            if count == 10:
                # Print the current statistics
                print_stats()

                # Reset the line count for the next 10 lines
                count = 0

# Handle keyboard interruption (CTRL + C)
except KeyboardInterrupt:
    # Print the current statistics before exiting
    print_stats()

finally:
    # Print the final statistics after all lines have been processed
    print_stats()
