import json
import os

# Define the input and output directories
input_directory = 'website development (5)'
output_file = 'websiteDevelopment(5).txt'

# Set to store unique gig URLs
unique_gig_urls = set()

# Iterate over all JSON files in the input directory
for filename in os.listdir(input_directory):
    if filename.endswith('.json'):
        input_path = os.path.join(input_directory, filename)
        
        try:
            # Open the file with UTF-8 encoding
            with open(input_path, 'r', encoding='utf-8') as file:
                data = json.load(file)
            
            # Extract gig_url from each gig in listings
            for listing in data.get('listings', []):
                for gig in listing.get('gigs', []):
                    gig_url = gig.get("gig_url")
                    if gig_url:
                        unique_gig_urls.add(gig_url)
        
            print(f"Processed file: {filename}")
        
        except (UnicodeDecodeError, json.JSONDecodeError) as e:
            print(f"Error processing file '{filename}': {e}")
        except Exception as e:
            print(f"An unexpected error occurred with file '{filename}': {e}")

# Write unique gig URLs to output file
with open(output_file, 'w', encoding='utf-8') as txt_file:
    for gig_url in unique_gig_urls:
        txt_file.write(f"{gig_url}\n")

print("All JSON files have been processed. Unique gig URLs saved in gigs.txt")
