# Kilu

Kilu is a YAML-based template system that allows you to generate project files for any type of project you indicate. With a simple and flexible syntax, Kilu makes it easy to define and manage project structures.

## Introduction

Kilu uses YAML to define project templates, which include the base directory for the project, as well as a list of file entries. Each file entry specifies the file's name and content. Kilu also supports Base64 encoding for binary file contents, allowing you to work with a wide range of file types.

## Examples

### Basic Kilu Template

```yaml
basedir: "your_project_directory"

files:
  - name: "file_name_1.ext"
    content: |
      This is the content of file_name_1.ext.

  - name: "file_name_2.ext"
    content: |
      This is the content of file_name_2.ext.
```

### Kilu Template with base64 encoded Binary file content

```yaml
basedir: "my_project_with_binary_files"

files:
  - name: "example.gif"
    content_base64: |
      R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7

  - name: "example.zip"
    content_base64: |
      UEsFBgAAAAAAAAAAAAAAAAAAAAAAAA==
```

## Examples of GPT generating Kilu templates for the user

In this section, we showcase how GPT can generate Kilu templates for users based on their requests. By leveraging GPT's natural language understanding capabilities, the model can create context-aware and relevant project templates.
These examples demonstrate how GPT can generate Kilu templates based on user requests, creating custom project structures that fit the user's specific needs.

### Example 1: Simple Python Project

**User request:** "Create a Kilu template for a simple Python project with a `main.py` file that prints 'Hello, World!'."

**GPT-generated Kilu template:**

```yaml
basedir: "simple_python_project"

files:
  - name: "main.py"
    content: |
      def main():
          print("Hello, World!")
          
      if __name__ == "__main__":
          main()


### Example 2: Basic HTML and CSS Project

User request: "Generate a Kilu template for a basic HTML and CSS project with an index.html file and a styles.css file."

GPT-generated Kilu template:

```yaml
basedir: "basic_html_css_project"

files:
  - name: "index.html"
    content: |
      <!DOCTYPE html>
      <html lang="en">
      <head>
          <meta charset="UTF-8">
          <meta name="viewport" content="width=device-width, initial-scale=1.0">
          <link rel="stylesheet" href="styles.css">
          <title>Basic HTML and CSS Project</title>
      </head>
      <body>
          <h1>Welcome to the Basic HTML and CSS Project!</h1>
      </body>
      </html>

  - name: "styles.css"
    content: |
      body {
          font-family: Arial, sans-serif;
          background-color: #f0f0f0;
      }

      h1 {
          color: #333;
      }
```


## Why Use Kilu with GPT

Kilu can be a powerful tool when combined with the Generative Pre-trained Transformer (GPT) models like OpenAI's GPT-3 or GPT-4. By using Kilu templates as input (or ask GPT to output Kilu...) for GPT, you can:

1. Generate custom code snippets or configurations for different programming languages and frameworks.
2. Automate the creation of project files or folder structures based on user input or other criteria.
3. Leverage GPT's natural language understanding capabilities to generate more context-aware and relevant project files.
4. Summarize, Analyze third-party Kilu templates for security issues, functionality, or easily update an entire project dynamically.

The combination of Kilu's simplicity and GPT's advanced language modeling capabilities opens up a world of possibilities for creating dynamic and intelligent project templates that adapt to your specific needs.

## About the Author

Arturo "Buanzo" Busleiman is the creator of Kilu. With extensive experience in the software development and technology industry, Buanzo has a passion for creating tools that simplify and streamline the development process, empowering developers to focus on building great projects.

Visit [github.com/buanzo](https://github.com/buanzo) to see more of Buanzo's work.

