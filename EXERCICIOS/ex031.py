d = int(input('Distancia da viagem: '))
if d <= 200:
    print('O valor da passagem vai ser de R${}'.format(d * 0.5))
else:
    print('O valor da sua passagem é ser de R${}'.format(d * 0.45))
