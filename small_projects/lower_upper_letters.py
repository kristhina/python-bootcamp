def myfunc(argument):
    list_for_new_string = []
    for i, letter in enumerate(argument):
        if i % 2 == 0:
            new_letter = letter.lower()
        else:
            new_letter = letter.upper()
        list_for_new_string.append(new_letter)
    new_string = ''.join(list_for_new_string)
    return new_string

print(myfunc('cokolwiek'))