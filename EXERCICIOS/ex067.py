s = 1
while True:
    n = int(input('Quer ver a tabuada de qual valor? '))
    if n >= 0:
        print('---'*9)
        while s < 11:
            t = n * s
            s += 1
            print(f'--{t}--')
        print('---'*9)
    if n < 0:
        break
    s = 1
print('Programa encerrado. Valor invalido.')
