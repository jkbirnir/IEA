pip install pdfplumber
pip install pandas

import pdfplumber
import pandas as pd

# Path to the PDF file
pdf_path = "filename.pdf"

# Initialize a list to store all tables
all_tables = []

# Open the PDF file
with pdfplumber.open(pdf_path) as pdf:
    for page_number, page in enumerate(pdf.pages, start=1):
        # Extract tables from the current page
        tables = page.extract_tables()
        
        # Process each table on the page
        for table_number, table in enumerate(tables, start=1):
            # Convert the table to a DataFrame
            df = pd.DataFrame(table)
            
            # Add metadata about the page and table number (optional)
            df["page_number"] = page_number
            df["table_number"] = table_number
            
            # Append to the list of all tables
            all_tables.append(df)

# Combine all tables into a single DataFrame
combined_table = pd.concat(all_tables, ignore_index=True)

# Save the combined table to a CSV file
combined_table.to_csv("output_tables_all.csv", index=False)

print("Tables extracted and saved to output_tables.csv")


