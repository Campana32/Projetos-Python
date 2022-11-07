s = ''
while s != 'M' and s != 'F':
    s = str(input('DIgite seu genero [M/F]: ')).strip().upper()[0]
    if s != 'M' and s != 'F':
        print('===' * 10)
        print('Resposta invalida! \nTente novamente!')
        print('===' * 10)
if s == 'F':
    print('===' * 10)
    print('Resposta computada, sexo FEMININO.')
elif s == 'M':
    print('===' * 10)
    print('Resposta computada, sexo MASCULINO.')
