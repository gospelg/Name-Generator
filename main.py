from __future__ import division
import numpy as np
import os

def generate_word(learning_list, commit):
    probability = {} #frequency of patterns
    total = 0 # total to divide by and find probability
    for word in learning_list:
        if word[1].lower() not in probability:
            probability[word[1].lower()] = 1
            total += 1
        else:
            probability[word[1].lower()] += 1
            total += 1
    for x in probability:
        if probability[x] != 0:
            probability[x] /= total
        else:
            pass
    print probability
    
def main():
    working_dir = os.path.dirname(os.path.abspath( __file__ ))
    file_path = raw_input('Which culture do you wish to generate names from? \nPlease type the name exactly.\n')
    with open(file_path, 'r') as f:
        language = f.readlines()
    generate_word(language, '')
    #test(language)
    
    
main()
