import re

# Open the input file for reading
with open('1a_Georgia.txt', 'r') as f:
    text = f.read()

# Define the regex pattern to match the specified pattern 
pattern = r'^(\S+\s+-\s+\S+)\n((?:\s{2,}.+\n)+)'

# Find all matches in the text
matches = re.findall(pattern, text, re.MULTILINE)

# Loop through the matches and convert them to markdown subheadings and indented text blocks for match in matches:
# Get the subheading text (strip leading/trailing spaces)
for match in matches:
    subheading_text = match[0].strip()
    # Replace the original text with the markdown subheading and indented text block
    new_text = f'{subheading_text}\n\n'
    indented_text = match[1].strip().replace('\n', '\n  ')
    new_text += f'  {indented_text}\n\n'
    text = text.replace(match[0] + '\n' + match[1], new_text)

# Define the regex pattern to match strings with "CGPS" in front 
pattern = r'CGPS\s+\S+'

# Find all matches in the text
matches = re.findall(pattern, text)

# Loop through the matches and convert them to markdown hyperlinks for match in matches:
# Remove the "CGPS" prefix and any leading/trailing spaces
for match in matches:
    link_text = match[5:].strip()
    # Create the markdown hyperlink
    markdown_link = f'[{link_text}]({match})'
    # Replace the original text with the markdown hyperlink
    text = text.replace(match, markdown_link)


# Write the output to a new file
with open('1a_Georgia.txt', 'w') as f:
    f.write(text)