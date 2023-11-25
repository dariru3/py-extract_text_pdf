import PyPDF2

def extract_text_from_pdf(pdf_path):
    with open(pdf_path, 'rb') as file:
        reader = PyPDF2.PdfReader(file)
        text = ""
        for page_num, page in enumerate(reader.pages, start=1):
            text += f"PAGE {page_num}\n"
            text += page.extract_text()
            text += "\n----------------------------------------\n"
        return text

def save_text_to_file(text, output_path):
    with open(output_path, 'w', encoding='utf-8') as file:
        file.write(text)

file_path = "input_files/SR21_J_All.pdf"
# Replace 'your_pdf_file.pdf' with the path to your PDF file
pdf_text = extract_text_from_pdf(file_path)

# Save the extracted text to a text file
save_text_to_file(pdf_text, 'output_text_file.txt')
