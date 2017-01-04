#this module contains the neccessary tools for assigning numbers to words, should that functionality be desired.

alphabet_dict = {
	1:'a', 
	2:'b', 
	3:'c', 
	4:'d', 
	5:'e', 
	6:'f', 
	7:'g', 
	8:'h', 
	9:'i', 
	10:'j', 
	11:'k', 
	12:'l',
	13:'m',
	14:'n',
	15:'o',
	16:'p',
	17:'q',
	18:'r',
	19:'s',
	20:'t',
	21:'u',
	22:'v',
	23:'w',
	24:'x',
	25:'y',
	26:'z'
}

#this will find the number that corresponds to the word
def find_number(word):
	
	number = 0
	for i in word:
		for key, value in alphabet_dict.items():
			if value == i:
				number += key
			
return number
