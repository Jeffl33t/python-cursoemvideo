#Somar valores exceto o número usado como condição de parada
contador = 0
numero = 0
soma = 0

while numero != 999:
    numero = int(input('Digite um número:'))
    contador += 1

    if numero != 999:
        soma += numero

print('Voce digitou {} números e a soma total é {}'.format(contador - 1, soma))


