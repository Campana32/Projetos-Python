v = float(input('Valor da casa: R$'))
s = float(input('Salario do comprador: '))
t = float(input('Quantos anos o valor sera pago: '))
p = v / (t * 12)
d = (s*30) / 100
a = p - d
if a > 0:
    print('Desculpe, mas não será possivel efetuarmos a compra, '
          'pois a prestação mensal de {:.2f} ultrapassa o valor de 30% do salario informado.'.format(p))
elif a <= 0:
    print('O valor da prestação mensal sera de aproximadamente R$:{:.2f}.\n'
          'Levando em conta o valor salarial informado, a compra do imovel foi aprovado. Parabéns!'.format(p))
