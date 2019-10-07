import re

def fileReader(path):
    content = []
    with open(path, 'r', encoding='utf-8') as f:
        for line in f.readlines():
            content.append(line)

    f.close()
    return content

# def preprocess_line(content):
#     content = re.match('//')
print(fileReader(".//training.en"))