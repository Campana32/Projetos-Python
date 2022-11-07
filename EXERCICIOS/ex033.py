n1 = int(input('Diga um numero:'))
n2 = int(input('Diga outra numero:'))
n3 = int(input('Diga mais um nuemro:'))
me = n1
if n2 < n1 and n2 < n3:
    me = n2
if n3 < n2 and n3 < n1:
    me = n3
ma = n1
if n2 > n1 and n2 > n3:
    ma = n2
if n3 > n1 and n3 > n2:
    ma = n3
print('O menor numero é {}, e o maior é {}.'.format(me, ma))
