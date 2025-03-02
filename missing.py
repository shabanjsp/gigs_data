# File paths
filenames_file = "filenames.txt"
website_dev_file = "websiteDevelopment(5)id.txt"
output_file = "missing_gig_ids.txt"

# Read filenames.txt (gig IDs extracted from filenames)
with open(filenames_file, "r") as file:
    filenames_ids = set(file.read().splitlines())  # Convert to set for fast lookup

# Read websiteDevelopment(5)id.txt (original gig IDs)
with open(website_dev_file, "r") as file:
    website_dev_ids = set(file.read().splitlines())  # Convert to set for fast lookup

# Find gig IDs that are in websiteDevelopment(5)id.txt but NOT in filenames.txt
missing_ids = website_dev_ids - filenames_ids

# Save missing gig IDs to a file
with open(output_file, "w") as file:
    for gig_id in missing_ids:
        file.write(gig_id + "\n")

print(f"Found {len(missing_ids)} missing gig IDs. Saved to {output_file}.")
