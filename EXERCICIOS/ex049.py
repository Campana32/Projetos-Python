from time import sleep
n = int(input('Digite um numero: '))
print('===TABUADA DO {}==='.format(n))
for c in range(1, 11):
    s = c * n
    print('== {} =='.format(s))
    sleep(0.3)
