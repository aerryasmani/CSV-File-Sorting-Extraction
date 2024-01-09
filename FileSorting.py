import os
import shutil

# Function to generate a new filename based on month and year
def generate_new_filename(month_year):
    return f"newjoiners_{month_year}2020.csv"

# Path to the main folder containing subfolders for each month
main_folder = r'C:\Users\USER\Desktop\PythonTest\Employee Registration 2020'

# Create a new folder if it doesn't exist
Convertfolder = os.path.join(main_folder, 'NewEmployees2020Clean')
os.makedirs(Convertfolder, exist_ok=True)

# Iterate through each subfolder
for root, dirs, files in os.walk(main_folder):
    for file in files:
        if file.endswith('.csv'):
            # Extract month and year from the subfolder path
            month_year = os.path.basename(root)
            
            # Construct the new filename following the specified format
            new_filename = generate_new_filename(month_year)
            
            # Path to the original file
            original_path = os.path.join(root, file)
            
            # Path to the new destination file
            destination_file_path = os.path.join(Convertfolder, new_filename)
            
            # Copy the file to the new destination folder with the new name
            shutil.copy2(original_path, destination_file_path)
