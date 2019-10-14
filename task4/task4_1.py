import re
import random
import time

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
            content.append(re.split('[\t\n]', line))

    return content

def generate_from_LM(model, n):
    first_index = random.randint(0, len(model)-1)
    generate_str = model[first_index][0]
    for _ in range(n-2):
        max_str = ''
        max_prob = .0
        for character_3 in model:
            if character_3[0][0:2] == generate_str[-2:]:
                if float(character_3[1]) > max_prob:
                    max_str = character_3[0]
                    max_prob = float(character_3[1])

        generate_str += max_str[2]

    return generate_str


start_time = time.clock()
model_path_list = ['../data/model-br.en', '../task3/en_prob_output']
str_length = 300
for model_path in model_path_list:
    model = fileReader(model_path)
    generate_str = generate_from_LM(model, str_length)
    print(generate_str)

last_time = time.clock() - start_time
print('procedure time:', last_time)