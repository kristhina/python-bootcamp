import json

class Czlowiek:
    def __init__(self, imie, wzrost, waga):
        self.imie = imie
        self.wzrost = wzrost
        self.waga = waga
        self.bmi = self.count_bmi()

    def speak(self):
        print("Mówię prawdę")

    def count_bmi(self):
        return round(self.waga / (self.wzrost * 0.01) ** 2, 2)

    def diff_to_norm(self):
        #niedowaga 18,5
        #nadwaga 25
        if self.bmi <18.5:
            oczekiwana_waga = 18.5 * self.wzrost ** 2
            roznica = oczekiwana_waga - self.waga
            print("Musisz przytyć{} kg.".format(roznica))
        elif self.bmi > 25:
            oczekiwana_waga = 25 * self.wzrost ** 2
            roznica = oczekiwana_waga - self.waga
            print("Musisz schudnąć{} kg.".format(roznica))
        else:
            print("Ważysz idealnie")




    def save_data(self):
        with open(self.imie, 'w') as file:
            json.dump({"imie": self.imie, "waga": self.waga, "wzrost": self.wzrost}, file)

    def to_burn(self):
        pass

    def to_eat(self):
        pass

    def what_to_do(self):
        pass

class Polityk(Czlowiek):
    lapowka = False

    def speak(self):
        if not self.lapowka:
            print("Kłamię, bo mogę")
        elif self.lapowka:
            super().speak()

    def recive_bribe(self):
        self.lapowka = True

pol = Polityk("arnold", 150, 43)
pol.speak()
pol.recive_bribe()
pol.speak()
print(pol.bmi)
pol.save_data()
