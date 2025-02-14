import re
import math
import numpy as np
from task1.task1 import preprocess_line

def fileReader(path):
    """
    read the text file
    param path: the path of the file
    return:
    a list of the content in text file
    """
    content = []
    #create an empty to store the lines of the file
    with open(path, 'r', encoding='utf-8') as f:
        # read data of files line by line
        for line in f.readlines():
            content.append(line.strip('\n'))
            # delete \n in each line
    return content

def dic_prob(prob):
    """
    store the probabilities of all possible combinations in 3 characters into a dictionary
    :param prob: the language model
    :return:
    the dictionary of probabilities of all possible combinations in 3 characters
    """
    prob_dic={}
    # create a new empty dictiontary to store the probabilities
    for i in prob:
        prob_dic[i[0:3]] =float(i[-9:])
        # take the possible combinations in 3 characters as keys, and the probabilities as values
    return prob_dic


def perplexity(content,prob_dic):
    """
    compute the perplexity of the text document under this language model
    :param content:  content of the text document
    :param prob_dic: the language model
    :return:
    the value of perplexity
    """
    pp_list=[]
    for lines in content:
        p_line = sum([math.log(prob_dic[lines[i:(i+3)]],2) for i in range(len(lines)-2)])
               # compute the probabilities of each line
        pp_line = pow(2,p_line/-len(lines))
        # compute the perplexity of each line
        pp_list.append(pp_line)
    pp = sum(pp_list)/len(pp_list)
    # compute the average perplexity
    return pp



test_path = '../data/test' # set the path of text document
model_prob = '../data/model-br.en' # set the path of the language model
en_prob = '../task3/en_prob_output'
de_prob = '../task3/de_prob_output'
es_prob = '../task3/es_prob_output'

content = preprocess_line(fileReader(test_path)) # preprocess the text model
prob_dic_model = dic_prob(fileReader(model_prob))  # create the dictionary of probabilities of all possible combinations in 3 characters
prob_dic_en = dic_prob(fileReader(en_prob))
prob_dic_de = dic_prob(fileReader(de_prob))
prob_dic_es = dic_prob(fileReader(es_prob))
print("The perplexity of text document under the 'model-br.en' model",perplexity(content,prob_dic_model))
print("The perplexity of text document under the 'en_prob_output'",perplexity(content,prob_dic_en))
print("The perplexity of text document under the 'de_prob_output'",perplexity(content,prob_dic_de))
print("The perplexity of text document under the 'es_prob_output'",perplexity(content,prob_dic_es))

'''
to create a simpe_text with the LM from Question 2.3 and
use it to compare program’s perplexity result to hand computation
simpe_text=["##abaab#"]
dic_of_simple_LM={'##a':0.2,'#aa':0.2,'#ba':0.15,'aaa':0.4,'aba':0.6,
                  'baa':0.25,'bba':0.5,'##b':0.8,'#ab':0.7,'#bb':0.75,
                  'aab':0.5,'abb':0.3,'bab':0.65,'bbb':0.4,'###':0.0,
                  '#a#':0.1,'#b#':0.1,'aa#':0.1,'ab#':0.1,'ba#':0.1,
                  'bb#':0.1}
print(perplexity(simpe_text,dic_of_simple_LM))
----the output is 2.3569552537168756 which equals to the hand computation
'''