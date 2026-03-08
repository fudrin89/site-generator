import os
from markdown_to_html_node import markdown_to_html_node
from extract_title import extract_title

def generate_page(from_path, template_path, dest_path, basepath):
    print(f"Generating page from {from_path} to {dest_path} using {template_path}")

    with open(from_path, "r", encoding="utf-8") as f:
        markdown = f.read()

    with open(template_path, "r", encoding="utf-8") as f:
        template = f.read()

    content_html = markdown_to_html_node(markdown).to_html()
    title = extract_title(markdown)

    page_html = template.replace("{{ Title }}", title)
    page_html = page_html.replace("{{ Content }}", content_html)

    page_html = page_html.replace('href="/', f'href="{basepath}')
    page_html = page_html.replace('src="/', f'src="{basepath}')

    dest_dir = os.path.dirname(dest_path)
    if dest_dir:
        os.makedirs(dest_dir, exist_ok=True)

    with open(dest_path, "w", encoding="utf-8") as f:
        f.write(page_html)