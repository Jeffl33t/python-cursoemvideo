#Criar um menu
print('\033[1;33mCRIE UM PROGRAMA QUE LEIA 2 NÚMEROS E ABRA UM MENU NA TELA\033[m')

#Receber os valores e a opção do menu
num1 = int(input('Digite o 1° número:'))
num2 = int(input('Digite o 2° número:'))
print('\n[1] SOMAR \n[2] MULTIPLICAR \n[3] MAIOR \n[4] NOVOS NÚMERO \n[5] SAIR\n')
opcao = 0

#Realizar a operação selecionada no menu
while opcao != 5:
    opcao = int(input('Digite sua opção:'))

    if opcao == 1:
        resultado = num1 + num2
        print('{} + {} = {}'.format(num1, num2, resultado))

    elif opcao == 2:
        resultado = num1 * num2
        print('{} x {} = {}'.format(num1, num2, resultado))

    elif opcao == 3:
        maior = num1
        if num2 > maior:
            maior = num2
        print('Maior é {}'.format(maior))

    elif opcao == 4:
        num1 = int(input('Outro número:'))
        num2 = int(input('Mais um:'))

    elif opcao == 5:
        print('Programa terminado.')

    else:
        print('Opção inválida')

