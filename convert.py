import argparse
import json
import os
from pathlib import Path

def load_params(file_path):
    try:
        with open(file_path, 'r') as f:
            params = [line.strip() for line in f if line.strip()]
        if not params:
            raise ValueError("File parameter kosong atau tidak berisi parameter valid.")
        return params
    except FileNotFoundError:
        raise FileNotFoundError(f"File '{file_path}' tidak ditemukan.")
    except Exception as e:
        raise RuntimeError(f"Kesalahan saat membaca file: {e}")

def create_directory(output_folder):
    try:
        Path(output_folder).mkdir(parents=True, exist_ok=True)
    except Exception as e:
        raise RuntimeError(f"Kesalahan saat membuat direktori '{output_folder}': {e}")

def save_to_file(output_folder, index, content):
    ext = 'json' if output_folder == 'paramjson' else 'txt'
    file_path = f"{output_folder}/{index}.{ext}"
    try:
        with open(file_path, 'w') as f:
            f.write(content)
        print(f"[INFO] File berhasil disimpan: {file_path}")
    except Exception as e:
        print(f"[ERROR] Gagal menyimpan file '{file_path}': {e}")
        raise

def generate_postjson(params, limit, output_folder):
    for i in range(0, len(params), limit):
        chunk = params[i:i + limit]
        try:
            json_obj = {param: f"{param}null'" for param in chunk}
            save_to_file(output_folder, i // limit + 1, json.dumps(json_obj))
        except json.JSONDecodeError as e:
            print(f"[ERROR] Kesalahan saat membuat JSON: {e}")
            raise

def generate_posthtml(params, limit, output_folder):
    for i in range(0, len(params), limit):
        chunk = params[i:i + limit]
        html_data = "&".join(f"{param}={param}null'" for param in chunk)
        save_to_file(output_folder, i // limit + 1, html_data)

def generate_gethtml(params, limit, output_folder):
    for i in range(0, len(params), limit):
        chunk = params[i:i + limit]
        html_data = "&".join(f"{param}=null" for param in chunk)
        save_to_file(output_folder, i // limit + 1, html_data)

def main():
    parser = argparse.ArgumentParser(description="Convert parameter file to JSON or HTML formats.")
    parser.add_argument("-f", "--file", required=True, help="Path to the parameter file.")
    parser.add_argument("-of", "--output_folder", required=True, choices=["paramjson", "paramhtml", "paramgethtml"], help="Output folder and mode.")
    parser.add_argument("-limit", type=int, required=True, help="Number of parameters per output file.")

    args = parser.parse_args()

    try:
        params = load_params(args.file)
        create_directory(args.output_folder)

        if args.output_folder == "paramjson":
            generate_postjson(params, args.limit, args.output_folder)
        elif args.output_folder == "paramhtml":
            generate_posthtml(params, args.limit, args.output_folder)
        elif args.output_folder == "paramgethtml":
            generate_gethtml(params, args.limit, args.output_folder)

    except Exception as e:
        print(f"[ERROR] {e}")

if __name__ == "__main__":
    main()
