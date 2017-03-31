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
        
def generate_name(dataset):
    place = []
    stats = dataset[28]
    mu = stats["mean"]
    std = stats["std_dev"]
    word_length = np.random.normal(mu, std)
    print word_length
    
    first = data_strip(dataset[27])
    x = np.random.choice(first[0], p=first[1])
    place.append(x.upper())
    
    while len(place) < word_length:
        if x == 'A':
            stuff = data_strip(dataset[0])
            y = np.random.choice(stuff[0], p=stuff[1])
            place.append(y.lower())
            x = y
        
        if x == 'B':
            stuff = data_strip(dataset[1])
            y = np.random.choice(stuff[0], p=stuff[1])
            place.append(y.lower())
            x = y
                
        if x == 'C':
            stuff = data_strip(dataset[2])
            y = np.random.choice(stuff[0], p=stuff[1])
            place.append(y.lower())
            x = y
            
        if x == 'D':
            stuff = data_strip(dataset[3])
            y = np.random.choice(stuff[0], p=stuff[1])
            place.append(y.lower())
            x = y
            
        if x == 'E':
            stuff = data_strip(dataset[4])
            y = np.random.choice(stuff[0], p=stuff[1])
            place.append(y.lower())
            x = y
        
        if x == 'F':
            stuff = data_strip(dataset[5])
            y = np.random.choice(stuff[0], p=stuff[1])
            place.append(y.lower())
            x = y
            
        if x == 'G':
            stuff = data_strip(dataset[6])
            y = np.random.choice(stuff[0], p=stuff[1])
            place.append(y.lower())
            x = y
            
        if x == 'H':
            stuff = data_strip(dataset[7])
            y = np.random.choice(stuff[0], p=stuff[1])
            place.append(y.lower())
            x = y
            
        if x == 'I':
            stuff = data_strip(dataset[8])
            y = np.random.choice(stuff[0], p=stuff[1])
            place.append(y.lower())
            x = y
            
        if x == 'J':
            stuff = data_strip(dataset[9])
            y = np.random.choice(stuff[0], p=stuff[1])
            place.append(y.lower())
            x = y
        
        if x == 'K':
            stuff = data_strip(dataset[10])
            y = np.random.choice(stuff[0], p=stuff[1])
            place.append(y.lower())
            x = y
            
        if x == 'L':
            stuff = data_strip(dataset[11])
            y = np.random.choice(stuff[0], p=stuff[1])
            place.append(y.lower())
            x = y
            
        if x == 'M':
            stuff = data_strip(dataset[12])
            y = np.random.choice(stuff[0], p=stuff[1])
            place.append(y.lower())
            x = y
            
        if x == 'N':
            stuff = data_strip(dataset[13])
            y = np.random.choice(stuff[0], p=stuff[1])
            place.append(y.lower())
            x = y      
        
        if x == 'O':
            stuff = data_strip(dataset[14])
            y = np.random.choice(stuff[0], p=stuff[1])
            place.append(y.lower())
            x = y
            
        if x == 'P':
            stuff = data_strip(dataset[15])
            y = np.random.choice(stuff[0], p=stuff[1])
            place.append(y.lower())
            x = y
            
        if x == 'Q':
            stuff = data_strip(dataset[16])
            y = np.random.choice(stuff[0], p=stuff[1])
            place.append(y.lower())
            x = y 
            
        if x == 'R':
            stuff = data_strip(dataset[17])
            y = np.random.choice(stuff[0], p=stuff[1])
            place.append(y.lower())
            x = y
            
        if x == 'S':
            stuff = data_strip(dataset[18])
            y = np.random.choice(stuff[0], p=stuff[1])
            place.append(y.lower())
            x = y  
            
        if x == 'T':
            stuff = data_strip(dataset[19])
            y = np.random.choice(stuff[0], p=stuff[1])
            place.append(y.lower())
            x = y
        
        if x == 'U':
            stuff = data_strip(dataset[20])
            y = np.random.choice(stuff[0], p=stuff[1])
            place.append(y.lower())
            x = y   
            
        if x == 'V':
            stuff = data_strip(dataset[21])
            y = np.random.choice(stuff[0], p=stuff[1])
            place.append(y.lower())
            x = y 
            
        if x == 'W':
            stuff = data_strip(dataset[22])
            y = np.random.choice(stuff[0], p=stuff[1])
            place.append(y.lower())
            x = y   
            
        if x == 'X':
            stuff = data_strip(dataset[23])
            y = np.random.choice(stuff[0], p=stuff[1])
            place.append(y.lower())
            x = y      
            
        if x == 'Y':
            stuff = data_strip(dataset[24])
            y = np.random.choice(stuff[0], p=stuff[1])
            place.append(y.lower())
            x = y       
            
        if x == 'Z':
            stuff = data_strip(dataset[25])
            y = np.random.choice(stuff[0], p=stuff[1])
            place.append(y.lower())
            x = y       
            
        if x == ' ':
            stuff = data_strip(dataset[26])
            y = np.random.choice(stuff[0], p=stuff[1])
            place.append(y.upper())
            x = y 
        final_word = "".join(place)
        return final_word
    
def test(language):
    answer = raw_input("Do you want to generate a name?\n")
    if answer == "y":
        print generate_name(language)
        test(language)
    else:
        exit()

def main():
    working_dir = os.path.dirname(os.path.abspath( __file__ ))
    culture_path = "{0}\cultures".format(working_dir)
    print os.listdir(culture_path)
    file_path = raw_input('Which culture do you wish to generate names from? \nPlease type the name exactly.\n')
    final_path = "{0}\{1}".format(culture_path, file_path)
    language = import_data(final_path)
    test(language)
    
    
main()
