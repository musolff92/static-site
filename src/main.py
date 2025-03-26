import os
import shutil
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

def generate_page(from_path, template_path, dest_path):
    print(f"Generating page from {from_path} to {dest_path} using {template_path}")

    with open(from_path, "r") as f:
        markdown = f.read()
    
    with open(template_path, "r") as f:
        template = f.read()
    
    html_node = markdown_to_html_node(markdown)
    html_content = html_node.to_html()

    title = extract_title(markdown)

    full_html = template.replace("{{ Title }}", title).replace("{{ Content }}", html_content)

    os.makedirs(os.path.dirname(dest_path), exist_ok=True)

    with open(dest_path, "w") as f:
        f.write(full_html)

######################################
def generate_pages_recursive(dir_path_content, template_path, dest_dir_path):

    for item in dir_path_content:
        if item.isdirectory == True:
            generate_pages_recursive(item)
        else:
            generate_page(dir_path_content)




def main():
    copy_static("static", "public")

    generate_page(
        from_path="content/index.md",
        template_path="template.html",
        dest_path="public/index.html"
    )

    
main()