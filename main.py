#gematria calculator

#assigning a number to a letter
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
			

	
			
		
		
		
#notes
#here is an example function that returns all permutations of a list. Seems useful
#def permutation(s):
#   if len(s) == 1: this first if statement just accounts for a list having one item, in which case it has only one permutation
#     return [s]
#
#   perm_list = [] # resulting list
#   for a in s:
#     remaining_elements = [x for x in s if x != a] identifies the rest character. It cycles for a in s and then remaining list is everything that is not a
#     z = permutation(remaining_elements) # permutations of sublist
#
#    for t in z:
#       perm_list.append([a] + t)
#
#   return perm_list
		
	
	
