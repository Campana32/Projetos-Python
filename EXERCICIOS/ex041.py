from datetime import date
n = int(input('Digite a idade do atleta: '))
i = date.today().year - n
if i <= 9:
    print('A idade desse atleta é {} anos, ele esta na categoria mirim.'.format(i))
elif i <= 14:
    print('A idade desse atleta é {} anos, ele esta na categoria infantil.'.format(i))
elif i <= 19:
    print('A idade desse atleta é {} anos, ele esta na categoria junior.'.format(i))
elif i <= 25:
    print('A idade desse atleta é {} anos, ele esta na categoria senior.'.format(i))
else:
    print('A idade desse atleta é {} anos, ele esta na categoria master.'.format(i))
