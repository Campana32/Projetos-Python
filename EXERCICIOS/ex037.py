n = int(input('Digite um numero para a conversão: '))
c = int(input('Selecione qual formato deseja converter: \n (1) Binária \n (2) Octal \n (3) Hexadecimal \n -> '))
if c == 1:
    print('O numero {} convertido para binário é: {}'.format(n, bin(n)[2:]))
elif c == 2:
    print('O numero {} convertido para octal é: {}'.format(n, oct(n)[2:]))
elif c == 3:
    print('O numero {} convertido para hexadecimal é: {}'.format(n, hex(n)[2:]))
else:
    print('Opição invalida. Tente novamente.')
