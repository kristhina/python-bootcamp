# from pprint import pprint as pp
# zliczacz = {}
# wyraz = input('Podaj wyraz')
# for let in wyraz:
#     if let in zliczacz:
#         zliczacz[let] +=1
#     else:
#         zliczacz[let] = 1
#     print(zliczacz)
# print('--------------')
# pp(zliczacz)
#
# for a in range(10):
#     for b in range(9):
#         for c in range(8):
#             d = a*b + c
#             print(d)

# print(10*' '+'*')
# for i in range(10):
#     print(' '*(10-i) + i*'/' + i*'\\')
#
# k = 13
# print(k*' '+'*')

k = int(input("jaką chcesz mieć dużą choinkę "))
for i in range(k):
    if i % 3 == 2:
        print(" "*(k-i) + '/' + '*' + (i-2)*'/' + (i-2)*'\\' + '*' + '\\')
    else:
        print(' '*(k-i) + i*'/' + i*'\\')
for i in range(2):
    print((k-2)*' '+'|' + '  ' + '|')


