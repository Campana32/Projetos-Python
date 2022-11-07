import random
a = str(input('Nome do primeiro aluno: '))
b = str(input('Nome do segundo aluno: '))
c = str(input('Nome do terceiro aluno: '))
d = str(input('Nome do quarto aluno: '))
lista = [a, b, c, d]
escolhido = random.choices(lista)
print('O aluno escolido foi {}'.format(escolhido))
