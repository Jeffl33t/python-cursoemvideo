from time import sleep
from random import randint


# Criar uma função para sortear números
def sorteio(* num):
    print('Sorteando 5 valores:', end=' ')

    for c in range(0, 5):
        numeros.append(randint(1, 9))

    for v in numeros:
        print(f'{v}', end=' ')
        sleep(0.5)

    print('PRONTO!')


# Criar uma função que some os números pares
def somapar():
    soma = 0

    for v in numeros:
        if v % 2 == 0:
            soma += v

    print(f'Somando valores pares de {numeros}, temos {soma}')

# Programa principal
numeros = list()
sorteio(numeros)
somapar()