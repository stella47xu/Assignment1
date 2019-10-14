import re
import time
import random

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
            model_line = re.split('[\t\n]', line)
            content.append(model_line[0])

    return content

def fileWriter(file, path):
    '''
    write files
    :param file:
    :param path:
    :return:
    '''
    with open(path, 'w', encoding='utf-8') as f:
        for line in file:
            f.writelines(line)
    f.close()

def generate_from_LM(model, n):
    generate_str = '##'
    for i in range(n-2):
        next_list = []
        for character_3 in model:
            if character_3[0:2] == generate_str[-2:]:
                next_list.append(character_3)

        if not next_list:
            generate_str += '\n##'
        else:
            next_index = random.randint(0, len(next_list)-1)
            generate_str += next_list[next_index][2]

    return generate_str


start_time = time.clock()
model_path_list = ['../data/model-br.en', '../task3/en_prob_output']
model_writer_path_list = ['./model-br_random_output', './training_random_output']
str_length = 300
for i in range(len(model_path_list)):
    model = fileReader(model_path_list[i])
    generate_str = generate_from_LM(model, str_length)
    fileWriter(generate_str, model_writer_path_list[i])

last_time = time.clock() - start_time
print('procedure time:', last_time)