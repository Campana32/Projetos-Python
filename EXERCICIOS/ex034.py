s = int(input('Salario: '))
if s > 1250:
    sa = ((s*10)/100) + s
    print('O salario com o aumento de 10% é de R${}'.format(sa))
else:
    sb = ((s*15)/100) + s
    print('O salario com o aumento de 15% é de R${}'.format(sb))
