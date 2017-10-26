def czy_to_jest_cyfra(tekst):
    if isinstance(tekst, (float, int)):
        return tekst
    if not isinstance(tekst, str):
        return False
    tekst = tekst.replace(',', '.')
    try:
        a = float(tekst)
        return a
    except ValueError:
        return False

def czy_ala_ma_kota(wiek_ali):
    wiek_ali = czy_to_jest_cyfra(wiek_ali)
    if wiek_ali and wiek_ali < 18 or wiek_ali > 40:
        return True
    return False

print(czy_ala_ma_kota('25,5'))
print(czy_ala_ma_kota('eradaf'))
print(czy_ala_ma_kota('5'))
