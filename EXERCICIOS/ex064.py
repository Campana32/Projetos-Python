q = s = n = 0
print('=== CONTADOR === \nDigite o numero 999 para encerar.')
while n != 999:
    n = int(input('Digite o {} numero: '.format(q + 1)))
    q += 1
    s += n
if q > 2:
    print('Forna digitados um total de {} numeros e a soma deles é igual a {}.'.format(q - 1, s - 999))
else:
    print('Foi digitado {} numero e o valor dele é {}'.format(q - 1, s - 999))
