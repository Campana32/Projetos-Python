f = str(input('Digite a frase: '))
f1 = f.split()
f2 = ''.join(f1)
cf = len(f2)
s = str()
for r in range(cf, -1, -1):
    s += f2[r: r + 1]
if f2 == s:
    print('A frase: {}, é \33[:34mPOLINDROMA\33[m!'.format(f))
elif f2 != s:
    print('A frase: {}, \33[:31mNÃO\33[m é \33[:31mPOLINDROMA\33[m!'.format(f))
