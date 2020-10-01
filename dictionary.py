import json
from difflib import get_close_matches
f = open('data.json')
data = json.load(f)

def translate(word):
    word = word.lower() 
    if word in data:
        return data[word]
    elif word.title() in data:
        return data[word.title()]
    elif word.upper() in data:
        return data[word.upper()]
    elif len(get_close_matches(word, data.keys())) > 0:
        print("Are you looking for %s instead" %get_close_matches(word, data.keys())[0])
        decision = input("Press y to confirm :")
        if(decision == "y"):
            return data[get_close_matches(word, data.keys())[0]]
        else:
            return("It is not in our database")    
    else:
        print("The word is either wrong or not in our database")

word = input("Enter your word: ")
output = translate(word)
num = 1

if type(output) == list:
    for description in output:
        print(str(num) + "." + description)
        num = num + 1
else:
    print(output)
