import json
import time
import mysql.connector
from difflib import SequenceMatcher, get_close_matches

def db_connection():
    conn = mysql.connector.connect(
        user = "ardit700_student",
        password = "ardit700_student",
        host = "108.167.140.122",
        database = "ardit700_pm1database",
    )
    return conn

def db_query(words,flag=True):
    conn = db_connection()
    cur = conn.cursor()
    if flag:
        query = cur.execute(f"SELECT * FROM Dictionary WHERE Expression = "+
        "'{words[0]}' or Expression = '{words[1]}' or Expression = "+
        "'{words[2]}'")
    else:
        query = cur.execute('SELECT DISTINCT Expression FROM Dictionary')
    res = cur.fetchall()
    return res

#res from db_query will be a list of tuples.
def db_out(query_res):
    if len(query_res) ==1:
        print(query_res[0][1])
    else:
        for res in query_res:
            print(res[1])

def close_matches(word,res_list):
    vocab_list = [res[0] for res in res_list]
    matches = get_close_matches(word, vocab_list, n=3, cutoff=0.8)
    return matches

def user_interface():
    print('INTERACTIVE ENGLISH DICTIONARY')
    print('-------------------------------')
    while True:
        user_input = input('Tell me the word! ')
        list_of_words = [user_input.lower(),user_input.upper,\
                        user_input.title()]
        result = db_query(list_of_words)
        if result:
            db_out(result)
        else:
            res_list = db_query(list_of_words,flag=False)
            if close_matches(user_input.lower(), res_list):
                check = input(f'Did you mean any of these'+
                    ' {close_matches(user_input.lower(), res_list)}?, '+
                    'say Y or N and provide the correct word from the '+
                    'list after this input: ')
                if check == 'Y': continue
                elif check == 'N': print('The word you are looking for '+
                                'does not exist.')
                else: print('Sorry, Incorrect input!')
            else: print('No such word exist.')
        last = input('Would you like to try some other word? Say Y or N: ')
        if last == 'Y': continue
        elif last == 'N': 
            print("Thanks for trying this App!") 
            time.sleep(5)
            break
        else:
            print('Incorrect input. Thanks for trying.')
            time.sleep(5)
            break

if __name__=='__main__':
    user_interface()