<<<<<<< HEAD
#Coverter um número
print('\033[1;33mESCREVA UM NÚMERO PARA CONVERTE LO EM BINÁRIO, OCTAL, HEXADECIMAL\033[m\n')

num = int(input('Digite um número:'))
forma = input('Para qual forma voçê quer converter:')
bina = bin(num)
octa = oct(num)
hexa = hex(num)

if forma == 'binario':
    print('O número {} convertido para binário é {}'.format(num, bina[2:]))

elif forma == 'octal':
    print('O número {} convertido para octal é {}'.format(num, octa[2:]))

elif forma == 'hexadecimal':
    print('O número {} convertido para hexadecimal é {}'.format(num, hexa[2:]))

#gabarito
num = int(input('Digite um número inteiro:'))
print('\nEscolha uma das opções para converter:\n'
      '\n[1] Converter para BINÁRIO'
      '\n[2] Converter para OCTAL'
      '\n[3] Converter para HEXADECIMAL')
opcao = int(input('Sua opção: '))

if opcao == 1:
    print('{} Convertido para BINÁRIO é igual a {}'.format(num, bin(num)[2:]))

elif opcao == 2:
    print('{} Convertido para OCTAL é igual a {}'.format(num, oct(num)[2:]))

elif opcao == 3:
=======
#Coverter um número
print('\033[1;33mESCREVA UM NÚMERO PARA CONVERTE LO EM BINÁRIO, OCTAL, HEXADECIMAL\033[m\n')

num = int(input('Digite um número:'))
forma = input('Para qual forma voçê quer converter:')
bina = bin(num)
octa = oct(num)
hexa = hex(num)

if forma == 'binario':
    print('O número {} convertido para binário é {}'.format(num, bina[2:]))

elif forma == 'octal':
    print('O número {} convertido para octal é {}'.format(num, octa[2:]))

elif forma == 'hexadecimal':
    print('O número {} convertido para hexadecimal é {}'.format(num, hexa[2:]))

#gabarito
num = int(input('Digite um número inteiro:'))
print('\nEscolha uma das opções para converter:\n'
      '\n[1] Converter para BINÁRIO'
      '\n[2] Converter para OCTAL'
      '\n[3] Converter para HEXADECIMAL')
opcao = int(input('Sua opção: '))

if opcao == 1:
    print('{} Convertido para BINÁRIO é igual a {}'.format(num, bin(num)[2:]))

elif opcao == 2:
    print('{} Convertido para OCTAL é igual a {}'.format(num, oct(num)[2:]))

elif opcao == 3:
>>>>>>> db6fe22adc334c96809c710d30b7cd66b02d7359
    print('{} Convertido para HEXADECIMAL é igual a {}'.format(num, hex(num)[2:]))