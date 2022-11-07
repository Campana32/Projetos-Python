ma = 0
me = 0
for v in range(1, 6):
    c = float(input('Digite o \33[:35mPESO\33[m da {}ª pessoa: '.format(v)))
    if c > ma:
        ma = c
    if c < ma and c < me:
        me = c
    if me == 0:
        me = c
print('=='*15)
print('\33[:32mDENTRE OS PESSOS DIGITADOS:\33[m\n'
      '\33[:31mO MAIOR PESO:\33[m {}Kg \n'
      '\33[:34mO MENOS PESO:\33[m {}Kg'.format(ma, me))
