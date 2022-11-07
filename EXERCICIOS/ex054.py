from datetime import date
t = 0
for r in range(1, 8):
    a = int(input('DIGITE O \33[:32mANO DE NACIMENTO\33[m DA {} PESSOA: '.format(r)))
    s = date.today().year - a
    if s >= 21:
        t += 1
print('DAS 7 PESSOAS:\n-> \33[:34mSão MAIORES de 21 anos:\33[m {} '
      '\n-> \33[:31mSão MENORES de 21 anos:\33[m {}'.format(t, 7 - t))

