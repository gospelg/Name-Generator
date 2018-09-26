from __future__ import division
import numpy as np
import os

def generate(learning_list, commit, newline_bias):
    #print "this is what has been commited so far"
    #print commit
    probability = {} #frequency of patterns
    total = 0 # total to divide by and find probability
    if len(commit) == 0:
        for word in learning_list:
            if word[0].lower() not in probability:
                probability[word[0].lower()] = 1
                total += 1
            else:
                probability[word[0].lower()] += 1
                total += 1
    else:
        for word in learning_list:
            if commit in word:
                position = word.index(commit)
                next_char = word[position + len(commit)]
                if next_char not in probability:
                    probability[next_char] = 1
                    total += 1
                else:
                    probability[next_char] += 1
                    total += 1

    for x in probability:
        if probability[x] != 0:
            probability[x] /= total
        else:
            pass
    #add newline_bias if \n is a possibility
    if '\n' in probability:
        adjustment = newline_bias / len(probability)
        for x in probability:
            if probability[x] - adjustment < 0:
                probability[x] = 0
            else:    
                probability[x] -= adjustment        
        round = (1 - sum(probability.itervalues()) - newline_bias)
        probability['\n'] += (round + newline_bias)
        print probability
    #separate dictionary keys and values into two corresponding lists
    clean_data = [[],[]]
    for x,y in probability.items():
         clean_data[0].append(x)
         clean_data[1].append(y)
    #choose letter
    
    x = np.random.choice(clean_data[0], p=clean_data[1])
    if x != '\n':
        print "Recursing"
        generate(learning_list, commit + x, (newline_bias + .10))
    elif x == '\n':
        return commit
    else:
        print 'math error, dumping data'
        print probability
        print clean_data
        exit()
    

def run_loop(language):
    operation = raw_input('Run?\n')
    if operation == 'y':
        generate(language, '', 0)
        run_loop(language)
    else:
        exit()

def main():
    working_dir = os.path.dirname(os.path.abspath( __file__ ))
    file_path = raw_input('Which culture do you wish to generate names from? \nPlease type the name exactly.\n')
    with open(file_path, 'r') as f:
        language = f.readlines()
    run_loop(language)

    #test(language)


main()
