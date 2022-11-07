from random import shuffle
a = str(input('Nome: '))
b = str(input('Nome: '))
c = str(input('Nome: '))
d = str(input('Nome: '))
l = [a, b, c, d]
shuffle(l)
print('A ordem será:')
print(l)
