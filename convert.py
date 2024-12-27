import os
import json
import sys
from argparse import ArgumentParser

def read_params(file_path):
    try:
        with open(file_path, 'r') as file:
            return [line.strip() for line in file if line.strip()]
    except Exception as e:
        print(f"Error reading file: {e}")
        sys.exit(1)

def write_file(output_folder, filename, content):
    os.makedirs(output_folder, exist_ok=True)
    try:
        with open(os.path.join(output_folder, filename), 'w') as file:
            file.write(content)
    except Exception as e:
        print(f"Error writing file: {e}")
        sys.exit(1)

def generate_json(params, limit, output_folder):
    for i in range(0, len(params), limit):
        chunk = params[i:i + limit]
        json_content = {param: f"{param}null'" for param in chunk}
        write_file(output_folder, f"{i // limit + 1}.json", json.dumps(json_content, indent=4))

def generate_post_html(params, limit, output_folder):
    for i in range(0, len(params), limit):
        chunk = params[i:i + limit]
        html_content = "&".join([f"{param}={param}null'" for param in chunk])
        write_file(output_folder, f"{i // limit + 1}.txt", html_content)

def generate_get_html(params, limit, output_folder):
    for i in range(0, len(params), limit):
        chunk = params[i:i + limit]
        html_content = "&".join([f"{param}=null" for param in chunk])
        write_file(output_folder, f"{i // limit + 1}.txt", html_content)

def generate_xml(params, limit, output_folder):
    for i in range(0, len(params), limit):
        chunk = params[i:i + limit]
        xml_content = "<parameters>\n" + "\n".join([f"  <{param}>{param}null</{param}>" for param in chunk]) + "\n</parameters>"
        write_file(output_folder, f"{i // limit + 1}.xml", xml_content)

def generate_multipart(params, limit, output_folder):
    boundary = "----WebKitFormBoundary7MA4YWxkTrZu0gW"
    for i in range(0, len(params), limit):
        chunk = params[i:i + limit]
        multipart_content = "".join([f"--{boundary}\nContent-Disposition: form-data; name=\"{param}\"\n\n{param}null\n" for param in chunk])
        multipart_content += f"--{boundary}--"
        write_file(output_folder, f"{i // limit + 1}.txt", multipart_content)

def main():
    parser = ArgumentParser(description="Convert parameters into various formats.")
    parser.add_argument('-f', '--file', required=True, help="Path to the parameter file.")
    parser.add_argument('-limit', type=int, required=True, help="Number of parameters per output file.")
    parser.add_argument('-of', '--output-folder', required=True, help="Output folder and mode (e.g., paramjson, paramhtml, paramgethtml, paramxml, parammultipart).")

    args = parser.parse_args()

    params = read_params(args.file)
    if not params:
        print("Error: No parameters found in the file.")
        sys.exit(1)

    mode = args.output_folder.lower()
    limit = args.limit

    if mode == "paramjson":
        generate_json(params, limit, args.output_folder)
    elif mode == "paramhtml":
        generate_post_html(params, limit, args.output_folder)
    elif mode == "paramgethtml":
        generate_get_html(params, limit, args.output_folder)
    elif mode == "paramxml":
        generate_xml(params, limit, args.output_folder)
    elif mode == "parammultipart":
        generate_multipart(params, limit, args.output_folder)
    else:
        print(f"Error: Unsupported mode '{mode}'.")
        sys.exit(1)

if __name__ == "__main__":
    main()
