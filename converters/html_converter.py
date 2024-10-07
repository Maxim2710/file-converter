from markdown2 import markdown


def html_to_markdown(html_file, markdown_file):
    """
    Converts an HTML file to a Markdown file.

    Args:
        html_file (str): Path to the input HTML file.
        markdown_file (str): Path where the output Markdown file will be saved.

    Raises:
        Exception: If an error occurs while reading the HTML or writing the Markdown file.
    """
    try:
        with open(html_file, 'r') as file:
            html = file.read()
        markdown_text = markdown(html)
        with open(markdown_file, 'w') as file:
            file.write(markdown_text)
        print(f"Successfully converted {html_file} to {markdown_file}")
    except Exception as e:
        print(f"Error: {e}")
