file = open("fruits.txt", "r")
content = file.readlines()
for element in content:
    new_element = element[0:-1]
    print(len((new_element)))
file.close()