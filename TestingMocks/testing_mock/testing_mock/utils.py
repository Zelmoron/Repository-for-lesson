import csv

def parse_csv(csv_string: str) -> list[dict[str, str]]:
    data = []
    lines = csv_string.strip().split("\n")
    if not lines:
        return data

    reader = csv.DictReader(lines)
    for row in reader:
        data.append(row)
        
    return data