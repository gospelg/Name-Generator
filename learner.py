from __future__ import division
import base
import json
import os
import numpy as np


def word_stats(language):
    word_len = []
    for word in language:
        x = len(word)
        word_len.append(x)
    base.stats["mean"] = np.mean(word_len)
    base.stats["std_dev"] = np.std(word_len)
    
    
#this function accounts for the first letter of a word. 
def first_char(place_names):
    for place in place_names:
        i = place[0]
        if i in base.first_letter:
            base.first_letter[i] = base.first_letter[i] + 1
            base.first_letter['total'] = base.first_letter['total'] + 1
            

#this is the primary learning function. It calls the first_char function, which records the frequency of the first letter words
#start with. If then cylces through each letter of each word, and calls the find_frequncy function on it.
def learn_language(place_names):
    word_stats(place_names)
    first_char(place_names)

    for place in place_names:
        for i in range(1, len(place) - 1):
            find_frequency(place, i)
            
    find_weights(base.all_dicts)
        
        
#this one identifies the letter, selects the correct dictionary, then it looks at what letter comes next. It adds a tally in the
#dictionary for the next letter and a tally for the total.      
def find_frequency(place, x):
    char = place[x]
    
    if char == 'A':
        nex_char = place[x + 1]
        base.a[nex_char] = base.a[nex_char] + 1
        base.a['total'] = base.a['total'] + 1
            
    if char == 'B':
        nex_char = place[x + 1]
        base.b[nex_char] = base.b[nex_char] + 1
        base.b['total'] = base.b['total'] + 1
            
    if char == 'C':
        nex_char = place[x + 1]
        base.c[nex_char] = base.c[nex_char] + 1
        base.c['total'] = base.c['total'] + 1
        
    if char == 'D':
        nex_char = place[x + 1]
        base.d[nex_char] = base.d[nex_char] + 1
        base.d['total'] = base.d['total'] + 1
        
    if char == 'E':
        nex_char = place[x + 1]
        base.e[nex_char] = base.e[nex_char] + 1
        base.e['total'] = base.e['total'] + 1
    
    if char == 'F':
        nex_char = place[x + 1]
        base.f[nex_char] = base.f[nex_char] + 1
        base.f['total'] = base.f['total'] + 1
        
    if char == 'G':
        nex_char = place[x + 1]
        base.g[nex_char] = base.g[nex_char] + 1
        base.g['total'] = base.g['total'] + 1
        
    if char == 'H':
        nex_char = place[x + 1]
        base.h[nex_char] = base.h[nex_char] + 1
        base.h['total'] = base.h['total'] + 1
        
    if char == 'I':
        nex_char = place[x + 1]
        base.i[nex_char] = base.i[nex_char] + 1
        base.i['total'] = base.i['total'] + 1
        
    if char == 'J':
        nex_char = place[x + 1]
        base.j[nex_char] = base.j[nex_char] + 1
        base.j['total'] = base.j['total'] + 1
    
    if char == 'K':
        nex_char = place[x + 1]
        base.k[nex_char] = base.k[nex_char] + 1
        base.k['total'] = base.k['total'] + 1
        
    if char == 'L':
        nex_char = place[x + 1]
        base.l[nex_char] = base.l[nex_char] + 1
        base.l['total'] = base.l['total'] + 1
        
    if char == 'M':
        nex_char = place[x + 1]
        base.m[nex_char] = base.m[nex_char] + 1
        base.m['total'] = base.m['total'] + 1   
        
    if char == 'N':
        nex_char = place[x + 1]
        base.n[nex_char] = base.n[nex_char] + 1
        base.n['total'] = base.n['total'] + 1       
    
    if char == 'O':
        nex_char = place[x + 1]
        base.o[nex_char] = base.o[nex_char] + 1
        base.o['total'] = base.o['total'] + 1
        
    if char == 'P':
        nex_char = place[x + 1]
        base.p[nex_char] = base.p[nex_char] + 1
        base.p['total'] = base.p['total'] + 1
        
    if char == 'Q':
        nex_char = place[x + 1]
        base.q[nex_char] = base.q[nex_char] + 1
        base.q['total'] = base.q['total'] + 1   
        
    if char == 'R':
        nex_char = place[x + 1]
        base.r[nex_char] = base.r[nex_char] + 1
        base.r['total'] = base.r['total'] + 1
        
    if char == 'S':
        nex_char = place[x + 1]
        base.s[nex_char] = base.s[nex_char] + 1
        base.s['total'] = base.s['total'] + 1   
        
    if char == 'T':
        nex_char = place[x + 1]
        base.t[nex_char] = base.t[nex_char] + 1
        base.t['total'] = base.t['total'] + 1   
    
    if char == 'U':
        nex_char = place[x + 1]
        base.u[nex_char] = base.u[nex_char] + 1
        base.u['total'] = base.u['total'] + 1   
        
    if char == 'V':
        nex_char = place[x + 1]
        base.v[nex_char] = base.v[nex_char] + 1
        base.v['total'] = base.v['total'] + 1   
        
    if char == 'W':
        nex_char = place[x + 1]
        base.w[nex_char] = base.w[nex_char] + 1
        base.w['total'] = base.w['total'] + 1   
        
    if char == 'X':
        nex_char = place[x + 1]
        base.x[nex_char] = base.x[nex_char] + 1
        base.x['total'] = base.x['total'] + 1       
        
    if char == 'Y':
        nex_char = place[x + 1]
        base.y[nex_char] = base.y[nex_char] + 1
        base.y['total'] = base.y['total'] + 1       
        
    if char == 'Z':
        nex_char = place[x + 1]
        base.z[nex_char] = base.z[nex_char] + 1
        base.z['total'] = base.z['total'] + 1       
        
    if char == ' ':
        nex_char = place[x + 1]
        base.blank[nex_char] = base.blank[nex_char] + 1
        base.blank['total'] = base.blank['total'] + 1       
        
    else:
        pass

#for each dict, divides each key by total to get an average
def find_weights(data):
    for subset in data[:-1]:
        for key in sorted(subset):
            if subset["total"] != 0:
                subset[key] = subset[key] / subset["total"]
            else:
                pass
            
#this function imports a txt file with words that the program uses to gather its data.
def importer(the_file):
    learninglist = []
    with open(the_file, 'r') as f:
        for line in f:
            learninglist.append(line.strip())
    learninglist = [x.upper() for x in learninglist]
    return learninglist
    

#this is the function that dumps all of the data filled dictionaries as json files, for later use in other modules.     
def make_dump(language):
    working_dir = os.path.dirname(os.path.abspath( __file__ ))
#create a folder for all the json dumps to go into. Just adds it to the current working dir
    newpath = working_dir + r'\cultures\%s' % language
    if not os.path.exists(newpath):
        os.makedirs(newpath)

    alphabet = base.alpha_list()
    for i in range(len(alphabet)):
        filename = newpath + '\%s.json' % alphabet[i]
        with open(filename, 'w') as f:
            json.dump(base.all_dicts[i], f, sort_keys=True, indent=4)   
            
"""call alpha_list func to generate the list, which can then be cycled through to name the jsons. The base.all_dicts is an array
that contains all of the data dictionaries. Alphabet is an array of strings that matches base.all_dicts's array of dictionaries
so as they both cycle through indicies it matches and puts a string name with the variable.
ie. alphabet[0] = 'a' all_dicts[0] = a
"""
    
def main():
    lng_group = raw_input('What language group do these places belong to? \n ')
    print 'Ok. Process initiated...'
    the_file = raw_input('What file do you want to learn from? \n ')
    la_lista = importer(the_file)
    learn_language(la_lista)
    make_dump(lng_group)
    
    
main()
                        
    
            
        

        
    
    
