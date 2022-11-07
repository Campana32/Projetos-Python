# an = a1 +(n-1) * r
a1 = int(input('Digite o primeiro termo: '))
r = int(input('Digite a razão: '))
n = 1
print('\33[:31m== PROGUESÃO ARITIMEDICA ==\33[m')
while n != 11:
    an = a1 + (n - 1) * r
    n += 1
    print('\33[:34m== {} ==\33[m'.format(an))
