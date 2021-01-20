import json
data = json.load(open("dictionary/data.json"))

import difflib
from difflib import SequenceMatcher
from difflib import get_close_matches


def translate(word):
    word = word.lower()
    if word in data:
        return data[word]
    else:
        return "The word doesn't exist."

word = input("Enter word: ")
print(translate(word))