n1 = int(input('Primeira reta: '))
n2 = int(input('Segunda reta: '))
n3 = int(input('Terceira reta: '))
ma = n1
if n2 > n1 and n2 > n3:
    ma = n2
if n3 > n1 and n3 > n2:
    ma = n3
if n1 == ma:
    a = n2
    b = n3
if n2 == ma:
    a = n1
    b = n3
if n3 == ma:
    a = n1
    b = n2
r = ma - (a + b)
if r > 0:
    print('Não podera ser feito um trianglo.')
if r < 0 or r == 0:
    print('Podera ser feito um tiangulo.')
if r == 0:
    print('parabens um triangulo perfeito ;>')
