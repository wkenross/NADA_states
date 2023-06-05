import re

# define regex pattern to match URLs
url_regex = re.compile(r"(https?\S+)")

# read in input file
with open("1a_Georgia.txt", "r") as input_file:
    input_text = input_file.read()

# find all URLs in input text
urls = re.findall(url_regex, input_text)

# create markdown links for each URL
for url in urls:
# check if URL is already in markdown format 
    if "(" in url and ")" in url and "[" in url and "]" in url:
        continue
    else:
        hyperlink = f"[{url}]({url})"
        # replace URL with markdown hyperlink in input text 
        input_text = input_text.replace(url, hyperlink)

# write updated text to output file
with open("1a_Georgia.md", "w") as output_file:
    output_file.write(input_text)
