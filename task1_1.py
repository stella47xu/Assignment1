import re

def fileReader(path):
    content = []
    with open(path, 'r', encoding='utf-8') as f:
        for line in f.readlines(path):
            content.extend(line)

    f.close()
    return content

def preprocess_line(content):
    content = re.match('//')