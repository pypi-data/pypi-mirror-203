import yaml
import os
import sys
import base64

def create_project_from_template(template_file):
    # Read the template from file
    with open(template_file, "r") as f:
        template = yaml.safe_load(f)

    # Create the project directory if it doesn't exist
    if not os.path.exists(template["basedir"]):
        os.mkdir(template["basedir"])
        print(f'Created {template["basedir"]}')

    # Create the files and write the contents
    for file in template["files"]:
        fn = os.path.join(template["basedir"], file["name"])

        # Create the parent directory if it doesn't exist
        os.makedirs(os.path.dirname(fn), exist_ok=True)

        if "content" in file:
            with open(fn, "w") as f:
                f.write(file["content"])
        elif "content_base64" in file:
            content = base64.b64decode(file["content_base64"])
            with open(fn, "wb") as f:
                f.write(content)
        print(f'Created {fn}')

def main_kilu():
    if len(sys.argv) < 2:
        print("Usage: kilu <template_file>")
        sys.exit(1)

    template_file = sys.argv[1]
    create_project_from_template(template_file)

def main_dir2kilu():
    if len(sys.argv) < 3:
        print("Usage: dir2kilu <basedir> <output_file>")
        sys.exit(1)

    basedir = sys.argv[1]
    output_file = sys.argv[2]

    from .dir2kilu import dir_to_kilu_template
    dir_to_kilu_template(basedir, output_file)


if __name__ == "__main__":
    main_kilu()
