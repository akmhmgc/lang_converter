# Ruby to Python Converter

## Requirements
This script requires an OpenAI API key, which can be obtained from the OpenAI website. The openai Python package is also required and can be installed via pip.

## Usage
1. Ensure that you have set the OPENAI_API_KEY environment variable to your OpenAI API key.
2. Place the Ruby files you want to convert in a directory.
3. Set the `ruby_directory` variable in the script to the directory containing your Ruby files.
4. Set the `output_directory` variable in the script to the directory where you want the Python files to be saved.
5. Run the script.

The Ruby files will be combined into a single string and passed as input to OpenAI's `davinci-codex` engine, which will generate Python code. The generated Python code will be split into individual files and saved in the output directory.

## Note
This script currently only supports conversion from Ruby to Python, and it assumes that the Ruby code adheres to standard syntax. Some manual adjustment may be required for more complex Ruby code.
