import json
import os
from base import alpha_list
import numpy as np


#imports json data back into dictionaries. The arguement is the dir where the specific jsons are, to be inputed by user in another 
#function.
def import_data(file_path):
	alphabet = alpha_list()
	data_dump = []
#files are loaded as dictionaries to an array. They are loaded in order, and must be accessed by index. 
	for i in range(len(alphabet)):
	    filename = file_path + '\%s.json' % alphabet[i]
	    with open(filename, 'r') as f:
		    data_dump.append(json.load(f))
	return data_dump

def data_strip(data):
    prob = []
    letters = sorted(data)[:-1]
    for x in sorted(data)[:-1]:
        prob.append(data[x])
    new_data = (letters, prob)
    return new_data
        
def generate_name(dataset, number_places):
    place = []
    stats = dataset[28]
    mu = stats["mean"]
    std = stats["std_dev"]
    word_lengths = np.random.normal(mu, std, number_places)
    
    first = data_strip(dataset[27])
    x = np.random.choice(first[0], p=first[1])
    place.append(x.upper())
    
    

    
    
    
    

    
def main():
	working_dir = os.path.dirname(os.path.abspath( __file__ ))
    culture_path = working_dir + "\cultures"
    print os.listdir(culture_path)
    file_path = raw_input('Which culture do you wish to generate names from? \nPlease type the name exactly.\n')
	language = import_data(file_path)
	
	
main()
	
			
