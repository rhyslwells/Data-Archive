import os
import shutil
import re

# Define paths
selector_file = "Selector.md"  # File containing the list of selected files
source_folder = os.path.abspath("../../standardised")  # Source folder
destination_folder = os.path.abspath("./selected_files")  # Destination folder

# Ensure destination folder exists
os.makedirs(destination_folder, exist_ok=True)

# Read Selector.md and extract filenames from [[...]]
with open(selector_file, "r", encoding="utf-8") as f:
    files = [re.search(r"\[\[(.*?)\]\]", line).group(1) + ".md" 
             for line in f.readlines() if re.search(r"\[\[(.*?)\]\]", line)]

# Copy each selected file
for file_name in files:
    source_path = os.path.join(source_folder, file_name)
    destination_path = os.path.join(destination_folder, file_name)

    if os.path.exists(source_path):
        shutil.copy(source_path, destination_path)
        print(f"Copied: {file_name}")
    else:
        print(f"Warning: {file_name} not found in {source_folder}")

print("File copying completed.")
