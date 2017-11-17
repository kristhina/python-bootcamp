from math import pi
from math import sqrt

r = int(input("podaj promień podstawy stozka"))
h = int(input("podaj wysokość stożka"))
l = sqrt(r**2 + h**2)
objetosc = 1/3 * pi * r**2 * h
pole_podstawy = pi * r**2
pole_powierzchni_bocznej = pi * r * l
pole_powierzchni_calkowitej = pole_podstawy + pole_powierzchni_bocznej

print("pole podstawy wynosi {}".format(pole_podstawy))
print("pole powierzchni bocznej wynosi {}".format(pole_powierzchni_bocznej))
print("pole powierzchni całkowitej wynosi {}".format(pole_powierzchni_calkowitej))





