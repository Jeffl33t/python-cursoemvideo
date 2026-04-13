from random import randint
from time import sleep


# Criar bilhetes da loteria
print('-'* 30)
print(f'{'JOGA NA MEGA SENA':^30}')
print('-' * 30)

# Receber a quantidade de jogos a serem gerados
jogo = int(input('Quantos jogos voce quer: '))
print(f'{f'\n-=-=-= SORTEANDO {jogo} JOGOS =-=-=-':^30}')

# Sortear os números
for j in range(1, jogo + 1):
    sorteio = []
    sleep(0.8)

    # Sortear os números para cada jogo
    for s in range(0, 6):
        while len(sorteio) != 6:
            numeros = randint(1, 60)

            # Verificar para que o número não se repita dentro do mesmo jogo
            if numeros not in sorteio:
                sorteio.append(numeros)

    # Organiza os números sorteados em ordem crescente
    sorteio.sort()
    print(f'Jogo {j}: {sorteio}')

print(f'{'-=-=-=-= < BOA SORTE! > =-=-=-=-':^30}')

#Verão 2

# Receber a quantidade de jogos a serem gerados
lista = []
jogos = []
tot = 0
num = int(input(f'Quantos jogos voçê quer: '))

# Sortear os números
while tot < num:
    sorte = randint(1, 60)

    # Verificar para que o número não se repita dentro do mesmo jogo
    if sorte not in lista:
        lista.append(sorte)
        lista.sort()

    # Criar o jogo e colocar dentro do bilhete
    if len(lista) == 6:
        jogos.append(lista[:])
        lista.clear()
        tot += 1

# Retornar os jogos dentro do bilhete
for i, j in enumerate(jogos):
    print(f'{i+1}: {j}')
