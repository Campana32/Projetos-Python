from random import randint
n = randint(0, 10)
r = int(input('== \33[:32mADIVINHE O NUMERO\33[m =='
              '\nENTRE \33[:33m0\33[m A \33[:33m10\33[m\n->'))
t = 1
while r != n:
    print('\33[:31mERRADO!\33[m')
    r = int(input('Tente novamente: \n->'))
    t += 1
print('\33[:34mCORRETO!\33[m '
      '\nEra o numero \33[:33m{}\33[m. '
      '\nVocê precisou de \33[:35m{}\33[m tentativas para acertar.'.format(n, t))
