
from __future__ import division
import json
import os
from learner import alpha_list
import numpy

alpha_index = [
    "blank", 
    "a", 
    "b", 
    "c", 
    "d", 
    "e", 
    "f", 
    "g", 
    "h", 
    "i", 
    "j", 
    "k", 
    "l", 
    "m", 
    "n", 
    "o", 
    "p", 
    "q", 
    "r", 
    "s", 
    "t", 
    "total", 
    "u", 
    "v", 
    "w", 
    "x", 
    "y", 
    "z"
    ]
	

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
		
def weights(the_data):
	for dataset in the_data:
		for i in [x for x in range(27) if x != 21]:
			if dataset[alpha_index[i]] != 0:
				dataset[alpha_index[i]] = dataset[alpha_index[i]] / dataset['total']
			else:
				pass
			
			
def main():
	file_path = raw_input('Where are the jsons?')
	language = import_data(file_path)
	weights(language)
	print language
	
main()
	
			
