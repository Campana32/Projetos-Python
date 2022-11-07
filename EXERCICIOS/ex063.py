from time import sleep
n = int(input('Digite a quantidade de termos desejado: '))
t1 = 0
t2 = 1
c = 3
print('===' * 10)
print('\33[:36m-> FIBONACCI <-'), sleep(0.3)
print('= {} ='.format(t1)), sleep(0.3)
print('= {} ='.format(t2)), sleep(0.3)
while c < n + 1:
    t3 = t1 + t2
    t1 = t2
    t2 = t3
    c += 1
    print('\33[:36m= {} =\33[m'.format(t3)),sleep(0.3)
print('===' * 10)
