import os
import sys
import yaml
import base64
from pathlib import Path

def is_text_file(file_path):
    try:
        with open(file_path, "rt") as file:
            file.read()
        return True
    except UnicodeDecodeError:
        return False

def should_include(file_path):
    ignored_items = ['.git']
    for item in ignored_items:
        if item in file_path.parts:
            return False
    return True

def dir_to_kilu_template(basedir, output_file):
    basedir_path = Path(basedir).resolve()

    if not basedir_path.is_dir():
        print(f"Error: {basedir} is not a valid directory")
        sys.exit(1)

    template = {
        "basedir": basedir_path.name,
        "files": []
    }

    for root, _, files in os.walk(basedir_path):
        for file in files:
            file_path = Path(root) / file
            if not should_include(file_path):
                continue

            relative_path = file_path.relative_to(basedir_path)
            if is_text_file(file_path):
                with open(file_path, "r") as f:
                    content = f.read()
                template["files"].append({
                    "name": str(relative_path),
                    "content": content
                })
            else:
                with open(file_path, "rb") as f:
                    content = f.read()
                content_base64 = base64.b64encode(content).decode("utf-8")
                template["files"].append({
                    "name": str(relative_path),
                    "content_base64": content_base64
                })

    with open(output_file, "w") as f:
        yaml.dump(template, f, default_flow_style=False)

    print(f"Created Kilu template: {output_file}")

def main():
    if len(sys.argv) < 3:
        print("Usage: dir2kilu <basedir> <output_file>")
        sys.exit(1)

    basedir = sys.argv[1]
    output_file = sys.argv[2]

    dir_to_kilu_template(basedir, output_file)

if __name__ == "__main__":
    main()
