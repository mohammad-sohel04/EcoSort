import os
import csv
# Function to log the image filename and its associated tag to a CSV file
def log_to_csv(csv_path, filename, tag):
    file_exists = os.path.isfile(csv_path)
    
    with open(csv_path, mode='a', newline='') as csv_file:
        fieldnames = ['filename', 'tag']
        writer = csv.DictWriter(csv_file, fieldnames=fieldnames)
        
        if not file_exists:
            writer.writeheader()  # Write header only if the file doesn't exist
        
        writer.writerow({'filename': filename, 'tag': tag})