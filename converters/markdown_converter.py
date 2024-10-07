import markdown


def markdown_to_html(markdown_file, html_file):
    """
    Converts a Markdown file to an HTML file.

    Args:
        markdown_file (str): Path to the input Markdown file.
        html_file (str): Path where the output HTML file will be saved.

    Raises:
        Exception: If an error occurs while reading the Markdown or writing the HTML file.
    """
    try:
        with open(markdown_file, 'r') as file:
            text = file.read()
        html = markdown.markdown(text)
        with open(html_file, 'w') as file:
            file.write(html)
        print(f"Successfully converted {markdown_file} to {html_file}")
    except Exception as e:
        print(f"Error: {e}")
