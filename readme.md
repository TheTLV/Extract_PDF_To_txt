# PDF to Text Converter with Docling

This script converts a PDF file into Markdown text using the Docling library.

## Requirements

Ensure you have the required dependencies installed:

```bash
pip install docling
```

## Usage

1. Place the source PDF file in the same directory as the script.
2. Update the `name` variable with the PDF file name (excluding `.pdf`).
3. Run the script:

```bash
python pdftotxt.py
```

## How It Works

- **Text Extraction**: Uses `DocumentConverter` from Docling to extract text from a PDF.
- **Output**:
  - Prints the extracted text in Markdown format.
  - Prints document tokens for further processing.
  - Saves the extracted text as a `.txt` file.

## Output Files

- `<your_file_name>.txt`: Contains the extracted text in Markdown format.

## Notes

- Ensure the PDF has selectable text for better conversion results.

## License

This project is licensed under the MIT License.

