print('----- RADAR ELETRONICO -----')
v = int(input('Velocidade: '))
m = (v - 80) * 12
if v > 80:
    print('Você foi multado por excesso de velocidade. \nA velocidade permitida era de 80 Km/h e você estava a {}Km/h. '
          '\nO valor da sua multa sera de R$:{},00'.format(v, m))
elif v == 80:
    print('Você esta no limita da velocidade, cuidado!')
else:
    print('Você esta dentro da velocidade permitada, continue assim.')
