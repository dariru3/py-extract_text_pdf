# PDF Text Extractor and Cleaner

## Overview
This Python script is designed to extract text from PDF files, specifically targeting documents with Japanese content. It handles the extraction of text from each page, formats it with page numbers, cleans the text by removing unnecessary spaces between Japanese characters, and saves the output to a text file named after the original PDF.

## Requirements
- Python 3.x
- PyPDF2
- Other dependencies listed in `requirements.txt`

## Usage
To run the script, use the following command:
```sh
python main.py
```

This will process the PDF file specified in the `config.py` file. The script will:
- Extract text from the PDF.
- Clean the text by removing unnecessary spaces, particularly between Japanese characters.
- Save the cleaned text to a new file named `[original_pdf_name]_output_text.txt`.