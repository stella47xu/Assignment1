import numpy as np
import task1

def trigram(stems, word3_id, counter):
    count_length = len(counter)
    trigram0 = np.zeros(count_length)
    trigram1 = np.zeros((count_length, count_length))
    trigram2 = np.zeros((count_length, count_length, count_length))
    for sentence in stems:
        sentence = [word3_id[w] for w in sentence]

