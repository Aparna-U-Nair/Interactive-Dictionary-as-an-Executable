import json
from difflib import SequenceMatcher, get_close_matches
import time
# with open('data.json','r') as fjson:
#     cont = fjson.read()
# z = json.loads(cont)
# print(type(z))

with open('data.json','r') as fjson:    
    data = json.load(fjson)
 
print('INTERACTIVE ENGLISH DICTIONARY')
print('-------------------------------')
while True:
    user_input = input('Tell me the word! ')
    word_list = [user_input.lower(), user_input.title(), user_input.upper()]
    word_present = [word for word in word_list if word in data.keys()]

    if word_present:
        for meaning in data[word_present[0]]:  
            print(meaning) 

    elif get_close_matches(word_list[0],data.keys(),n=3,cutoff=0.8):
        matches = get_close_matches(word_list[0],data.keys(),n=3,cutoff=0.8)
        check = input(f'Did you mean any of this {matches}? Say Y or N: ')
        if check == 'Y':
            continue
        else:
           print('Cannot find any matches, please try again') 

    else:
        print('Word does not exist. Please try again.')
    
    more = input('Do you wish to try some other word? Expecting Y or '+
                    'N: ')
    if more == 'Y': continue
    elif more == 'N':
        print('Thanks for using my script!')
        time.sleep(5)
        break
    else:
        print('Incorrect input. Thanks for trying.')
        time.sleep(5)
        break

#Will check the percentage of matching between two sequences.
# print(SequenceMatcher(None,'Rainn','Rain').ratio())
