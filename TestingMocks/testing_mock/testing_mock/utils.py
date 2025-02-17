import csv

def parse_csv(csv_string: str) -> list[dict[str, str]]:
    data = []
    lines = csv_string.strip().splitlines()

    if not lines:
        return data

    header = lines[0].strip()
    reader = csv.reader(lines)
    header_list = next(reader)
    
    try:
        for row in reader:
            cleaned_row = {header_name.strip(): "" for header_name in header_list}
            for i, value in enumerate(row):
                if i < len(header_list):
                    header_name = header_list[i].strip()
                    cleaned_row[header_name] = value.strip()
            data.append(cleaned_row)
    except Exception as e:
        raise ValueError(f"Error parsing CSV: {e}")

    return data