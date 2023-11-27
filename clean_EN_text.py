import re
import os

remove_specific_lines = [
    r"NISSAN MOTOR CORPORATION SUSTAINABILITY REPORT 2021\d*Contents",
    r"EnvironmentalCEO Message",
    r"SocialCSO Message",
    r"GovernanceCarbon Neutrality/ \nResponse to COVID-19",
    r"ESG DataChair of the Board of \nDirectors Message",
    r"Editorial PolicySustainability at Nissan",
    r"TCFD Content IndexNissan's Contribution \nto the SDGsThe Alliance",
    r"GRI Content IndexQuick Guide For \nInvestors"
]

def remove_lines(text, lines):
    for line in lines:
        pattern = re.escape(line) + r"\n?"
        text = re.sub(line, '', text)

    text = re.sub(r'\n{2,}','\n', text)
    return text

def read_text_from_file(file_path):
    with open(file_path, 'r', encoding='utf-8') as file:
        return file.read()

def is_header(line):
    # Check if the line is fully uppercase (might be a header)
    if line.isupper():
        return True
    # Check if the line is in nuanced title case
    elif is_title_case(line):
        return True
    return False

def is_title_case(line):
    lowercase_words = ['at', 'the', 'and', 'in', 'on', 'for', 'with', 'a', 'an', 'of', 'to']
    words = line.split()
    if not words:
        return False

    if not words[0].istitle():
        return False

    for word in words[1:]:
        if word.lower() in lowercase_words:
            if not word.islower():
                return False
        elif not word.istitle():
            return False

    return True

def clean_text(text):
    text = remove_lines(text, remove_specific_lines)
    lines = text.split('\n')
    cleaned_lines = []
    for line in lines:
        if is_header(line):
            cleaned_lines.append(line + '\n')
        else:
            if line.strip():
                cleaned_lines.append(line.strip() + ' ')
            else:
                cleaned_lines.append('\n')
    cleaned_text = ''.join(cleaned_lines)
    cleaned_text = re.sub(r' +', ' ', cleaned_text)
    return cleaned_text

def save_text_to_file(text, output_path):
    with open(output_path, 'w', encoding='utf-8') as file:
        file.write(text)

if __name__ == '__main__':
    input_file = 'SR21_E_All_output_text.txt'  # Update this path to your text file
    output_file = 'cleaned_output_text.txt'

    extracted_text = read_text_from_file(input_file)
    cleaned_text = clean_text(extracted_text)
    save_text_to_file(cleaned_text, output_file)
