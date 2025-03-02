import os
import re

# Define the folder path
folder_path = 'gigs website development (5)'

# Regular expression to match files with (1), (2), etc.
pattern = re.compile(r'^(.*?) \(\d+\)\.json$')

# Iterate through all files in the folder
for filename in os.listdir(folder_path):
    # Check if the filename matches the pattern (i.e., it's a duplicate)
    match = pattern.match(filename)
    if match:
        # Extract the base name (e.g., "a_nauckhoff.json" from "a_nauckhoff (1).json")
        base_name = match.group(1) + '.json'
        
        # Check if the base file exists
        if os.path.exists(os.path.join(folder_path, base_name)):
            # If the base file exists, delete the duplicate
            os.remove(os.path.join(folder_path, filename))
            print(f"Deleted duplicate: {filename}")
        else:
            # If the base file doesn't exist, rename the duplicate to the base name
            os.rename(os.path.join(folder_path, filename), os.path.join(folder_path, base_name))
            print(f"Renamed {filename} to {base_name}")

print("Duplicate removal complete.")