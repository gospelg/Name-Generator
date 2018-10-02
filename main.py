from __future__ import division
import numpy as np
import os

class word(object):
    
    def __init__(self, learning_list, newline_bias, magic_number, commit):
        self.learning_list = learning_list
        self.newline_bias = newline_bias
        self.magic_number = magic_number
        self.commit = commit

    def clean_data(self, prob_dict):
        round = (1.0 - sum(prob_dict.itervalues()) )
        prob_dict.values()[0] += (round)
        clean = [[],[]]
        for x,y in prob_dict.items():
            clean[0].append(x)
            clean[1].append(y)
        return clean
        
    def find_prob(self):
        probability = {} #frequency of patterns
        total = 0 # total to divide by and find probability
        if len(self.commit) == 0:
            for word in self.learning_list:
                if word[0].lower() not in probability:
                    probability[word[0].lower()] = 1
                    total += 1
                else:
                    probability[word[0].lower()] += 1
                    total += 1
        else:
            for word in self.learning_list:
                working = word.lower()
                commit = ''.join(self.commit)
                if commit in working:
                    position = working.index(commit)
                    next_char = working[position + len(commit)]
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
        cleaned = self.clean_data(probability)
        return cleaned

    def add_bias(self, probability):
        if '\n' in probability:
            adjustment = newline_bias / (len(probability) - 1)
            probability['\n'] += newline_bias
            for x in probability:
                if x == '\n':
                    break
                elif probability[x] - adjustment < 0:
                    probability[x] = 0
                else:    
                    probability[x] -= adjustment
        else:
            return probability
        return probability
        
    def next_char(self, cleaned_probs):
        try:
            x = np.random.choice(cleaned_probs[0], p=cleaned_probs[1])
            return x
        except:
            print 'probability error! Dumping data'
            print probability
            print sum(probability[1])
        
    def generate(self):
        probability = self.find_prob()
        self.commit.append(self.next_char(probability))
        while '\n' not in self.commit:
            probability = self.find_prob()
            self.commit.append(self.next_char(probability))
        print ''.join(self.commit)
 
def run_loop(language):
    operation = raw_input('Run?\n')
    if operation == 'y':
        i = word(language, 0, 0, [])
        i.generate()
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
