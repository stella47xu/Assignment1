from task1.task1 import fileReader
import numpy as np
import time

def fileWriter(file, path):
    '''
    write files
    :param file:
    :param path:
    :return:
    '''
    with open(path, 'w', encoding='utf-8') as f:
        for key in sorted(file.keys()):
            f.writelines(key + '\t{:.3e}\n'.format(file[key]))
    f.close()

# def characterTransform(content):
#     character3_list = []
#     for sentence in content:
#         for idx in range(len(sentence)-2):
#             character3_list.append(sentence[idx:(idx+3)])
#     return token_list, character3_list

def characterCounter(token):
    character_dic = {}
    for sentence in token:
        for i in range(len(sentence) - 2):
            if sentence[i:(i+3)] not in character_dic.keys():
                character_dic[sentence[i:(i+3)]] = 1
            else:
                character_dic[sentence[i:(i+3)]] += 1
        for i in range(len(sentence) - 1):
            if sentence[i:(i+2)] not in character_dic.keys():
                character_dic[sentence[i:(i+2)]] = 1
            else:
                character_dic[sentence[i:(i+2)]] += 1

    return character_dic

def estimate_3gram(ch_dic):
    probability_dic = {}
    for key in ch_dic.keys():
        if len(key) == 3:
           probability = ch_dic[key]/ch_dic[key[0:2]]
           probability_dic[key] = probability

    return probability_dic

def Smoothing(ch_dic,tokens):
    alpha_value = 0.01
    smooth_prob_dic = {}
    total = 0
    length_cnt = [len(sentence) for sentence in tokens]
    total = sum(length_cnt)
    for key in ch_dic.keys():
        if len(key) ==3:
           smooth_prob_dic[key] = (ch_dic[key] + alpha_value) / (ch_dic[key[0:2]] + total*alpha_value)

    return smooth_prob_dic



start_time = time.clock()
de_path = '../task1/de_output'
de_prob_path = './de_prob_output'
tokens = np.array(fileReader(de_path)).flatten()

character_dic = characterCounter(tokens)
probability_dic = estimate_3gram(character_dic)
smooth_prob_dic = Smoothing(character_dic, tokens)
fileWriter(smooth_prob_dic, de_prob_path)

last_time = time.clock() - start_time
print('procedure time:', last_time)