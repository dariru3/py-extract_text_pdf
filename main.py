import PyPDF2
import re
import os
from config import config

def extract_text_from_pdf(pdf_path):
    with open(pdf_path, 'rb') as file:
        reader = PyPDF2.PdfReader(file)
        text = ""
        for page_num, page in enumerate(reader.pages, start=1):
            text += f"PAGE {page_num}\n"
            text += page.extract_text()
            text += "\n----------------------------------------\n"
        return text

def clean_japanese_text(text):
    # Regular expression pattern to identify and remove spaces between Japanese characters
    japanese_char_pattern = r'(?<=[\u3000-\u303f\u3040-\u309f\u30a0-\u30ff\u3400-\u4dbf\u4e00-\u9fff]) ' \
                            r'(?=[\u3000-\u303f\u3040-\u309f\u30a0-\u30ff\u3400-\u4dbf\u4e00-\u9fff])'
    return re.sub(japanese_char_pattern, '', text)

def save_text_to_file(text, pdf_path):
    base_name = os.path.splitext(os.path.basename(pdf_path))[0]
    output_path = f'{base_name}_output_text.txt'
    with open(output_path, 'w', encoding='utf-8') as file:
        file.write(text)

if __name__ == '__main__':
    file_path = config["filepath"]
    extracted_text = extract_text_from_pdf(file_path)
    cleaned_text = clean_japanese_text(extracted_text)
    save_text_to_file(cleaned_text, file_path)