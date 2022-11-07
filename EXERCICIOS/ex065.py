f = 1
s = q = ma = me = 0
while f != 0:
    n = int(input('Digite um \33[:36mNUMERO\33[m: '))
    s += n
    q += 1
    if ma == me == 0:
        ma = n
        me = n
    if ma < n:
        ma = n
    if me > n:
        me = n
    r = str(input('Quer \33[:35mCONTUNUAR\33[m? ')).strip().upper()[0]
    if r == 'S':
        print('Proximo digito:')
    if r == 'N':
        f = 0
    if r != 'S' and r != 'N':
        print('Resposta invalida, tente novamente.')
        r = str(input('Quer continuar? ')).strip().upper()[0]
m = s / q
print('===' * 10)
print('De acordo com os dados: \n\33[:32mMedia dos valores: {}\33[m '
      '\n\33[:34mMenor valor: {}\33[m \n\33[:31mMaior valor: {}\33[m'.format(m, me, ma))
print('===' * 10)
