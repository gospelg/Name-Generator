
import base
import json
import os
from learner import alpha_list

#imports json data back into dictionaries. The arguement is the dir where the specific jsons are, to be inputed by user in another 
#function.
def import_data():
	alphabet = alpha_list(file_path)
	data_dump = []
#files are loaded as dictionaries to an array. They are loaded in order, and must be accessed by index. 
	for i in range(len(alphabet)):
	    filename = file_path + '\%s.json' % alphabet[i]
	    with open(filename, 'r') as f:
		    data_dump.append(json.load(f))
			

	
			
