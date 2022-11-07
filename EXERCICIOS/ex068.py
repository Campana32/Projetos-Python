from random import randint
nm = randint(0, 10)
g = 0
print('-=-'*10)
print('        PAR ou IMPAR')
print('-=-'*10)
while True:
    np = int(input('Digite um numero de 0 a 10: '))
    pi = str(input('Escola entre Par ou Impar [P/I]: ')).strip().upper()[0]
    s = (np + nm)
    n = s % 2
    if pi == 'I':
        if n == 0:
            print(f'Voce perdeu! \nComputador: {nm} \nJogador: {np} \nSoma: {s} \nVoce ganhou {g} vezes seguidas.')
            break
        if n > 0:
            print(f'Voce GANHOU! \nComputador: {nm} \nJogador: {np} \nSoma: {s} ')
            g += 1
    if pi == 'P':
        if n == 0:
            print(f'Voce GANHOU! \nComputador: {nm} \nJogador: {np} \nSoma: {s} ')
            g += 1
        if n > 0:
            print(f'Voce perdeu! \nComputador: {nm} \nJogador: {np} \nSoma: {s} \nVoce ganhou {g} vezes seguidas.')
            break
print('Vamos jogar de novo?')