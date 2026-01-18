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
        for row in reader:
            raw_data.append(row)
            
    return raw_data

if __name__ == "__main__":
    input_file = "messy_data.csv"
    
    data = read_csv(input_file)
    
    for index, row in enumerate(data[:3]):
        print(f"Row {index + 1}: {row}")
