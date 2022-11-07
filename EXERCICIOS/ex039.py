from datetime import date
n = int(input('Ano de nacimento: \n->'))
s = int(input('Genero: \n(1) Homem \n(2) Mulher \n->'))
l = date.today().year - n
g = l - 18
h = 18 - l
if s == 1:
    if l == 18:
        print('você complata 18 anos esse anos, esta na hora de se alistar para o serviço militar.')
    elif l > 18:
        if g == 1:
            print('Você ja completou 18 anos, esta em divida com o serviço militar a 1 ano.')
    elif g > 1:
        print('Você ja completou 18 anos, esta em divida com o serviço militar a {} anos.'.format(g))
    else:
        if h == 1:
            print('Falta apenas um ano para você se alistar para o serviço militar obrigatorio.')
        elif h > 1:
            print('Faltam {} anos para você se alistar para o serviço militar obrigatorio.'.format(h))
elif s == 2:
    print('Você não tem que se alistar para o serviço militar.')
else:
    print('Resposta invalida! \nTente novamete.')
