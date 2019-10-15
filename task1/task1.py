import re
import time

def fileReader(path):
    '''
    read files
    :param path: file path
    :return: file content
    '''
    content = []
    with open(path, 'r', encoding='utf-8') as f:
        # read data of files line by line
        for line in f.readlines():
            content.append(line.strip())
    return content

def fileWriter(file, path):
    '''
    write files
    :param file: file content
    :param path: file path
    :return: None
    '''
    with open(path, 'w', encoding='utf-8') as f:
        for line in file:
            f.writelines(line+'\n')
    f.close()

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
        if len(lines) != 1:
            # convert all characters into lowercase
            lines = lines.lower()
            # delete all characters required to be removed
            rstr= r"[^0-9a-z\.\s]"
            newlines = re.sub(rstr, "", lines)
            # convert all digits to 0
            digit_rstr = r'[0-9]+'
            newlines = re.sub(digit_rstr, '0', newlines)
            new_content.append('##'+newlines+'#')
            # add '##' to the start of the each sentence and '#' to the end of each sentence
    return new_content


start_time = time.clock()
languahe_list = ['de', 'en', 'es']
for language in languahe_list:
    de_path = '../data/training.' + language
    de_write_path = './' + language + '_output'
    stems = preprocess_line(fileReader(de_path))
    fileWriter(stems, de_write_path)

last_time = time.clock() - start_time
print('procedure time:', last_time)