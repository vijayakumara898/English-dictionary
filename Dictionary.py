import json
from difflib import get_close_matches

data = json.load(open("data.json"))

def translate(word):
    word = word.lower()
    if word in data:
        return data[word]
    elif word.title() in data:
        return data[word.title()]
    elif word.upper() in data:
        return data[word.upper()]
    elif len(get_close_matches(word,data.keys()))> 0:
        yn = input("Did you mean %s instead.Enter y if yes or n if no : " %get_close_matches(word, data.keys(),cutoff=0.8)[0])
        yn=yn.lower()
        if yn == "y":
            return data[get_close_matches(word, data.keys(), cutoff=0.8)[0]]
        elif yn == "n":
            return "please check the word"
        else:
            return "we don't understand"
    else:
        return "the word does not exit.please double check the word"

word = input("Enter the word: ")
output = translate(word)

if type(output) == list:
    for item in output:
        print(item)
else:
    print(output)

