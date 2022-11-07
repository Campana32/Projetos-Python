a = b = c = 0
l = 1
while True:
    i = int(input(f'Digite a idade da {l} pessoa: '))
    s = str(input(f'Digite o sexo da {l} pessoa [H/M]: ')).strip().upper()[0]
    l += 1
    if i > 18:
        a += 1
    if s == 'H':
        b += 1
    if s == 'M' and i < 20:
        c += 1
    if s != 'M' and s != 'H':
        print('ERRO!\nALTERNATIVA INVALIDA')
        break
    r = str(input('Deseja cadastrar mais alguem [S/N]?')).strip().upper()[0]
    if r == 'N':
        break
print('-=-'*13)
print(f'Resultado dos cadastros: \nPessoas com mais de 18 anos: {a} \nTotal de homens registrados: {b} '
      f'\nMulheres com menos de vinte anos: {c}')
print('-=-'*13)
