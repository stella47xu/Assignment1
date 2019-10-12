import re
import math
from collections import Counter
from task1.task1 import fileReader
import numpy as np
import time
import random

def fileWriter(file, path):
    '''
    write files
    :param file:
    :param path:
    :return:
    '''
    with open(path, 'w', encoding='utf-8') as f:
        for key in file.keys():
            f.writelines(key+'\n')
    f.close()

def characterTransform(content):
    character3_list = []
    token_list = [('  '+word) for word in content]
    for word in token_list:
        for idx in range(len(word)-2):
            character3_list.append(word[idx:(idx+3)])
    return token_list, character3_list

def characterCounter(token_list, character3_list):
    count_dic = {}
    for character3 in character3_list:
        character2_count = 0
        for character3_new in token_list:
            if character3_new.find(character3[0:2]) > -1:
                character2_count += 1
        count_dic[character3] = [character3_list.count(character3) , character2_count]
    return count_dic

def estimate_3gram(count_dic):
    probability_dic = {}
    for key in count_dic.keys():
        probability = count_dic[key][0]/count_dic[key][1]
        probability_dic[key.strip()] = probability
    return probability_dic

def Smoothing(count_dic,tokens, AlphaValue = 0.1):
    prob_dic = {}
    total=0
    for sentence in tokens:
        for i in sentence:
            total += 1
    for key,value in count_dic.items():
        prob_dic[key] = (value[0] + AlphaValue) / (value[1] + total*AlphaValue)
    return prob_dic



de_path = '../task1/en_output'
tokens = np.array(fileReader(de_path)).flatten()
token_list, character3_list = characterTransform(tokens)
count_dic = characterCounter(token_list, character3_list)
probability_dic = estimate_3gram(count_dic)
smoothing_dic = Smoothing(count_dic,0.2,tokens)
print(smoothing_dic)
