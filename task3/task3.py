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
    for sentence in token:
        for i in range(len(sentence) - 2):
            if character3_dic.__contains__(sentence[i] + sentence[i + 1] + sentence[i + 2]) == False:
                character3_dic[sentence[i] + sentence[i + 1] + sentence[i + 2]] = 1
            else:
                character3_dic[sentence[i] + sentence[i + 1] + sentence[i + 2]] += 1
        for i in range(len(sentence) - 1):
            if character2_dic.__contains__(sentence[i] + sentence[i + 1]) == False:
                character2_dic[sentence[i] + sentence[i + 1]] = 1
            else:
                character2_dic[sentence[i] + sentence[i + 1]] += 1

    return character3_dic , character2_dic

def estimate_3gram(ch3_dic,ch2_dic):
    probability_dic = {}
    for key in ch3_dic.keys():
        probability = ch3_dic[key]/ch2_dic[key[0]+key[1]]
        probability_dic[key] = probability
    return probability_dic
def Smoothing(ch3_dic,ch2_dic,tokens):
    alpha_value = 0.01
    smooth_prob_dic = {}
    total = 0
    for sentence in tokens:
        for i in sentence:
            total += 1
    for key in ch3_dic.keys():
        smooth_prob_dic[key] = (ch3_dic[key]+ alpha_value) / (ch2_dic[key[0]+key[1]] + total*alpha_value)
    return smooth_prob_dic



de_path = '../task1/de_output'
tokens = np.array(fileReader(de_path)).flatten()
character3_dic,character2_dic = characterCounter(tokens)
probability_dic = estimate_3gram(character3_dic,character2_dic)
smooth_prob_dic = Smoothing(character3_dic,character2_dic,tokens)
print(probability_dic)
print(smooth_prob_dic)