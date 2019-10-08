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
        rstr = r" "
        newlines = re.sub(rstr,"_", lines)
        new_content.append(newlines)
    return new_content

print(preprocess_line(fileReader("training.de")))

