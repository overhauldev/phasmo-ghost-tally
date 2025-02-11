import zipfile
import os

# Define the files to include in the ZIP
files_to_include = ['dist/phas_tally.exe', 'tally_counts.json', 'requirements.txt', 'README.txt']

# Create a ZIP file
with zipfile.ZipFile('phas_tally.zip', 'w') as zipf:
    for file in files_to_include:
        zipf.write(file, os.path.basename(file))

print("phas_tally.zip created successfully.")