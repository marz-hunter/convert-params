# Convert Parameters Script

This Python script processes a list of parameters from a file and converts them into various formats (JSON, POST HTML, GET HTML) with options for limiting the number of parameters per output file and specifying output directories.

---

## Features

1. Converts parameters into:
   - JSON format (e.g., `{"email": "emailnull'"}`).
   - POST HTML format (e.g., `email=emailnull'&type=typenull'`).
   - GET HTML format (e.g., `email=null&type=null`).
2. Allows limiting the number of parameters per output file.
3. Creates the necessary output directories if they do not exist.
4. Handles errors gracefully, such as missing files or invalid inputs.

---

## Requirements

- Python 3.x

---

## Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/marz-hunter/convert-params.git
   cd convert-params
   ```

2. Ensure the required file (`params.txt`) is in the project directory.

---

## Usage

Run the script using the following command:

```bash
python3 convert.py -f <file_path> -limit <number> -of <output_folder>
```

### Arguments

| Argument        | Description                                                       |
|-----------------|-------------------------------------------------------------------|
| `-f`            | Path to the file containing parameters.                          |
| `-limit`        | Number of parameters per output file.                            |
| `-of`           | Output folder and mode. Options: `paramjson`, `paramhtml`, `paramgethtml`. |

### Examples

#### Convert to JSON
```bash
python3 convert.py -f params.txt -limit 200 -of paramjson
```
- Input: `params.txt`
- Output: Files in the `paramjson` folder, e.g., `1.json`, `2.json`.

#### Convert to POST HTML
```bash
python3 convert.py -f params.txt -limit 200 -of paramhtml
```
- Input: `params.txt`
- Output: Files in the `paramhtml` folder, e.g., `1.txt`, `2.txt`.

#### Convert to GET HTML
```bash
python3 convert.py -f params.txt -limit 200 -of paramgethtml
```
- Input: `params.txt`
- Output: Files in the `paramgethtml` folder, e.g., `1.txt`, `2.txt`.

---

## Error Handling

1. **File Not Found**:
   - If the parameter file does not exist, the script will display an error message.
2. **Empty File**:
   - If the parameter file is empty, the script will terminate with a descriptive error.
3. **Invalid Output Directory**:
   - The script will attempt to create the output directory if it does not exist.
4. **JSON/HTML Generation Errors**:
   - The script will handle and display any errors during file generation.

---

## License

This project is licensed under the MIT License. See the LICENSE file for details.

---
