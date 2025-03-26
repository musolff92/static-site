import os
import shutil
import sys
from block_parser import markdown_to_html_node
#from textnode import TextNode

def copy_static(src, dst):
    if os.path.exists(dst):
        shutil.rmtree(dst)
    os.makedirs(dst)

    for item in os.listdir(src):
        s_item = os.path.join(src, item)
        d_item = os.path.join(dst, item)

        if os.path.isdir(s_item):
            copy_static(s_item, d_item)
        else:
            shutil.copy(s_item, d_item)
            print(f"Copied {s_item} to {d_item}")

def extract_title(markdown):
    for line in markdown.split("\n"):
        if line.startswith("# "):
            return line.lstrip("# ").strip()
    raise Exception("No h1 header found")

def generate_page(from_path, template_path, dest_path, base_path="/"):
    print(f"Generating page from {from_path} to {dest_path} using {template_path}")

    with open(from_path, "r") as f:
        markdown = f.read()
    
    with open(template_path, "r") as f:
        template = f.read()
    
    html_node = markdown_to_html_node(markdown)
    html_content = html_node.to_html()

    title = extract_title(markdown)

    full_html = template.replace("{{ Title }}", title).replace("{{ Content }}", html_content)

    full_html = full_html.replace('href="/', f'href="{base_path}')
    full_html = full_html.replace('src="/', f'src="{base_path}')

    os.makedirs(os.path.dirname(dest_path), exist_ok=True)

    with open(dest_path, "w") as f:
        f.write(full_html)

######################################
def generate_pages_recursive(dir_path_content, template_path, dest_dir_path, base_path):

    for item in os.listdir(dir_path_content):
        content_item_path = os.path.join(dir_path_content, item)
        dest_item_path = os.path.join(dest_dir_path, item)

        if os.path.isdir(content_item_path):
            generate_pages_recursive(content_item_path, template_path, dest_item_path, base_path)
        elif os.path.isfile(content_item_path) and item.endswith(".md"):
            dest_item_path = os.path.splitext(dest_item_path)[0] + ".html"

            os.makedirs(os.path.dirname(dest_item_path), exist_ok=True)

            generate_page(content_item_path, template_path, dest_item_path, base_path)




def main():
    base_path = sys.argv[1] if len(sys.argv) > 1 else "/"

    output_dir = "docs"
    
    copy_static("static", output_dir)

    generate_pages_recursive("content", "template.html", output_dir, base_path)

    
if __name__ == "__main__":
    main()