#Análisando números digitados no teclado
num1 = int(input('Digite um número:'))
num2 = int(input('Digite mais um número:'))
num3 = int(input('Digite outro número:'))
num4 = int(input('Digite o ultimo número:'))
numeros = (num1, num2, num3, num4)

#Mostrar números digitados
print('Números digitados: ', end='')
for n in numeros:
    print(f'{n}', end=' ')

#Contar a quantidade vezes que os números 9 e 3 foram digitados
tres = numeros.count(3)
nove = numeros.count(9)
lista = []

#Verificar se o número 9 foi ou não digitado
if nove != 0:
    print(f'\nVezes que o número 9 foi digitado {nove}.')

else:
    print('\nO número nove não foi digitado.')

#Verificar se o número 3 foi digitado e qual a primeira ocorrência
if tres != 0:
    tres = numeros.count(3) + 1
    print(f'O número três foi digitado pela primeira vez na posição {tres} ')

else:
    print('O valor tres nao foi digitado em nenhuma posição')

#Verificar se foram digitados números pares
for pares in numeros:
    if pares % 2 == 0:
        lista.append(pares)

if len(lista) != 0:
    print(f'Número(s) par(es) digitado(s): ', end='')

    for n in lista:
        print(f'{n}', end=' ')

else:
    print('Não foi digitado nenhum número par')

#gabarito

"""num = (int(input('Digite um número:')),
       int(input('Digite mais um número:')),
       int(input('Digite outro número:')),
       int(input('Digite o ultimo número:')))
print('Números digitados: ', end='')

for n in num:
    print(f'{n}', end=' ')

if 9 in num:
    print(f'\nO número nove foi digitado: {num.count(9)} vez(es).')

else:
    print('O número nove não foi digitado.')

if 3 in num:
    print(f'O número três foi digitado pela primeira vez na posição {num.index(3) + 1}.')

else:
    print('O número três não foi digitado.')

print('Os valores pares digitados foram: ', end='')

for pares in num:
    if pares % 2 == 0:
        print(f'{pares}', end=' ')"""



