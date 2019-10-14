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
            if len(key) ==3:
                f.writelines(key + '\t{:.3e}\n'.format(file[key]))
    f.close()

def createProbDic():
    # character3_count/ gram3_probability
    probability_dic = {}
    # character2_count
    character2_dic = {}
    char_list = [chr(i) for i in range(97, 123)]
    char_list.extend(['0', ' ', '.', '#'])
    for first_char in char_list:
        for second_char in char_list:
            for third_char in char_list:
                probability_dic[first_char+second_char+third_char] = 0
                character2_dic[first_char+second_char] = 0
                if first_char == '#':
                    if third_char == '#':
                        probability_dic.pop(first_char+second_char+third_char)
                else:
                    if second_char == '#':
                        probability_dic.pop(first_char+second_char+third_char)
                        character2_dic.pop(first_char+second_char)

    return probability_dic, character2_dic

def characterCounter(token, smoothing_dic, character2_dic):
    '''
    count character3 and character2
    :param token: tokens in input
    :param smoothing_dic: (dic)all possible combinations in character3
    :param character2_dic: (dic)all possible combinations in character2
    :return:
    '''
    gram3_dic = {}
    for sentence in token:
        for i in range(len(sentence) - 2):
            smoothing_dic[sentence[i:(i+3)]] += 1
            if sentence[i:(i+3)] not in gram3_dic.keys():
                gram3_dic[sentence[i:(i+3)]] = 1
            else:
                gram3_dic[sentence[i:(i+3)]] += 1
        for i in range(len(sentence) - 1):
            character2_dic[sentence[i:(i+2)]] += 1
            if sentence[i:(i+2)] not in gram3_dic.keys():
                gram3_dic[sentence[i:(i+2)]] = 1
            else:
                gram3_dic[sentence[i:(i+2)]] += 1

    return gram3_dic, smoothing_dic, character2_dic

def estimate_3gram(ch_dic):
    gram3_prob_dic = {}
    for key in ch_dic.keys():
        if len(key) == 3:
           probability = ch_dic[key]/ch_dic[key[0:2]]
           gram3_prob_dic[key] = probability

    return gram3_prob_dic

def Smoothing(smoothing_dic, character2_dic):
    alpha_value = 0.01
    # length_cnt = [len(sentence) for sentence in tokens]
    # total = sum(length_cnt)
    for key in smoothing_dic.keys():
        smoothing_dic[key] = (smoothing_dic[key] + alpha_value) / (smoothing_dic[key[0:2]] + character2_dic[key[0:2]]*alpha_value)
            
    return smoothing_dic



start_time = time.clock()
smoothing_dic, character2_dic = createProbDic()
# languahe_list = ['de', 'en', 'es']
languahe_list = ['de', 'en']
for language in languahe_list:
    # input file path
    de_path = '../task1/' + language + '_output'
    # output file path
    de_prob_path = './' + language + '_prob_output'
    # tokens in input file
    tokens = np.array(fileReader(de_path)).flatten()

    gram3_count_dic, smoothing_count_dic, character2_dic = characterCounter(tokens, smoothing_dic, character2_dic)
    gram3_prob_dic = estimate_3gram(gram3_count_dic)
    smooth_prob_dic = Smoothing(smoothing_count_dic, character2_dic)
    fileWriter(smooth_prob_dic, de_prob_path)

last_time = time.clock() - start_time
print('procedure time:', last_time)