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
        if all(value.strip() == '' for value in row.values() if value is not None):
            continue
            
        cleaned_row = {}
        for key, value in row.items():
            clean_val = value.strip() if value else ""
            
            if key in ['first_name', 'LAST_name']:
                clean_val = clean_val.title()
            elif key == 'email':
                clean_val = clean_val.lower()
                
            cleaned_row[key.lower()] = clean_val
            
        cleaned.append(cleaned_row)
        
    return cleaned

def write_csv(data, output_path):
    """Writes the cleaned data list of dictionaries to a new CSV file."""
    if not data:
        print("No data to write!")
        return

    # Extract headers from the keys of the first dictionary
    headers = data[0].keys()
    print(f"Writing clean data to {output_path}...")

    with open(output_path, mode='w', encoding='utf-8', newline='') as file:
        writer = csv.DictWriter(file, fieldnames=headers)
        writer.writeheader()
        writer.writerows(data)
        
    print("Export complete!")

if __name__ == "__main__":
    input_file = "messy_data.csv"
    output_file = "cleaned_data.csv"
    
    # 1. Pipeline execution
    raw_dataset = read_csv(input_file)
    clean_dataset = clean_data(raw_dataset)
    write_csv(clean_dataset, output_file)