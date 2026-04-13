#Separar valores ímpares e pares em duas listas
valores = []
pares = []
impares = []

while True:
    valores.append(int(input('Digite um valor:')))
    opcao = ' '
    while opcao not in 'SsNn':
        opcao = str(input('Continuar [S/N]:'))

    if opcao in 'Nn':
        break

for valor in valores:
    if valor % 2 == 0:
        pares.append(valor)

    else:
        impares.append(valor)

print(f'Valores digitados {valores}')
print(f'Valores pares digitados {pares}')
print(f'Valores ímpares digitados {impares}')