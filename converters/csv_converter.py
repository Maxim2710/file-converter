import csv
import json


def csv_to_json(csv_file, json_file):
    """
    Converts a CSV file to a JSON file.

    Args:
        csv_file (str): Path to the input CSV file.
        json_file (str): Path where the output JSON file will be saved.

    Raises:
        Exception: If an error occurs while reading the CSV or writing the JSON file.
    """
    data = []
    try:
        with open(csv_file, 'r') as file:
            reader = csv.DictReader(file)
            for row in reader:
                data.append(row)
        with open(json_file, 'w') as file:
            json.dump(data, file, indent=4)
        print(f"Successfully converted {csv_file} to {json_file}")
    except Exception as e:
        print(f"Error: {e}")


def json_to_csv(json_file, csv_file):
    """
    Converts a JSON file to a CSV file.

    Args:
        json_file (str): Path to the input JSON file.
        csv_file (str): Path where the output CSV file will be saved.

    Raises:
        Exception: If an error occurs while reading the JSON or writing the CSV file.
    """
    try:
        with open(json_file, 'r') as file:
            data = json.load(file)
        with open(csv_file, 'w', newline='') as file:
            writer = csv.DictWriter(file, fieldnames=data[0].keys())
            writer.writeheader()
            writer.writerows(data)
        print(f"Successfully converted {json_file} to {csv_file}")
    except Exception as e:
        print(f"Error: {e}")
