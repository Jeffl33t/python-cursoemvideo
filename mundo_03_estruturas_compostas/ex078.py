#Verificar a posição do maior e do menor valor digitados
valores = []
for v in range(0, 5):
    valores.append(int(input(f'Digite o valor {v}:')))

maior = max(valores)
menor = min(valores)
print(f'Voçê digitou os valores: {valores}')
print(f'O maior valor é {maior} na posição ', end='')

for pos, valor in enumerate(valores):
    if valor == maior:
        print(f'{pos}', end='... ')

print(f'\nO menor valor é {menor} na posição ', end='')
for pos, valor in enumerate(valores):
    if valor == menor:
        print(f'{pos}', end='... ')
