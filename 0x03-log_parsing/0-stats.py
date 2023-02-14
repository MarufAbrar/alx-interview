#!/usr/bin/env python

import sys

total_size = 0
count_by_status = {200: 0, 301: 0, 400: 0, 401: 0, 403: 0, 404: 0, 405: 0, 500: 0}
line_count = 0

for line in sys.stdin:
    # Parse the line
    line_count += 1
    line_parts = line.split()
    if len(line_parts) != 5:
        continue
    ip_address = line_parts[0]
    date = line_parts[1]
    status_code = int(line_parts[3])
    file_size = int(line_parts[4])

    # Update the total size
    total_size += file_size

    # Update the count by status
    if status_code in count_by_status:
        count_by_status[status_code] += 1

    # Print the stats after every 10 lines
    if line_count % 10 == 0:
        print('Total file size:', total_size)
        for status_code in sorted(count_by_status):
            print('{}: {}'.format(status_code, count_by_status[status_code]))