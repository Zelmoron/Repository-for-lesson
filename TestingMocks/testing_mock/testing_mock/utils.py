import csv

def parse_csv(csv_string: str) -> list[dict[str, str]]:
    """
    Parses a CSV string into a list of dictionaries.

    Each dictionary represents a row in the CSV data, where keys are column names and values are cell contents.

    Args:
        csv_string (str): The CSV data as a string.

    Returns:
        list[dict[str, str]]: A list of dictionaries representing the parsed CSV data.

    Raises:
        ValueError: If an error occurs during parsing.
    """
    data = []
    lines = csv_string.strip().splitlines()

    if not lines:
        return data

    # Extract the header line (not used directly, but included for clarity)
    header = lines[0].strip()
    
    # Create a CSV reader from the lines
    reader = csv.reader(lines)
    
    # Extract the header list from the reader
    header_list = next(reader)
    
    try:
        # Iterate over each row in the CSV data
        for row in reader:
            # Initialize a cleaned row dictionary with empty values
            cleaned_row = {header_name.strip(): "" for header_name in header_list}
            
            # Populate the cleaned row dictionary with actual values
            for i, value in enumerate(row):
                if i < len(header_list):
                    header_name = header_list[i].strip()
                    cleaned_row[header_name] = value.strip()
            
            # Append the cleaned row to the data list
            data.append(cleaned_row)
    except Exception as e:
        # Raise a ValueError if any exception occurs during parsing
        raise ValueError(f"Error parsing CSV: {e}")

    return data