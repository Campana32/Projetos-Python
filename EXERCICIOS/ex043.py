p = float(input('Digite seu peso (Kg): '))
a = float(input('Digite sua altura (M): '))
m = p / (a * a)
if m < 18.5:
    print('Seu imc é {:.1f}, você esta abaixo do peso.'.format(m))
elif 18.5 <= m < 25:
    print('Seu imc é {:.1f}, seu peso esta ideal.'.format(m))
elif 25 <= m < 30:
    print('Seu imc é {:.1f}, seu esta na faixa de sobre peso.'.format(m))
elif 30 <= m < 40:
    print('Seu imc é {:.1f}, você esta na faixa de obesidade.'.format(m))
else:
    print('Seu imc é {:.1f}, você esta na faixa de obesidade morbida. Cuidado!'.format(m))
