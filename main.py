import os
from converters.csv_converter import csv_to_json, json_to_csv
from converters.json_converter import json_to_csv, csv_to_json
from converters.xml_converter import xml_to_json, json_to_xml
from converters.yaml_converter import yaml_to_json, json_to_yaml
from converters.markdown_converter import markdown_to_html
from converters.html_converter import html_to_markdown

INPUT_DIR = "input"
OUTPUT_DIR = "output"


def get_file_name(extension):
    """
    Prompts the user to input a file name with a specific extension.

    Args:
        extension (str): The required file extension.

    Returns:
        str: The name of the file with the specified extension.
    """
    file_name = input(f"Enter the {extension} file name (with extension): ")
    if file_name.endswith(extension):
        return file_name
    else:
        print(f"File name must end with {extension}.")
        return None


def main():
    """
    Main function to handle user interaction for file conversions.
    It presents a menu of conversion options and executes the selected conversion.
    """
    while True:
        print("\nFile Converter")
        print("1. CSV to JSON")
        print("2. JSON to CSV")
        print("3. XML to JSON")
        print("4. JSON to XML")
        print("5. YAML to JSON")
        print("6. JSON to YAML")
        print("7. Markdown to HTML")
        print("8. HTML to Markdown")

        choice = input("Select an option: ")
        if choice == "1":
            csv_file = get_file_name(".csv")
            if csv_file:
                csv_to_json(os.path.join(INPUT_DIR, csv_file),
                            os.path.join(OUTPUT_DIR, csv_file.replace(".csv", ".json")))
        elif choice == "2":
            json_file = get_file_name(".json")
            if json_file:
                json_to_csv(os.path.join(INPUT_DIR, json_file),
                            os.path.join(OUTPUT_DIR, json_file.replace(".json", ".csv")))
        elif choice == "3":
            xml_file = get_file_name(".xml")
            if xml_file:
                xml_to_json(os.path.join(INPUT_DIR, xml_file),
                            os.path.join(OUTPUT_DIR, xml_file.replace(".xml", ".json")))
        elif choice == "4":
            json_file = get_file_name(".json")
            if json_file:
                json_to_xml(os.path.join(INPUT_DIR, json_file),
                            os.path.join(OUTPUT_DIR, json_file.replace(".json", ".xml")))
        elif choice == "5":
            yaml_file = get_file_name(".yaml")
            if yaml_file:
                yaml_to_json(os.path.join(INPUT_DIR, yaml_file),
                             os.path.join(OUTPUT_DIR, yaml_file.replace(".yaml", ".json")))
        elif choice == "6":
            json_file = get_file_name(".json")
            if json_file:
                json_to_yaml(os.path.join(INPUT_DIR, json_file),
                             os.path.join(OUTPUT_DIR, json_file.replace(".json", ".yaml")))
        elif choice == "7":
            markdown_file = get_file_name(".md")
            if markdown_file:
                markdown_to_html(os.path.join(INPUT_DIR, markdown_file),
                                 os.path.join(OUTPUT_DIR, markdown_file.replace(".md", ".html")))
        elif choice == "8":
            html_file = get_file_name(".html")
            if html_file:
                html_to_markdown(os.path.join(INPUT_DIR, html_file),
                                 os.path.join(OUTPUT_DIR, html_file.replace(".html", ".md")))
        else:
            print("Invalid choice. Please try again.")

        continue_choice = input("\nDo you want to perform another conversion? (y/n): ")
        if continue_choice.lower() != 'y':
            break


if __name__ == "__main__":
    main()
