import re
import string

def fileReader(path):
    '''
    read files
    :param path:
    :return:
    '''
    content = []
    with open(path, 'r', encoding='utf-8') as f:
        # read data of files line by line
        for line in f.readlines():
            content.append(line)

    return content

def preprocess_line(content):
    '''
    preprocess each line of files:
    lowercase all characters;
    convert all digits to 0;
    remove characters that are not digits, space, '.' or are not in alphabet
    :param content:
    :return:
    '''
    new_content = []
    for lines in content:
        # convert all characters into lowercase
        lines = lines.lower()
        # replace all characters to be removed by space
        rstr= r"[^0-9a-z\.\s]"
        newlines = re.sub(rstr,'',lines)
        # convert all digits to 0
        digit_rstr = r'[0-9]+'
        newlines = re.sub(digit_rstr,'0',newlines)
        new_content.append(newlines)
    return new_content

f_path = "test"
print(preprocess_line(fileReader(f_path)))