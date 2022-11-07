v = float(input('Valor do produto: '))
f = int(input('Escolha a forma de pagamento: \n(1) A vista dinheiro/cheque. \n(2) A vista no cartao. '
              '\n(3) Em 2x no cartao.\n(4) Em 3x no cartao. \n->'))
if f == 1:
    d1 = (v * 10) / 100
    d2 = v - d1
    print('Ao pagar a vista você tera 10% de desconto, o valor final da sua compra é de R${:.2f}.'.format(d2))
elif f == 2:
    c1 = (v * 5) / 100
    c2 = v - c1
    print('Ao pagar a vista no cartao você tera 5% de desconto, o valor final da sua compra é de R${:.2f}.'.format(c2))
elif f == 3:
    d = v / 2
    print('Ao pagar em 2x no cartao você não tera juros, o valor de cada parcela é de R${:.2f}.'.format(d))
elif f == 4:
    j1 = (v * 20) / 100
    j2 = v + j1
    j3 = j2 / 3
    print('Ao pagar em 3x no cartao você tera 20% de juros, o valor de cada parcela é de R${:.2f}.'.format(j3))
