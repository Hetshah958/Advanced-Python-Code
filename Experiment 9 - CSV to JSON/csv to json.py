import csv
import json
from pathlib import Path

def csv_to_json(csv_path: str | Path, json_path: str | Path) -> None:
    """Convert each CSV row into a dictionary and write the records as JSON."""
    records = []
    with open(csv_path, "r", newline="", encoding="utf-8") as csv_file:
        for row in csv.DictReader(csv_file):
            records.append(row)

    with open(json_path, "w", encoding="utf-8") as json_file:
        json.dump(records, json_file, indent=4, ensure_ascii=False)

    print(f"Converted {len(records)} records from {csv_path} to {json_path}.")

if __name__ == "__main__":
    input_file = Path(__file__).with_name("input.csv")
    output_file = Path(__file__).with_name("output.json")
    csv_to_json(input_file, output_file)
    print(output_file.read_text(encoding="utf-8"))
