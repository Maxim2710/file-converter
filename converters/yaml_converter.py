import yaml
import json


def yaml_to_json(yaml_file, json_file):
    """
    Converts a YAML file to a JSON file.

    Args:
        yaml_file (str): Path to the input YAML file.
        json_file (str): Path where the output JSON file will be saved.

    Raises:
        Exception: If an error occurs while reading the YAML or writing the JSON file.
    """
    try:
        with open(yaml_file, 'r') as file:
            data = yaml.safe_load(file)
        with open(json_file, 'w') as file:
            json.dump(data, file, indent=4)
        print(f"Successfully converted {yaml_file} to {json_file}")
    except Exception as e:
        print(f"Error: {e}")


def json_to_yaml(json_file, yaml_file):
    """
    Converts a JSON file to a YAML file.

    Args:
        json_file (str): Path to the input JSON file.
        yaml_file (str): Path where the output YAML file will be saved.

    Raises:
        Exception: If an error occurs while reading the JSON or writing the YAML file.
    """
    try:
        with open(json_file, 'r') as file:
            data = json.load(file)
        with open(yaml_file, 'w') as file:
            yaml.dump(data, file)
        print(f"Successfully converted {json_file} to {yaml_file}")
    except Exception as e:
        print(f"Error: {e}")
