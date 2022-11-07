v = s = 0
while True:
    n = int(input(f'Digite o {v} numero (digite 999 para parar): '))
    if n == 999:
        break
    s += n
    v += 1
print(f'A soma dos {v} valores, é igual a {s}.')
