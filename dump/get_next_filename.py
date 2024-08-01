# Function to get the next available filename in the sequence
import os
def get_next_filename(directory, prefix, extension):
    existing_files = [f for f in os.listdir(directory) if f.startswith(prefix) and f.endswith(extension)]
    existing_files.sort()
    
    if existing_files:
        last_file = existing_files[-1]
        last_num = int(last_file.split('_')[1].split('.')[0])
        next_num = last_num + 1
    else:
        next_num = 1
    
    return f"{prefix}_{next_num}.{extension}"