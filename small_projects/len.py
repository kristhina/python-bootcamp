def string_length(mystring):
    if type(mystring) == int or type(mystring) == float:
        return "Integer and float doesn't have length"
    else:
        return len(mystring)

print(string_length(7.5))
