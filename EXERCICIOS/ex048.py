s = 0
k = 0
for c in range(0, 501, 3):
    if c % 2 == 1:
        k = k + 1
        s = s + c
print('A soma de todos os {} numeros impares, multiplos de 3, entre 1 e 500 é : {}'.format(k, s))
