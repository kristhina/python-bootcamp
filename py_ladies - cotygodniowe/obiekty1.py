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
            oczekiwana_waga = 18.5 / self.wzrost ** 2
            roznica = oczekiwana_waga - self.waga
            print("Musisz przytyć{} kg.".format(roznica))
        elif self.bmi > 25:
            oczekiwana_waga = 25 / self.wzrost ** 2
            roznica = oczekiwana_waga - self.waga
            print("Musisz schudnąć{} kg.".format(roznica))
        else:
            print("Ważysz idealnie")




    def save_data(self):
        with open('{}.json'.format(self.imie), 'w') as file:
            json.dump({"imie": self.imie, "waga": self.waga, "wzrost": self.wzrost}, file)

    def to_burn(self):
        # Zakładając, że aby schudnąć 1 kg trzeba spalić 6000kcal,
    # napisz funkcjonalność, która powie użytkownikowi,
    # ile powinien godzin biegać(500kcal/h) /
    # jeździć rowerem(600kcal/h) /
    # uprawiać hobby(250kcal/h) /
    # grać w szachy(150kcal/h) / etc. aby być w normie (to_burn).
        bieganie = 500
        rower = 600
        hobby = 250
        szachy = 150

        oczekiwana_waga = 25 / self.wzrost ** 2
        roznica = oczekiwana_waga - self.waga
        if roznica < 0:
            print("Nie musisz nic schudnąć")
        else:
            liczba_kalorii_do_spalenia = roznica*6000
            godziny_biegania = liczba_kalorii_do_spalenia/bieganie
            godziny_roweru = liczba_kalorii_do_spalenia/rower
            godziny_hobby = liczba_kalorii_do_spalenia/hobby
            godziny_szachy = liczba_kalorii_do_spalenia/szachy
            print("Żeby schudnąć do dobrej wagi musisz biegać przez {} godzin, jeździć na rowerze przez {} godzin, uprawiać hobby przez {} godzin albo grać w szachy przez {} godzin.".format(godziny_biegania, godziny_roweru, godziny_hobby, godziny_szachy))

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

pol = Polityk("arnold", 150, 90)
pol.speak()
pol.recive_bribe()
pol.speak()
print(pol.bmi)
pol.save_data()
pol.diff_to_norm()
pol.to_burn()
