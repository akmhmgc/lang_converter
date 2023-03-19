import os
import openai

def list_files(path, extension=".rb"):
    return [os.path.join(path, f) for f in os.listdir(path) if f.endswith(extension)]

openai.api_key = os.getenv("OPENAI_API_KEY")

def convert_ruby_to_python(ruby_code):
    prompt = f"Convert the following Ruby code to equivalent Python code:\n\n```ruby\n{ruby_code}\n```\n\nPython code:\n\n```python\n"

    response = openai.Completion.create(
        engine="davinci-codex",
        prompt=prompt,
        max_tokens=2048,  # Increase the token limit if necessary
        n=1,
        stop="```",
        temperature=0.5,
    )

    python_code = response.choices[0].text.strip()
    return python_code

def convert_ruby_files_to_python(files, output_dir):
    ruby_code_combined = ""

    for file in files:
        with open(file, 'r') as ruby_file:
            ruby_code = ruby_file.read()
            ruby_code_combined += f"# {os.path.basename(file)}\n{ruby_code}\n\n"

    python_code_combined = convert_ruby_to_python(ruby_code_combined)

    for file, python_code in zip(files, python_code_combined.split("\n\n")):
        output_file = os.path.join(output_dir, os.path.basename(file).replace(".rb", ".py"))
        with open(output_file, 'w') as python_file:
            python_file.write(python_code)

ruby_directory = "./ruby"
output_directory = "./python"

if not os.path.exists(output_directory):
    os.makedirs(output_directory)

ruby_files = list_files(ruby_directory, extension=".rb")
convert_ruby_files_to_python(ruby_files, output_directory)
