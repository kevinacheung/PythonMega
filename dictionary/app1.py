import json
data = json.load(open("dictionary/data.json"))

import difflib
from difflib import SequenceMatcher
from difflib import get_close_matches


def translate(w):
    w = w.lower()
    if w in data:
        return data[w]
    elif w.title() in data: #if user entered "texas" this will check for "Texas" as well.
        return data[w.title()]
    elif w.upper() in data: #in case user enters words like USA or NATO
        return data[w.upper()] 
    elif len(get_close_matches(w, data.keys())) > 0:
        yn = input("Did you mean %s instead? Y or N? " %get_close_matches(w, data.keys())[0])
        if yn == "Y" or yn == "y":
            return data[get_close_matches(w, data.keys())[0]]
        elif yn == "N" or yn == "n":
            return "The word doesn't exist. Please check again."
        else:
            return "We didn't understand your query."
    else:
        return "The word doesn't exist. Please check again."

word = input("Enter word: ")
output = translate(word)

if type(output) == list:
    for item in output:
        print(item)
else:
    print(output)
