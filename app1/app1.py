import json
from difflib import get_close_matches

eng_dict = json.load(open("data.json"))

def translate(word):
    if word in eng_dict:
        return eng_dict[word]
    elif word.lower() in eng_dict:
        return eng_dict[word.lower()]
    elif len(get_close_matches(word, eng_dict.keys())) >0:
        print("Did you mean {}?".format(get_close_matches(word, eng_dict.keys())[0]))
        decision = input("y/n")
        if decision == "y":
            return eng_dict[get_close_matches(word, eng_dict.keys())[0]]
        elif decision == "n":
            return "so we do not have your word in our dictionary"
        else:
            return "you did not write y nor n"
    else:
        return "Such word does not exist"

word_to_check = input("What do you want to check? ")

output = (translate(word_to_check))
if type(output) == str:
    print(output)
else:
    for definition in output:
        print(definition)