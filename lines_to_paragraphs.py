def process_text_file(filepath):
    with open(filepath, 'r', encoding='utf-8') as file:
        lines = file.readlines()
    
    # This will store the processed text
    processed_text = []
    paragraph = []

    # Process each line in the file
    for line in lines:
        # Strip any whitespace from the beginning and end of the line
        stripped_line = line.strip()
        if stripped_line:
            # If the line contains text, add it to the current paragraph
            paragraph.append(stripped_line)
        elif paragraph:
            # If the line is empty and there is a paragraph collected, join it and add to results
            processed_text.append(''.join(paragraph)) # use ' '.join to add a space bewteen sentences
            # processed_text.append('')  # Add a blank line to separate paragraphs
            paragraph = []  # Reset the current paragraph

    # If there's any remaining text in the paragraph list, add it as a paragraph
    if paragraph:
        processed_text.append(' '.join(paragraph))

    # Write the processed text back to the file
    with open(filepath, 'w', encoding='utf-8') as file:
        file.write('\n'.join(processed_text))

# Specify the path to your file
file_path = 'environment.txt'
# Process the text file
process_text_file(file_path)

print("The file has been updated.")
