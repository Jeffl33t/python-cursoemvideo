#Criar uma lista - Armazenar números digitados pelo teclado
#                - Impedir que números se repitam
#                - Organizar os números em ordem crescente
valores = []
opcao = ' '

while opcao not in 'Nn':
    num = int(input('Digite um valor:'))

    if num not in valores:
        valores.append(num)

    else:
        print('Valor duplicado. Tente novamente')

    opcao = str(input('Continuar [S/N]'))

valores.sort()
print(valores)
