# Cadastrar pessoas e análisar os pesos
dados = []
pesos = []
maior = menor = 0

# Receber os dados
while True:
    dados.append(str(input('Digite seu nome: ')))
    dados.append(int(input('Digite seu peso: Kg')))

    # Verificar o menor e maior peso
    if len(pesos) == 0:
        maior = menor = dados[1]

    else:

        if dados[1] > maior:
            maior = dados[1]

        if dados[1] < menor:
            menor = dados[1]

    pesos.append(dados[:])
    dados.clear()
    opcao = (str(input('Continuar [S/N]: ')))
    if opcao in 'Nn':
        break

# Retorna quantidade de pessoas cadastradas
print(f'Pessoas cadastradas {len(pesos)}')

# Retorna o maior peso e o nome da pessoa
print(f'O maior peso é {maior}Kg. Peso de ', end='')
for p in pesos:
    if p[1] == maior:
        print(f'{p[0]}', end=' ')
print()

# Retorna o menor peso e o nome da pessoa
print(f'O menor peso é {menor}Kg. Peso de ', end='')
for p in pesos:
    if p[1] == menor:
        print(f'{p[0]}', end=' ')
