n = int(input('Digite um numero: '))
c = 0
f = 1
if n == 0:
    f = 0
else:
    while c != n:
        f *= n - c
        c += 1
print('=== FATORIAL ===')
print('O fatorial de {} é: {}'.format(n, f))
