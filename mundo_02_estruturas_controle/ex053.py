<<<<<<< HEAD
#Verificar se uma frase é um palíndromo
print('\033[1;34mESCOLHA UMA FRASE PARA SABER SE ELA É OU NÃO UM PALÍNDROMO\033[m\n')

frase = input('Digite a frase á ser analisada:').replace(' ','').lower()
contrario = frase[::-1]

if contrario == frase:
    print('À frase "{}" é um palíndromo.'.format(contrario))

else:
    print('Não é um palíndromo.')

#gabarito
frase = str(input('Digite uma frase:')).strip().upper()
palavra = frase.split()
junto = ''.join(palavra)
inverso = ''

for letra in range(len(junto) -1, -1, -1):
    inverso += junto[letra]

print('O inverso de {} é {}'.format(frase, inverso))

if inverso == frase:
    print('Temos um palíndromo')

else:
    print('Não é um palíndromo')

=======
#Verificar se uma frase é um palíndromo
print('\033[1;34mESCOLHA UMA FRASE PARA SABER SE ELA É OU NÃO UM PALÍNDROMO\033[m\n')

frase = input('Digite a frase á ser analisada:').replace(' ','').lower()
contrario = frase[::-1]

if contrario == frase:
    print('À frase "{}" é um palíndromo.'.format(contrario))

else:
    print('Não é um palíndromo.')

#gabarito
frase = str(input('Digite uma frase:')).strip().upper()
palavra = frase.split()
junto = ''.join(palavra)
inverso = ''

for letra in range(len(junto) -1, -1, -1):
    inverso += junto[letra]

print('O inverso de {} é {}'.format(frase, inverso))

if inverso == frase:
    print('Temos um palíndromo')

else:
    print('Não é um palíndromo')

>>>>>>> db6fe22adc334c96809c710d30b7cd66b02d7359
