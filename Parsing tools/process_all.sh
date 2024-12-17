#!/bin/bash

# Define the directory containing the MRT files
input_dir="Benign data MRT Format"

# Get the total number of files for progress tracking
total_files=$(ls "$input_dir"/updates.* 2>/dev/null | wc -l)
if [ "$total_files" -eq 0 ]; then
    echo "No files matching 'updates.*' were found in $input_dir."
    exit 1
fi

# Initialize a counter
counter=0

# Iterate over all files matching the pattern `updates.*` in the specified directory
for file in "$input_dir"/updates.*; do
    # Increment the counter
    counter=$((counter + 1))

    # Get the current timestamp
    timestamp=$(date +"%Y-%m-%d %H:%M:%S")

    # Print progress message
    echo "[$timestamp] Processing file $counter of $total_files: $file"

    # Run the Python script for each file
    python3 mrt2csv.py "$file"

    # Print completion message for the current file
    echo "[$timestamp] Completed file $counter of $total_files: $file"
    echo
done

# Final completion message
echo "All $total_files files processed."

