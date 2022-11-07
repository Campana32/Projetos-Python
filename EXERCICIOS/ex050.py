s = 0
c = 0
for n in range(1, 7):
    n1 = int(input('Digite o {} numero:'.format(n)))
    if n1 % 2 == 0:
        s += n1
        c += 1
print("A soma dos {} igitos pares é {}.".format(c, s))
