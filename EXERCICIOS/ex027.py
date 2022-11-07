n = str(input('Digite seu nome completo: '))
u = n.rfind(' ')
s = (u + 1)
a = n[s:]
l = n.find(' ')
b = n[:l]
print('O primeiro nome é: {} \nO ultimo nome é: {}'.format(b, a))
