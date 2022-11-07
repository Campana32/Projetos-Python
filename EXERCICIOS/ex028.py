from random import randint
n = randint(0, 5)
print('Adivinhe qual foi o numero que eu escolhi de 0 a 5!')
e = int(input('Numero: '))
if e == n:
    print('Parabéns! Você acertou!')
else:
    print('Não foi dessa vez! Tente de novo!')
