#Somar valores exceto o número usado como condição de parada
soma = cont = 0

while True:
    num = int(input('Digite um número (999 PARAR):'))

    if num == 999:
        break

    cont += 1
    soma += num

print(f'Voçê digitou {cont} números e a soma é {soma}')