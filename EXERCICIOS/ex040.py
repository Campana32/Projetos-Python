n1 = float(input('Digite a primeira nota: '))
n2 = float(input('Digite a segunda nota: '))
m = (n1 + n2) / 2
if m < 5:
    print('Sua media foi {:.1f}, você esta reprovado.'.format(m))
elif 5 <= m < 7:
    print('Sua media foi {:.1f}, você esta de recuperação.'.format(m))
elif m >= 7:
    print('Parabens, sua media foi {:.1f}, você esta aprovado!'.format(m))
