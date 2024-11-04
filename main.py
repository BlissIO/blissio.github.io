import os
import re
from datetime import datetime

TEMPLATE_FILE = "template.html"  # Path to the HTML template file
OUTPUT_DIR = "generated"         # Output directory for the generated HTML
BLOG_TAG = "{{blog_content}}"    # Placeholder for the blog content in the template

def load_template():
    """Load the HTML template file with UTF-8 encoding."""
    if not os.path.exists(TEMPLATE_FILE):
        print(f"Template file '{TEMPLATE_FILE}' not found!")
        return None
    with open(TEMPLATE_FILE, "r", encoding="utf-8") as file:
        return file.read()

def get_blog_content(filename):
    """Load the blog content from a specified input file."""
    if not os.path.exists(filename):
        print(f"Blog content file '{filename}' not found!")
        return None
    with open(filename, "r", encoding="utf-8") as file:
        return file.read()

def generate_blog_filename(title):
    """Generate a filename for the blog post based on the title and date."""
    date_str = datetime.now().strftime("%Y-%m-%d")
    # Replace any characters that aren't alphanumeric or hyphens with an empty string
    title_slug = re.sub(r'[^a-zA-Z0-9\-]', '', title.lower().replace(" ", "-"))
    filename = f"{date_str}-{title_slug}.html"
    return os.path.join(OUTPUT_DIR, filename)

def save_blog_file(filename, content):
    """Save the generated HTML content to a file."""
    os.makedirs(OUTPUT_DIR, exist_ok=True)
    with open(filename, "w", encoding="utf-8") as file:
        file.write(content)
    print(f"Generated blog saved to '{filename}'")

def main():
    # Load the template
    template = load_template()
    if template is None:
        return

    # Get input for the blog post
    title = input("Enter the blog title: ")
    date = input("Enter the blog date (YYYY-MM-DD) or leave blank for today: ") or datetime.now().strftime("%Y-%m-%d")
    blog_content_file = input("Enter the path to the blog content file (e.g., blog_content.txt): ")

    # Load the blog content from the specified file
    blog_content = get_blog_content(blog_content_file)
    if blog_content is None:
        return

    # Replace placeholders in the template with actual data
    blog_html = template.replace("{{title}}", title)
    blog_html = blog_html.replace("{{date}}", date)
    blog_html = blog_html.replace(BLOG_TAG, blog_content)

    # Generate a filename and save the HTML file
    output_filename = generate_blog_filename(title)
    save_blog_file(output_filename, blog_html)

if __name__ == "__main__":
    main()
