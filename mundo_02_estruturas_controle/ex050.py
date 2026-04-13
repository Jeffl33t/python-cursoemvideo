#Somar apenas os números pares
print('\033[1;34mDIGITE 6 NÚMERO PARA SOMAR APENAS OS NÚMEROS PARES\033[m\n')

soma = 0
cont = 0

for c in range(1, 7):
    n = int(input('Digite o {} número:'.format(c)))
    if n % 2 == 0:
        cont += 1
        soma += n

print('Você digitou {} números pares e a soma deles é {}'.format(cont, soma))
