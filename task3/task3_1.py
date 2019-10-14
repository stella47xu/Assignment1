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
            if len(key) == 3:
                f.writelines(key + '\t{:.3e}\n'.format(file[key]))
    f.close()

def createProbDic():
    probability_dic = {}
    char_list = [chr(i) for i in range(97, 123)]
    char_list.extend(['0', ' ', '.', '#'])
    for first_char in char_list:
        for second_char in char_list:
            for third_char in char_list:
                probability_dic[first_char+second_char+third_char] = 0
                probability_dic[first_char+second_char] = 0
                if first_char == '#':
                    if third_char == '#':
                        probability_dic.pop(first_char+second_char+third_char)
                else:
                    if second_char == '#':
                        probability_dic.pop(first_char+second_char+third_char)

    return probability_dic

def characterCounter(token, smoothing_dic):
    gram3_dic = {}
    for sentence in token:
        for i in range(len(sentence) - 2):
            # print(sentence[i:(i+3)])
            smoothing_dic[sentence[i:(i+3)]] += 1
            if sentence[i:(i+3)] not in gram3_dic.keys():
                gram3_dic[sentence[i:(i+3)]] = 1
            else:
                gram3_dic[sentence[i:(i+3)]] += 1
        for i in range(len(sentence) - 1):
            smoothing_dic[sentence[i:(i+2)]] += 1
            if sentence[i:(i+2)] not in gram3_dic.keys():
                gram3_dic[sentence[i:(i+2)]] = 1
            else:
                gram3_dic[sentence[i:(i+2)]] += 1

    return gram3_dic, smoothing_dic

def estimate_3gram(ch_dic):
    gram3_prob_dic = {}
    for key in ch_dic.keys():
        if len(key) == 3:
           probability = ch_dic[key]/ch_dic[key[0:2]]
           gram3_prob_dic[key] = probability

    return gram3_prob_dic

def Smoothing(smoothing_dic, tokens):
    alpha_value = 0.01

    for key in smoothing_dic.keys():
        if len(key) == 3:
            smoothing_dic[key] = (smoothing_dic[key] + alpha_value) / (smoothing_dic[key[0:2]] + len(smoothing_dic)*alpha_value)

    return smoothing_dic



start_time = time.clock()
smoothing_dic = createProbDic()
# languahe_list = ['de', 'en', 'es']
languahe_list = ['de', 'en']
for language in languahe_list:
    de_path = '../task1/' + language + '_output'
    de_prob_path = './' + language + '_prob_output'
    tokens = np.array(fileReader(de_path)).flatten()

    gram3_count_dic, smoothing_count_dic = characterCounter(tokens, smoothing_dic)
    gram3_prob_dic = estimate_3gram(gram3_count_dic)
    smooth_prob_dic = Smoothing(smoothing_count_dic, tokens)
    fileWriter(smooth_prob_dic, de_prob_path)

last_time = time.clock() - start_time
print('procedure time:', last_time)
