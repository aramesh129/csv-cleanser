# CSV Data Cleanser

A automated pipeline built in Python to ingest, sanitize, and export unstructured data fields from low quality CSV documents into clean datasets.

## Features

- Row Validation: Drops corrupted records where all column fields are null or empty.

- String Sanitization: Automatically strips leading and trailing whitespaces from both headers and data strings.

- Casing Normalization: Enforces standard structural formatting across sensitive keys (e.g., lowercase mutations for emails and proper title casing for names).

## How to Run

Place your target file inside the working directory and title it `messy data.csv`. 

Run the processing pipeline using your Python runtime environment:

```bash
python cleaner.py
```
Open the newly generated `cleaned_data.csv` file inside your workspace to review your structured dataset.
