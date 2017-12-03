file = open("py1.2")
data = file.readlines()
file.close()
names = []
heigh = []
eyes = []
creatures = {}
for creature in data:
    first_n = creature.find(". ")+2
    last_n = creature.find(" has")
    names.append(creature[first_n:last_n])
    first_h = creature.find(" is ") + 4
    last_h = creature.find(" cm")
    heigh.append(creature[first_h: last_h])
    first_e = creature.find("has ") + 4
    last_e = creature.find(" and")
    eyes.append(creature[first_e:last_e])

for i in range(len(names)):
    creatures[names[i]] = {"height": heigh[i], "eyes": eyes[i]}
print(creatures)


file1 = open("hero_200_plus", "w")
file2 = open("hero_short", "w")
for creature in creatures:
    if int(creatures[creature]["height"]) > 200:
        file1.writelines("{}, ".format(creature))
    else:
        file2.writelines("{}, ".format(creature))
file1.close()
file2.close()


file3 = open("heigh_for_eyes", "w")
different_eyes = set(eyes)
for color in different_eyes:
    i = 0
    heigh_sum = 0
    for creature in creatures:
        if color == creatures[creature]["eyes"]:
            heigh_sum += int(creatures[creature]["height"])
            i+=1
    file3.write("Średni wzrost osób z kolorem oczu {} wynosi {} cm.\n".format(color, round(heigh_sum/i, 2)))
file3.close()


print(different_eyes)
file4 = open("heigh_for_eyes")
data2 = file4.readlines()
file4.close()
file5 = open("height_for_eyes_translation", "w")
for a in data2:
    a = a.replace(" red ", " czerwone ")
    a = a.replace("blue", "niebieskie")
    a = a.replace("gold", "złote")
    a = a.replace("pink", "różowe")
    a = a.replace("green", "zielone")
    a = a.replace("yellow", "żółte")
    a = a.replace("orange", "pomarańczowe")
    a = a.replace("hazel", "piwne")
    a = a.replace("black", "czarne")
    a = a.replace("brown", "brązowe")
    a = a.replace("gray", "szare")
    a = a.replace("unknown", "nieznany")
    file5.write(a)
file5.close()



