from time import sleep
a1 = int(input('\33[:30mDigite o \33[:36mPRIMEIRO\33[m \33[:30mtermo: '))
r = int(input('Digite a \33[:36mRAZÃO\33[m\33[:30m: '))
n = 1
t = 1
print('\33[:31m== PROGUESÃO ARITIMEDICA ==\33[m')
while t != 0:
    while n != 10 + t:
        an = a1 + (n - 1) * r
        n += 1
        print('\33[:34m== {} ==\33[m'.format(an))
        sleep(0.2)
    a = str(input('\33[:30mQuer mais termos:\33[m ')).strip().upper()[0]
    if a == 'S':
        t += int(input('\33[:30mQuantos termos a mais:\33[m '))
    elif a == 'N':
        t = 0
print('\33[:30mENCERRANDO...'), sleep(1.5)
print('PROGRAMA FINALIZADO.\33[m')
