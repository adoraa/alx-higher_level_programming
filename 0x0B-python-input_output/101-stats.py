#!/usr/bin/python3
"""
Script that reads stdin line by line and computes metrics.
"""

import sys


def print_metrics(total_size, status_codes):
    """
    Prints the metrics since the beginning.

    Args:
        total_size (int): The total file size.
        status_codes (dict): Dictionary containing counts of status codes.
    """
    print("File size: {}".format(total_size))
    for code in sorted(status_codes):
        print("{}: {}".format(code, status_codes[code]))


def main():
    total_size = 0
    status_codes = {'200': 0, '301': 0, '400': 0, '404': 0, '500': 0}

    try:
        for i, line in enumerate(sys.stdin, 1):
            try:
                parts = line.split()
                size = int(parts[-1])
                code = parts[-2]
                total_size += size

                if code in status_codes:
                    status_codes[code] += 1

                if i % 10 == 0:
                    print_metrics(total_size, status_codes)

            except (ValueError, IndexError):
                pass

    except KeyboardInterrupt:
        print_metrics(total_size, status_codes)


if __name__ == "__main__":
    main()
