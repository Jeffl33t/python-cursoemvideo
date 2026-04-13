#Criar uma lista - Armazenar os números em ordem crescente
#                - Mostrar a posição do número no momento em que é digitado
valores = []

for v in range(0, 5):
    num = int(input(f'Digite o valor {v}:'))

    if v == 0 or num > valores[-1]:
        valores.append(num)
        print('Valor adicionado ao final da lista...')

    else:
        pos = 0

        while pos < len(valores):
            if num <= valores[pos]:
                valores.insert(pos, num)
                print(f'Valor adicionado a posição {pos}')
                break

            pos += 1

print(f'Os valores digitados em ordem {valores}')

