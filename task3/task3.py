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

# def characterTransform(content):
#     character3_list = []
#     for sentence in content:
#         for idx in range(len(sentence)-2):
#             character3_list.append(sentence[idx:(idx+3)])
#     return token_list, character3_list

def characterCounter(token):
    character3_dic = {}
    character2_dic = {}
    count_character3 = 0
    count_character2 = 0
    for sentence in token:

        for i in range(len(sentence)-2):
            character3_dic[sentence[i] + sentence[i + 1] + sentence[i + 2]] = count_character3
            if sentence.find(sentence[i]+sentence[i+1]+sentence[i+2]) >-1:
               count_character3 += 1
        for i in range(len(sentence)-1):
            character2_dic[sentence[i] + sentence[i + 1]] = count_character2
            if sentence.find(sentence[i]+sentence[i+1]) > -1:
                count_character2 +=1
    return character2_dic , character3_dic

def estimate_3gram(ch2_dic,ch3_dic):
    probability_dic = {}
    for key in ch3_dic.keys():
        probability = ch3_dic[key]/ch2_dic[key[0]+key[1]]
        probability_dic[key.strip()] = probability
    return probability_dic
# def Smoothing(count_dic,tokens, AlphaValue = 0.1):
#     prob_dic = {}
#     total=0
#     for sentence in tokens:
#         for i in sentence:
#             total += 1
#     for key,value in count_dic.items():
#         prob_dic[key] = (value[0] + AlphaValue) / (value[1] + total*AlphaValue)
#     return prob_dic



de_path = '../task1/de_output'
tokens = np.array(fileReader(de_path)).flatten()
character2_dic,character3_dic = characterCounter(tokens)
probability_dic = estimate_3gram(character2_dic,character3_dic)
# smoothing_dic = Smoothing(count_dic,0.2,tokens)
print(probability_dic)