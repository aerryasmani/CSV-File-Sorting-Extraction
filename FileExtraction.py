import os
import pandas as pd
from PyPDF2 import PdfReader
import re

# Folder path containing the PDF files
folder_path = r'C:\Users\USER\Desktop\PythonTest\Employee Registration 2020\Employee Registration 2020\Employee Registration Aug 2020'

# List all files in the folder with a .pdf extension
pdf_files = [file for file in os.listdir(folder_path) if file.endswith('.pdf')]

# Create a list to store PDF content
pdf_contents = []

# Extract text from PDFs and store in the list
for pdf_file in pdf_files:
    file_path = os.path.join(folder_path, pdf_file)
    with open(file_path, 'rb') as file:
        pdf_reader = PdfReader(file)
        text = ''
        for page in pdf_reader.pages:
            text += page.extract_text()

        # Extracting specific information from the file name
        file_name_parts = pdf_file.split('_')  # File names are structured with '' as separator
        name_from_file_name = ' '.join(file_name_parts[:2])  # Extracting first and last name from file name parts
        joined_month_from_file_name = file_name_parts[-1].split('.')[0]  # Extracting joined month from file name

        # Extracting email and employee ID from the content using patterns
        emails = re.findall(r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b', text)
        employee_id = re.search(r'Employee ID: (\d+)', text)

        # Creating a dictionary for each PDF file with extracted data
        pdf_content = {
            'File Name': pdf_file,
            'Name': name_from_file_name,
            'Joined Date': joined_month_from_file_name,
            'Email': ', '.join(emails) if emails else None,
            'Employee ID': employee_id.group(1) if employee_id else None
        }

        # Appending extracted data for each PDF to the list
        pdf_contents.append(pdf_content)

# Creating a DataFrame from the list of contents
pdf_data = pd.DataFrame(pdf_contents)

# Initialize counter for file numbering
counter = 1
excel_file_path = os.path.join(folder_path, f'PDFExcel_{counter}.xlsx')

# Counter if the name file already exist
while os.path.exists(excel_file_path):
    counter += 1
    excel_file_path = os.path.join(folder_path, f'PDFExcel_{counter}.xlsx')

# Save PDF content into an Excel file
pdf_data.to_excel(excel_file_path, index=False)