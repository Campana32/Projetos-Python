from random import randint
j = int(input('=== JOKENPÔ === \n(0) PEDRA \n(1) PAPEL \n(2) TESOURA \n'
              'Escolha o numero respectivo ao objeto que você deseja jogar: \n->'))
i = ('Pedra', 'Papel', 'Tesoura')
c = randint(0, 2)
k = input('Você esta pronto?')
print('-=-' * 8)
print('Computador: {}'.format(i[c]))
print('Jogador: {}'.format(i[j]))
print('-=-' * 8)
if c == 0:
    if j == 0:
        print('EMPATE')
    if j == 1:
        print('GANHOU')
    if j == 2:
        print('PERDEU')
if c == 1:
    if j == 0:
        print('PERDEU')
    if j == 1:
        print('EMPATE')
    if j == 2:
        print('GANHOU')
if c == 2:
    if j == 0:
        print('GANHOU')
    if j == 1:
        print('PERDEU')
    if j == 2:
        print('EMPATE')
