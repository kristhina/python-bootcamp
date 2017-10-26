file = open('py1.2')
data = file.readlines()
names = []
heigh = []
eyes = []
creatures = {}
for creature in data:
    first_n = creature.find('. ')+2
    last_n = creature.find(' has')
    names.append(creature[first_n:last_n])
    first_h = creature.find(' is ') + 4
    last_h = creature.find(' cm')
    heigh.append(creature[first_h: last_h])
    first_e = creature.find('has ') + 4
    last_e = creature.find(' and')
    eyes.append(creature[first_e:last_e])

for i in range(len(names)):
    creatures[names[i]] = {'height': heigh[i], 'eyes': eyes[i]}
print(creatures)

file1 = open('hero_200_plus', 'w')
file2 = open('hero_short', 'w')
for creature in creatures:
    if int(creatures[creature]['height']) > 200:
        file1.writelines('{}, '.format(creature))
    else:
        file2.writelines('{}, '.format(creature))
