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
        # niedowaga 18,5
        # nadwaga 25
        if self.bmi < 18.5:
            oczekiwana_waga = 18.5 * (self.wzrost * 0.01) ** 2
            roznica = oczekiwana_waga - self.waga
            print("Musisz przytyć {} kg.".format(roznica))
        elif self.bmi > 25:
            oczekiwana_waga = 25 * (self.wzrost * 0.01) ** 2
            roznica = self.waga - oczekiwana_waga
            print("Musisz schudnąć {} kg.".format(roznica))
        else:
            print("Ważysz idealnie :)")

    def save_data(self):
        with open("{}.json".format(self.imie), "w") as file:
            json.dump({"imie": self.imie, "waga": self.waga, "wzrost": self.wzrost}, file)

    def to_burn(self):
        # ile kalorii tracimy przy określonej czynności
        bieganie = 500
        rower = 600
        hobby = 250
        szachy = 150

        oczekiwana_waga = 25 * (self.wzrost * 0.01) ** 2
        roznica = self.waga - oczekiwana_waga
        if self.bmi < 25:
            print("Nie musisz nic schudnąć")
        else:
            liczba_kalorii_do_spalenia = roznica * 6000
            godziny_biegania = round(liczba_kalorii_do_spalenia / bieganie)
            godziny_roweru = round(liczba_kalorii_do_spalenia / rower)
            godziny_hobby = round(liczba_kalorii_do_spalenia / hobby)
            godziny_szachy = round(liczba_kalorii_do_spalenia / szachy)
            print(
                "Żeby schudnąć do dobrej wagi musisz biegać przez {} godzin, jeździć na rowerze przez {} godzin, uprawiać hobby przez {} godzin albo grać w szachy przez {} godzin.".format(
                    godziny_biegania, godziny_roweru, godziny_hobby, godziny_szachy))

    def to_eat(self):
        ziemniaki = 800  # kalorie w kg
        czekolada = 4500  # kalorie w kg

        oczekiwana_waga = 18.5 * (self.wzrost * 0.01) ** 2
        roznica = oczekiwana_waga - self.waga
        if self.bmi > 18.5:
            print("Nie musisz nic przytyć")
        else:
            liczba_kalorii_do_przyjecia = 6000 * roznica
            ziemniaki_do_zjedzenia = round(liczba_kalorii_do_przyjecia / ziemniaki)
            czekolada_do_zjedzenia = round(liczba_kalorii_do_przyjecia / czekolada)
            print("Żeby przytyć do dobrej wagi musisz zjeść {} kg ziemniaków albo {} kg czekolady.".format(
                ziemniaki_do_zjedzenia, czekolada_do_zjedzenia))

    def what_to_do(self):
        if self.bmi < 18.5:
            print("Jesteś za chudy, musisz trochę przytyć.")
            self.to_eat()
        elif self.bmi > 25:
            print("Ważysz za dużo, musisz trochę schudnąć.")
            self.to_burn()
        else:
            print("Ważysz idealnie! Tak trzymaj!")


class Polityk(Czlowiek):
    lapowka = False

    def speak(self):
        if not self.lapowka:
            print("Kłamię, bo mogę")
        elif self.lapowka:
            super().speak()

    def recive_bribe(self):
        self.lapowka = True


pol = Polityk("arnold", 150, 35)
pol.speak()
pol.recive_bribe()
pol.speak()
print(pol.bmi)
pol.save_data()
pol.diff_to_norm()
pol.what_to_do()
