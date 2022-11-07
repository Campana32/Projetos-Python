n1 = int(input('Primeira reta: '))
n2 = int(input('Segunda reta: '))
n3 = int(input('Terceira reta: '))
m = n1
if n2 > n1 and n2 > n3:
    m = n2
if n3 > n1 and n3 > n2:
    m = n3
if m == n1:
    a = n2
    b = n3
if m == n2:
    a = n1
    b = n3
if m == n3:
    a = n1
    b = n2
r = (a + b) - m
if r < 0:
    print('Não posse ser feito um triangulo com essas tres retas.')
if r >= 0:
    if a == b and a == m:
        print('O triangulo formado por esses tres lados é um triangulo EQUILATERO.')
    elif a == b != m or b == m != a or a == m != b:
        print('O triangulo formado por esses tres lados é um triangulo ISOCELES.')
    elif a != b != m != a:
        print('O triangulo formado por esses tres lados é um triangulo ESCALENO.')
