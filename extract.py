import os

# Folder containing JSON files
folder_path = "gigs website development (7)"

# Output file
output_file = "filenames.txt"

# Get all JSON filenames without extension
json_files = [os.path.splitext(f)[0] for f in os.listdir(folder_path) if f.endswith(".json")]

# Save to a text file
with open(output_file, "w") as file:
    for name in json_files:
        file.write(name + "\n")

print(f"Extracted {len(json_files)} filenames (without .json) and saved to {output_file}.")
