from random import randint

#Sortear números e mostrar o menor e o maior entre eles
print('\033[1;34mSORTEIE NÚMEROS E DIGA QUAL É O MAIOR E O MENOR ENTRE ELES\033[m\n')

num = ()
maior = menor = 0

for c in range(0, 5):
    numeros = randint(1, 10)
    lista = list(num)
    lista.append(numeros)
    num = tuple(lista)

    if c == 0 or numeros > maior:
        maior = numeros

    if c == 0 or numeros < menor:
        menor = numeros

print(f'O valores foram {num}')
print(f'\nO maior valor é {maior}')
print(f'O menor valor é {menor}')

#gabarito

numeros = (randint(1, 10), randint(1, 10), randint(1, 10),
           randint(1, 10), randint(1, 10))
print(f'Os números sorteados foram: ', end='')

for n in numeros:
    print(f'{n}', end=' ')

print(f'\nO maior número sorteado foi: {max(numeros)}')
print(f'O menor número sorteado foi: {min(numeros)}')