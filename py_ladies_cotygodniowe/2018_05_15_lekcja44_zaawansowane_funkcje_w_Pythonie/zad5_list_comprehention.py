# Napisz list comprehension, która będzie zawierała tylko
# całkowite dodatnie liczby z listy [134.6, -2203.4, 344, 68.3, -112, 344, 1212.712]

my_list = [134.6, -2203.4, 344, 68.3, -112, 344, 1212.712]
a_list = [a for a in my_list if a > 0 and a == int(a)]
print(a_list)