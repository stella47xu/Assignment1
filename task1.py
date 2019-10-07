# def readfile(path):
#     text=[]
#     with open (path,'r',encoding='utf-8') as f:
#         for lines in f.readlines(path):
#             text.extend(lines)
#     f.close()
#     return text

import re

def fileReader(path):
    content = []
    with open(path, 'r', encoding='utf-8') as f:
        for line in f.readlines(path):
            content.extend(line)

    f.close()
    return content
#
# def preprocess_line(content):
#     content = re.match('//')

print(fileReader("C:\Users\xu47s\PycharmProjects\Assignment1\training.de"))