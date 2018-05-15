# Napisz algorytm,
# który zmieni wszystkie stopnie Celsujsza na Farenheita w podanej liście: [39.2, 36.5, 37.3, 37.8]

# ℉ =℃ * 1.8000 + 32.00

my_list = [39.2, 36.5, 37.3, 37.8]

f = map(lambda c:  1.8*c + 32, my_list)
print(list(f))
