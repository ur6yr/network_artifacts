#!/usr/bin/env python

import csv
import json
import os
import sys
from mrtparse import Reader

def main():
    if len(sys.argv) < 2:
        print("Usage: ./script.py <input_file>")
        sys.exit(1)

    input_file = sys.argv[1]
    output_file = os.path.splitext(input_file)[0] + ".csv"

    # Parse the MRT file to infer headers
    reader = Reader(input_file)
    first_entry = next(reader, None)

    if not first_entry:
        print("No data found in the MRT file.")
        sys.exit(1)

    # Infer headers from the first record's keys
    headers = list(first_entry.data.keys())

    # Open CSV file for writing
    with open(output_file, mode='w', newline='') as csv_file:
        writer = csv.writer(csv_file)

        # Write inferred headers
        writer.writerow(headers)

        # Write rows for all entries
        for entry in Reader(input_file):
            row = [entry.data.get(header, "") for header in headers]
            writer.writerow(row)

    print(f"Conversion complete. CSV file saved as {output_file}")

if __name__ == '__main__':
    main()

