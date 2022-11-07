l = 1
tg = pc = 0
nb = pb = ''
while True:
    n = str(input(f'Digite o nome do {l} produto: '))
    p = float(input(f'Digite o preço do {l} produto: '))
    l += 1
    tg += p
    if p > 1000:
        pc += 1
    if pb == '':
        pb = p
    if nb == '':
        nb = n
    if pb > p:
        nb = n
    r = str(input('Quer cadastrar mais produtos [S/N]:')).strip().upper()[0]
    if r == 'N':
        break
    if r != 'N' and r != 'S':
        print('ERRO!\nALTERNATIVA INVALIDA!')
        r = str(input('Quer cadastrar mais produtos [S/N]:')).strip().upper()[0]
print('====='*10)
print(f'Resultado da lista: \nTotal gasto: {tg} '
      f'\nProdutos mais acima de R$1000: {pc} '
      f'\nProduto mais barato: {nb}')
print('====='*10)