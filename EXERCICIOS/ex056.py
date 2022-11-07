ih = 0
m = 0
t = 0
for x in range(1, 5):
    s = int(input('Selecione o \33[:30mSEXO\33[m da {} pessoa: \n(1) \33[:34mHOMEM\33[m \n(2) \33[:31mMULHER\33[m \n-> '.format(x)))
    n = str(input('Digite o \33[:35mNOME\33[m da {} pessoa: '.format(x)))
    i = int(input('Digite a \33[:32mIDADE\33[m da {} pessoa: '.format(x)))
    m += i
    if s == 1 and i > ih:
        ih = i
        nh = n
    # if s == 1 and i == ih:
    elif s == 2 and i < 20:
        t += 1
md = m / 4
print('==='*15)
print("""\33[:30mDE ACORDO COM OS DADOS COMPUTADOS:\33[m
-> \33[:32mMEDIA DA IDADE:\33[m {}
-> \33[:34mHOMEM MAIS VELHO:\33[m {}
-> \33[:31mQUANTIDADE DE MULHERES COM MENOS DE 20 ANOS:\33[m {}""".format(md, nh, t))
