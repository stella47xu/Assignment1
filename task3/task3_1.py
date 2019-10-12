import numpy as np
from task1.task1 import fileReader
import time

def characterCounter(content):
    character3_list = []
    token_list = [('  '+word) for word in content]
    for word in token_list:
        for idx in range(len(word)-2):
            character3_list.append(word[idx:(idx+3)])
    return token_list, character3_list

def estimate_3gram(token_list, character3_list):
    character3_dic = {}
    for character3 in character3_list:
        character2_count = 0
        for character3_new in token_list:
            if character3_new.find(character3[0:2]) > -1:
                character2_count += 1

        probability = character3_list.count(character3)/character2_count
        character3_dic[character3.strip()] = probability

    return character3_dic

start_time = time.clock()
de_path = '../task1/de_output'
tokens = np.array(fileReader(de_path)).flatten()
token_list, character3_list = characterCounter(tokens)
character3_dic = estimate_3gram(token_list, character3_list)

last_time = time.clock() - start_time
print('procedure time:', last_time)