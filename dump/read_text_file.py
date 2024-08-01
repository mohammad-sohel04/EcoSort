import os
# Function to read content from a text file
def read_text_file(directory, filename):
    file_path = os.path.join(directory, filename)
    try:
        with open(file_path, 'r') as file:
            content = file.read()
            return content
    except FileNotFoundError:
        print(f"The file {filename} does not exist in the directory {directory}.")
        return None