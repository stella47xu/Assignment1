'''
    generate the 1st, 2nd and 3rd characters randomly
    generate the later character with the highest probability in model
'''
import re
import time

def fileReader(path):
    '''
    read files
    :param path: file path
    :return: list for file content
    '''
    content = []
    with open(path, 'r', encoding='utf-8') as f:
        # read data of files line by line
        for line in f.readlines():
            model_line = re.split('[\t\n]', line)
            content.append(model_line)

    return content

def fileWriter(file, path):
    '''
    write files
    :param file: files to be writen
    :param path: file path
    :return: None
    '''
    with open(path, 'w', encoding='utf-8') as f:
        for line in file.split('#'):
            # write output without '#'
            f.writelines(line)

    f.close()

def generate_from_LM(model, n):
    '''
    generate sequences based on model
    :param model:  language model
    :param n: the length of output
    :return: output sequence
    '''
    # sentences start with '##'
    generate_str = '##'
    char_length = 0
    while char_length < n:
        max_prob = .0
        max_str = ''
        for character_3 in model:
            # find the combination whose the 1st and 2nd character are same with the last two characters of generate_str
            if character_3[0][0:2] == generate_str[-2:]:
                # find the character with the highest probability based on model
                if float(character_3[1]) > max_prob:
                    max_str = character_3[0]
                    max_prob = float(character_3[1])

        if not max_str:
            # when the sentences end up with '#', generate a new sentence
            generate_str += '\n##'
            # if a sentence ends, char_length equals char_length minus 1('#')
            char_length -= 1
        else:
            # else: add the character into generate_str
            generate_str += max_str[2]
            char_length += 1

    return generate_str


start_time = time.clock()
model_path_list = ['../data/model-br.en', '../task3/en_prob_output']
model_writer_path_list = ['./model-br_max_output', './training_max_output']
str_length = 300
for i in range(len(model_path_list)):
    model = fileReader(model_path_list[i])
    generate_str = generate_from_LM(model, str_length)
    fileWriter(generate_str, model_writer_path_list[i])

last_time = time.clock() - start_time
print('procedure time:', last_time)