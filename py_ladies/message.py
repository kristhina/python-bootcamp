file = open("encodedmsg.txt")
data = file.readlines()
file.close()

rozwiazanie = ""
for element in data:
    for sign in element:
        if (65 <= ord(sign) <= 90) or (97 <= ord(sign) <= 122):
            rozwiazanie += sign

print(rozwiazanie)


