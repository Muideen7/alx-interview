#!/usr/bin/python3
import random
import sys
from time import sleep
import datetime

# Loop 15 times to generate 15 log entries
for i in range(15):
    # Introduce random delay between log entries (simulating real-time logs)
    sleep(random.random())

    # Generate a random IP address in the format "x.x.x.x"
    ip_address = "{:d}.{:d}.{:d}.{:d}".format(random.randint(1, 255), random.randint(1, 255), random.randint(1, 255), random.randint(1, 255))

    # Get the current timestamp in the format "YYYY-MM-DD HH:MM:SS.ssssss"
    timestamp = datetime.datetime.now()

    # Generate a random status code from the given options: 200, 301, 400, 401, 403, 404, 405, 500
    status_code = random.choice([200, 301, 400, 401, 403, 404, 405, 500])

    # Generate a random file size between 1 and 1024 bytes
    file_size = random.randint(1, 1024)

    # Print the log entry with the generated values
    sys.stdout.write("{} - [{}] \"GET /projects/260 HTTP/1.1\" {} {}\n".format(ip_address, timestamp, status_code, file_size))
    sys.stdout.flush()
