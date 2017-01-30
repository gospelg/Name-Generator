
import base
import json
import os

def alpha_list():                           
	from string import ascii_lowercase
	alphabet = []
	for letter in ascii_lowercase:
		  alphabet.append(letter)
	  alphabet.append('blank')
	  alphabet.append('first letter')
    return alphabet

def import_data():
  alphabet = alpha_list()
  
  for i in range(len(alphabet)):
	    filename = le_path + '\%s.json' % alphabet[i]
	    with open(filename, 'r') as f:
		      base.all_dicts[i] = json.load(f)
