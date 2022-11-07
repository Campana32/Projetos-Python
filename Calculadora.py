print("======= CALCULADORA =======")
while True:
    n1 = float(input('DIGITE O PRIMEIRO NUMERO: '))
    n2 = float(input('DIGITE O SEGUNDO NUMERO: '))
    print("==="*9)
    e = input('ESCOLHA O SINAL DA OPERAÇÃO: \n1 - SOMA \n2 - SUBITRAÇÃO \n3 - DIVISÃO \n4 - MULTIPLICAÇÃo \n => ')
    print("==="*9)
    if e =='1':
        r = (n1 + n2)
        break
    elif e =='2':
        r = (n1 - n2)
        break
    elif e =='3':
        r = (n1 / n2)
        break
    elif e =='4':
        r = (n1 * n2)
        break
    else:
        print("ALTERNATIVA INVALIDA!\nTENTE NOVAMENTE!")
        print("==="*9)
print(f"RESPOSTA = {r}")
print("==="*9)
