
from blocks import *
import os
import shutil
from pathlib import Path



def copy_static():

    print("starting copy static")

    static_dir = os.path.join(os.getcwd(), "static")
    public_dir = os.path.join(os.getcwd(), "public")
   
    if os.path.exists(public_dir):
        shutil.rmtree(public_dir)
    os.mkdir(public_dir)

    def copy_rec(src, dst):
        if os.path.isfile(src):
            shutil.copy(src,dst)
            print(f"Copied file: {src} to {dst}")
        elif os.path.isdir(src):
            os.makedirs(dst, exist_ok=True)
            for item in os.listdir(src):
                s = os.path.join(src, item)
                d = os.path.join(dst, item)
                copy_rec(s, d)

    copy_rec(static_dir, public_dir)
   
def extract_title(markdown):

    lines = markdown.split('\n') # Double newline to specify paragraph

    for line in lines:
        if line.startswith("# "):
            line = line[2:len(line)]
            stripped = line.strip()
            return stripped

    raise Exception("h1 not found")  


def generate_page(from_path, template_path, dest_path):

    print(f"Generating page from {from_path} to {dest_path} using {template_path}...")

    with open(from_path, 'r') as f:
        from_file = f.read()
    
    with open(template_path, 'r') as t:
        template = t.read()
    
    node = markdown_to_html_node(from_file)
    html_string = node.to_html()

    heading = extract_title(from_file)

    template = template.replace("{{ Title }}", heading)
    template = template.replace("{{ Content }}", html_string)

    # Ensure the destination directory exists
    os.makedirs(os.path.dirname(dest_path), exist_ok=True)

    with open(dest_path, 'w') as d:
       d.write(template)
    
def generate_pages_recursive(dir_path_content, template_path, dest_dir_path):
    for filename in os.listdir(dir_path_content):
        from_path = os.path.join(dir_path_content, filename)
        dest_path = os.path.join(dest_dir_path, filename)
        if os.path.isfile(from_path):
            dest_path = Path(dest_path).with_suffix(".html")
            generate_page(from_path, template_path, dest_path)
        else:
            generate_pages_recursive(from_path, template_path, dest_path)
    
def main():
    copy_static() # function defined earlier

    shutil.rmtree("public")
    public_dir = os.path.join(os.getcwd(), "public")
    os.makedirs(public_dir)
   # Copy static files
    static_dir = os.path.join(os.getcwd(), "static")
    shutil.copytree(static_dir, public_dir, dirs_exist_ok=True)
    generate_pages_recursive("content", "template.html", "public")
    print("Site generated successfully!")

    

if __name__ == "__main__":
    main()