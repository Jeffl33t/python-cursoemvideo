<<<<<<< HEAD
#Somar valores exceto o número usado como condição de parada
soma = cont = 0

while True:
    num = int(input('Digite um número (999 PARAR):'))

    if num == 999:
        break

    cont += 1
    soma += num

=======
#Somar valores exceto o número usado como condição de parada
soma = cont = 0

while True:
    num = int(input('Digite um número (999 PARAR):'))

    if num == 999:
        break

    cont += 1
    soma += num

>>>>>>> db6fe22adc334c96809c710d30b7cd66b02d7359
print(f'Voçê digitou {cont} números e a soma é {soma}')