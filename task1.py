import re
import string
def fileReader(path):
    content = []
    with open(path, 'r', encoding='utf-8') as f:
        for line in f.readlines():
            content.append(line)

    return content

def preprocess_line(content):
    new_content = []
    for lines in content:
        lines = lines.lower()
        rstr= r"[^0-9a-z\.]"
        newlines = re.sub(rstr," ",lines)
        new_content.append(newlines)
    return new_content

print(preprocess_line(fileReader("training.de")))
