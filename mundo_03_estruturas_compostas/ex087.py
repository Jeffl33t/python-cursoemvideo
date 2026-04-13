# Criar uma matriz, inserir valores e manipular os valores
matriz = [[0, 0, 0],[0, 0, 0],[0, 0, 0]]
soma = soma3 = maior = 0

# Receber os valores
for l in range(0, 3):
    for c in range(0, 3):
        matriz[l][c] = int(input(f'Digite o número [{l}, {c}]: '))

        # Somar todos os valores pares
        if matriz[l][c] % 2 == 0:
            soma += matriz[l][c]

        # Somar todos os valores da terceira coluna
        if matriz[l][2]:
            soma3 += matriz[l][2]

        # Verificar o maior valor da linha 1
        if matriz == matriz[1][c]:
            maior = matriz[1][c]

        else:
            if matriz[1][c] > maior:
               maior = matriz[1][c]

# Mostrar a matriz
for l in range(0, 3):
    for c in range(0, 3):
        print(f'[{matriz[l][c]:^5}]', end='')
    print()

print(f'A soma dos valores pares é {soma}.')
print(f'A soma dos valores da terceira coluna é {soma3}.')
print(f'O maior valor da linha 1 é {maior}')


