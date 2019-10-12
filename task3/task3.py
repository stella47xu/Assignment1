import re
from collections import Counter
from task1.task1_1 import fileReader
import time
def Preprocessing(content):
    '''

    :param file:
    :return:
    '''
    newlines=[]
    for lines in content:
        lines=lines.strip()
        newlines.append(lines)
    return newlines

def flatten(sentence):
    '''
    Convert to 1-D list
    :param sentence:
    :return:
    '''
    new_list=[]
    for line in sentence:
        new_line=re.split(r' ',line)
        for i in new_line:
           new_list.append(i)
    return new_list

def count(word_list):
    for words in word_list:
        for character in words:
            count()




print(count(flatten(Preprocessing(fileReader('../task1/en_output')))))

