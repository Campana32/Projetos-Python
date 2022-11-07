n = int(input('Digite um numero: '))
t = 0
for p in range(1, n + 1):
    if n % p == 0:
        t += 1
if t == 2:
    print('O numero {} é \33[;34mPRIMO\33[m.'.format(n))
else:
    print('O numero {} \33[;31mNÃO\33[m é \33[;31mPRIMO\33[m.'.format(n))