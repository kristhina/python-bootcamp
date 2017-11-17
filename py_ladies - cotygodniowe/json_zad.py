import json

with open("py1.2.json") as json_data:
    data = json.load(json_data)

file1 = open("sw_women", "w")
file2 = open("sw_men", "w")

for i in range(len(data)):
    if data[i]["gender"] == "male":
        file2.write(data[i]["name"] + "\n")
    elif data[i]["gender"] == "female":
        file1.write(data[i]["name"] + "\n")

file1.close()
file2.close()

file3 = open("sw_all_heroes", "w")
for i in range(len(data)):
    if data[i]["gender"] == "male":
        plec = "mężczyzną"
    elif data[i]["gender"] == "female":
        plec = "kobietą"
    else:
        plec = "nieznanej płci"
    file3.write("{} waży {} kg jest {} i pochodzi z {}.\n".format(data[i]["name"], data[i]["mass"], plec, data[i]["homeworld"]))

file3.close()