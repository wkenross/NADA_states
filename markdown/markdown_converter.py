import re

# Open the input file for reading
with open('1a_Georgia.txt', 'r') as f:
    text = f.read()

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
    
