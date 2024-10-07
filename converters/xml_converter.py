import xml.etree.ElementTree as ET
import json


def xml_to_json(xml_file, json_file):
    """
    Converts an XML file to a JSON file.

    Args:
        xml_file (str): Path to the input XML file.
        json_file (str): Path where the output JSON file will be saved.

    Raises:
        Exception: If an error occurs while reading the XML or writing the JSON file.
    """
    try:
        tree = ET.parse(xml_file)
        root = tree.getroot()
        data = []

        def parse_element(element):
            """
            Recursively parses an XML element and its children into a dictionary.

            Args:
                element (xml.etree.ElementTree.Element): The XML element to parse.

            Returns:
                dict: A dictionary representation of the XML element.
            """
            obj = {}
            for child in element:
                obj[child.tag] = child.text if len(child) == 0 else parse_element(child)
            return obj

        for child in root:
            data.append(parse_element(child))

        with open(json_file, 'w') as file:
            json.dump(data, file, indent=4)
        print(f"Successfully converted {xml_file} to {json_file}")
    except Exception as e:
        print(f"Error: {e}")


def json_to_xml(json_file, xml_file):
    """
    Converts a JSON file to an XML file.

    Args:
        json_file (str): Path to the input JSON file.
        xml_file (str): Path where the output XML file will be saved.

    Raises:
        Exception: If an error occurs while reading the JSON or writing the XML file.
    """
    try:
        with open(json_file, 'r') as file:
            data = json.load(file)

        def build_xml(element, data):
            """
            Recursively builds XML elements from a dictionary.

            Args:
                element (xml.etree.ElementTree.Element): The parent XML element.
                data (dict): The dictionary to convert to XML.
            """
            for key, value in data.items():
                child = ET.SubElement(element, key)
                if isinstance(value, dict):
                    build_xml(child, value)
                else:
                    child.text = str(value)

        root = ET.Element('root')
        for item in data:
            item_element = ET.SubElement(root, 'item')
            build_xml(item_element, item)

        tree = ET.ElementTree(root)
        tree.write(xml_file)
        print(f"Successfully converted {json_file} to {xml_file}")
    except Exception as e:
        print(f"Error: {e}")
