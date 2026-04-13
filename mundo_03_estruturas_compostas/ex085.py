# Criar uma lista com duas listas dentro
    # Armazenar os números pares em uma das listas
    # Armazenar os números ímpares na outra
    # Mostrar as listas em ordem crescente
par = list()
impar = list()
resultado = list()

for c in range(0, 7):
    numero = int(input(f'Digite o número {c}°: '))
    if numero % 2 == 0:
        par.append(numero)

    else:
        impar.append(numero)

par.sort()
impar.sort()
resultado.append(par)
resultado.append(impar)

print(resultado)

# Gabarito
numeros = [[], []]
num = 0

for c in range(0, 7):
    num = (int(input(f'Digite número {c}: ')))
    if num % 2 == 0:
        numeros[0].append(num)

    else:
        numeros[1].append(num)

numeros[0].sort()
numeros[1].sort()

print(f'Todos os valores pares são {numeros[0]}.')
print(f'Todos os valores ímpares são {numeros[1]}.')
print(f'Todos os valores {numeros}')