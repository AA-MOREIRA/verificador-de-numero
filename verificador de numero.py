while True: # entra em um loop para nao aceitar um numero que nao seja inteiro
    digitado=input('digite um numero inteiro por favor:')

    if digitado.isdigit(): #verifica se e um digito numerico
        numero= int(digitado)

        if numero%2==0: # se o resto do numero for 0 ele e par
            input('seu numero e par:')

        else:
            print('seu numero e impar:') #caso contrario ele e impar

        break #vai sair do loop so depois de receber um numero inteiro

    else:
        print('incorreto, insira um numero valido:')# se nao for um numero inteiro vai retornar uma mensagem pedindo para digitar um numero inteiro e vai retornar no loop
