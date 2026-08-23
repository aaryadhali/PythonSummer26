# from pypdf import PdfReader

# reader = PdfReader("Grades for Aarya Dhaliwal_ 2026SU MATH4322 13424 - Introduction to Data Science and Machine Learning.pdf")

# print(len(reader.pages))
# # Extract text from the first page
# page = reader.pages[0]
# text = page.extract_text()

# print(type(text))
# print(text)

import pdfplumber

with pdfplumber.open("Grades for Aarya Dhaliwal_ 2026SU MATH4322 13424 - Introduction to Data Science and Machine Learning.pdf") as pdf:
    first_page = pdf.pages[0]
    print(first_page.chars[0])
    table = []
    for page in pdf.pages:
        table = page.extract_table()
        print("\n")
    print(table, end="\n")



    # Install required libraries: pip install pdfplumber pandas
import pdfplumber
import pandas as pd

all_rows = []

with pdfplumber.open("Grades for Aarya Dhaliwal_ 2026SU MATH4322 13424 - Introduction to Data Science and Machine Learning.pdf") as pdf:
    for page in pdf.pages:
        # Extract table matrix from the page
        table = page.extract_table()
        if table:
            for row in table:
                # Filter out empty rows or structural header duplicates
                if row and any(row): 
                    all_rows.append(row)

# Convert into a structured pandas DataFrame
df = pd.DataFrame(all_rows)

# Clean it up: remove unnecessary top rows and set column names
print(df.head(10))

# Save directly to an Excel-friendly CSV file
df.to_csv("canvas_grades.csv", index=False)
