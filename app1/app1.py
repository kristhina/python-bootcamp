import json
from difflib import get_close_matches

eng_dict = json.load(open("data.json"))

def translate(word):
    if word in eng_dict:
        return eng_dict[word]
    if word.lower() in eng_dict:
        return eng_dict[word.lower()]
    if len(get_close_matches(word, eng_dict.keys())) > 0:
        print("Did you mean {}?".format(get_close_matches(word, eng_dict.keys())[0]))
        decision = input("y/n")
        if decision == "y":
            return eng_dict[get_close_matches(word, eng_dict.keys())[0]]
        if decision == "n":
            return ["so we do not have your word in our dictionary"]
        return ["you did not write y nor n"]
    return ["Such word does not exist"]

word_to_check = input("What do you want to check? ")

output = (translate(word_to_check))

for definition in output:
    print(definition)