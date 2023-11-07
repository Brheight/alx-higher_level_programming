#!/usr/bin/python3
import sys
"""file"""
total_size = 0
status_codes = {200: 0, 301: 0, 400: 0, 401: 0, 403: 0, 404: 0, 405: 0, 500: 0}

def print_stats():
    """
    Prints statistics based on the global variables.
    """
    print("File size: {}".format(total_size))
    for key in sorted(status_codes.keys()):
        if status_codes[key] > 0:
            print("{}: {}".format(key, status_codes[key]))

try:
    for line in sys.stdin:
        try:
            parts = line.split()
            if len(parts) >= 2:
                size = int(parts[-1])
                status_code = int(parts[-2])
                if status_code in status_codes:
                    status_codes[status_code] += 1
                total_size += size
        except (ValueError, IndexError):
            pass

        if total_size % 10 == 0:
            print_stats()

except KeyboardInterrupt:
    print_stats()
    raise
