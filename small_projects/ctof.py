
def ctof(celcius):
    if celcius < -273.15:
        return "Too low temperature"
    else:
        return celcius*9/5 + 32

temperatures=[10,-20,-289,100]
file = open("ctof.txt", "w")
for temp in temperatures:
    if type((ctof(temp))) == float:
        file.write(str(ctof(temp)) + "\n")

file.close()
