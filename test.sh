#!/bin/bash
 
# Directory containing the files to be processed
FILES_DIR="./files"
 
# Iterate over each file in the directory
for file in "$FILES_DIR"/*; do
  # Check if it's a regular file
  if [[ -f "$file" ]]; then
    # Print the file being processed
    echo "Processing file: $file"
 
    # Run the main.py script with the file path as an argument
    python3 main.py "$file"
 
    # Check if the Python script ran successfully
    if [[ $? -eq 0 ]]; then
      echo "Successfully processed $file"
    else
      echo "Failed to process $file"
    fi
 
    echo "-------------------------------"
  fi
done