#Mostrar por extenso um número digitado
numeros = ('zero', 'um', 'dois', 'três', 'quatro', 'cinco', 'seis', 'sete', 'oito', 'nove', 'dez')
opcao = ' '

while opcao not in 'Nn':
    while True:
        num = int(input('Digite um número entre 0 e 10:'))

        if 0 <= num <= 10:
            print(f'Voce digitou o numero {num}, por extenso {numeros[num]}')
            break

        else:
            print('Tente novamente. ', end='')

    opcao = str(input('Continuar [S/N]:'))

print('Programa Terminado')





