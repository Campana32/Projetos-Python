# an = a1 +(n-1) x r
a1 = int(input('Digite o primeiro termo: '))
r = int(input('Digite a razão: '))
print('== PROGRESSÂO ARITIMEDICA ==')
for n in range(1, 11):
    an = a1 + (n-1) * r
    print('== {} =='.format(an))
