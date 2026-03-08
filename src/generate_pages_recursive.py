import os
from generate_page import generate_page

def generate_pages_recursive(dir_path_content, template_path, dest_dir_path, basepath):
    for entry in os.listdir(dir_path_content):
        from_path = os.path.join(dir_path_content, entry)
        dest_path = os.path.join(dest_dir_path, entry)

        if os.path.isfile(from_path):
            if from_path.endswith(".md"):
                dest_path = dest_path[:-3] + ".html"
                generate_page(from_path, template_path, dest_path, basepath)
        else:
            os.makedirs(dest_path, exist_ok=True)
            generate_pages_recursive(from_path, template_path, dest_path, basepath)