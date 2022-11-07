n1 = float(input('Digite o \33[:30mPRIMEIRO\33[m valor: '))
n2 = float(input('Digite o \33[:30mSEGUNDO\33[m valor: '))
o = int(input('\33[:30m==CALCULADORA==\33[m\n\33[:31m[1] SOMAR\33[m\n\33[:33m[2] MULTIPLICAR\33[m'
              '\n\33[:34m[3] MAIOR VALOR\33[m\n\33[:35m[4] NOVOS NUMEROS\33[m'
              '\n\33[:36m[5] SAIR DO PROGRAMA\33[m\n->'))
while o != 5:
    if o == 1:
        print('\33[:30m===\33[m'*10)
        print('\33[:31mRESULTADO:\33[m')
        print('\33[:34m{} + {} = {}\33[m'.format(n1, n2, n1 + n2))
        print('\33[:30m===\33[m'*10)
        o = int(input('\33[:30m==CALCULADORA==\33[m\n\33[:31m[1] SOMAR\33[m\n\33[:33m[2] MULTIPLICAR\33[m'
                      '\n\33[:34m[3] MAIOR VALOR\33[m\n\33[:35m[4] NOVOS NUMEROS\33[m'
                      '\n\33[:36m[5] SAIR DO PROGRAMA\33[m\n->'))
    if o == 2:
        print('\33[:30m===\33[m'*10)
        print('\33[:31mRESULTADO:\33[m')
        print('\33[:34m{} * {} = {}\33[m'.format(n1, n2, n1 * n2))
        print('\33[:30m===\33[m'*10)
        o = int(input('\33[:30m==CALCULADORA==\33[m\n\33[:31m[1] SOMAR\33[m\n\33[:33m[2] MULTIPLICAR\33[m'
                      '\n\33[:34m[3] MAIOR VALOR\33[m\n\33[:35m[4] NOVOS NUMEROS\33[m'
                      '\n\33[:36m[5] SAIR DO PROGRAMA\33[m\n->'))
    if o == 3:
        print('\33[:30m===\33[m'*10)
        print('\33[:31mRESULTADO:\33[m')
        if n1 > n2:
            print('O \33[:31mMAIOR\33[m numero é \33[:31m{}\33[m'.format(n1))
        if n1 < n2:
            print('O \33[:31mMAIOR\33[m numero é \33[:31m{}\33[m'.format(n2))
        if n1 == n2:
            print('Os \33[:34mDOIS\33[m numeros são \33[:34mIGUAIS\33[m.')
        print('\33[:30m===\33[m'*10)
        o = int(input('\33[:30m==CALCULADORA==\33[m\n\33[:31m[1] SOMAR\33[m\n\33[:33m[2] MULTIPLICAR\33[m'
                      '\n\33[:34m[3] MAIOR VALOR\33[m\n\33[:35m[4] NOVOS NUMEROS\33[m'
                      '\n\33[:36m[5] SAIR DO PROGRAMA\33[m\n->'))
    if o == 4:
        n1 = float(input('Digite o \33[:30mPRIMEIRO\33[m valor: '))
        n2 = float(input('Digite o \33[:30mSEGUNDO\33[m valor: '))
        o = int(input('\33[:30m==CALCULADORA==\33[m\n\33[:31m[1] SOMAR\33[m\n\33[:33m[2] MULTIPLICAR\33[m'
                      '\n\33[:34m[3] MAIOR VALOR\33[m\n\33[:35m[4] NOVOS NUMEROS\33[m'
                      '\n\33[:36m[5] SAIR DO PROGRAMA\33[m\n->'))
    else:
        print('\33[:31mOPÇÃO INVALIDA! TENTE NOVAMENTE:\33[m')
        o = int(input('\33[:30m==CALCULADORA==\33[m\n\33[:31m[1] SOMAR\33[m\n\33[:33m[2] MULTIPLICAR\33[m'
                      '\n\33[:34m[3] MAIOR VALOR\33[m\n\33[:35m[4] NOVOS NUMEROS\33[m'
                      '\n\33[:36m[5] SAIR DO PROGRAMA\33[m\n->'))
print('\33[:30m===\33[m'*10)
print('\33[:30mENCERRANDO...\33[m')
print('\33[:30m===\33[m'*10)
