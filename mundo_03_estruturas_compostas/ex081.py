#Criar uma lista de números
valores = []
alvo = 5

#Receber os números e adicionar a lista
while True:
    valores.append(int(input('Digite um número:')))
    opc = ' '

    while opc not in 'SsNn':
        opc = str(input('Continuar [S/N]:'))

    if opc in 'Nn':
        break

#Ordenar e mostrar a lista em ordem decrescente
valores.sort(reverse=True)
print(f"valores em ordem decrescente são {valores}")

#Verificar se o alvo está na lista, se sim mostrar a posição
if alvo in valores:
    print(f'O cinco esta na lista na posição ', end='')

    for pos, valor in enumerate(valores):
        if valor == alvo:
            print(f'{pos}...', end='')
    print()

else:
    print('O cinco não esta na lista')

print(f'Números digitados {len(valores)}')
