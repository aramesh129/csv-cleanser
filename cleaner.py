import csv
import os

def read_csv(file_path):
    """Opens and reads a CSV file, returning a list of dictionaries."""
    print(f"Reading data from {file_path}...")
    
    if not os.path.exists(file_path):
        print("Error: File not found!")
        return []

    raw_data = []
    with open(file_path, mode='r', encoding='utf-8') as file:
        reader = csv.DictReader(file)
        reader.fieldnames = [field.strip() for field in reader.fieldnames]
        for row in reader:
            raw_data.append(row)
            
    return raw_data

def clean_data(raw_data):
    """Cleans the raw data by removing empty rows and formatting strings."""
    print("Sanitizing data...")
    cleaned = []
    
    for row in raw_data:
        # 1. Skip rows where every single column is blank or just spaces
        if all(value.strip() == '' for value in row.values() if value is not None):
            continue
            
        cleaned_row = {}
        for key, value in row.items():
            clean_val = value.strip() if value else ""
            
            # 2. Format specific columns properly
            if key in ['first_name', 'LAST_name']:
                clean_val = clean_val.title() # e.g., jOhn -> John, smith -> Smith
            elif key == 'email':
                clean_val = clean_val.lower() # e.g., MIKE@email.com -> mike@email.com
                
            cleaned_row[key.lower()] = clean_val
            
        cleaned.append(cleaned_row)
        
    return cleaned

if __name__ == "__main__":
    input_file = "messy_data.csv"
    
    # Step 1: Read the data
    data = read_csv(input_file)
    
    # Step 2: Clean the data
    clean_dataset = clean_data(data)
    
    print("\n--- BEFORE (Sample Messy Row) ---")
    print(data[1])
    
    print("\n--- AFTER (Sample Cleaned Row) ---")
    print(clean_dataset[1])