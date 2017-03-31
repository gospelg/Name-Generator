
from __future__ import division
import json
import os
from base import alpha_list
import numpy


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
				
def main():
	working_dir = os.path.dirname(os.path.abspath( __file__ ))
    file_path = raw_input('Where are the jsons?')
	language = import_data(file_path)
	
	
main()
	
			
