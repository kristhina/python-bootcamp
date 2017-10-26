

from countries import countries

lista = []
for country in countries:
    lista.append(len(country['borders']))
max_index = lista.index(max(lista))
print("The country with maximum neighbours is {}, the neighbours are: {}" .format(countries[max_index]['name']['common'], countries[max_index]['borders']))



lista = []
area_list = []
name_list = []
for country in countries:
    lista.append(((country['area']), (country['name']['common'])))
for (area, name) in lista:
    area_list.append(area)
    name_list.append(name)
area_index = area_list.index((max(area_list)))
print("The country of the biggest area: {} (area: {})".format(name_list[area_index], area_list[area_index]))

for country in countries:
    if country['capital'] != "":
        if country['capital'][0] == "W":
            print('Country = {}, Capital = {}'.format(country['name']['common'], country['capital']))

for country in countries:
    if len(country['currency']) > 1:
        print("Kraj: {}, waluty: {}".format(country['name']['common'], country['currency']))


for country in countries:
    if country['region'] != "Africa":
        print(country['name']['common'])





for country in countries:
    if country['subregion'] == "Northern America":
        print(country['name']['common'])
