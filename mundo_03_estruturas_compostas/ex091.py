from random import randint
from operator import itemgetter
from time import sleep


#Criar um dicionário com 4 jogadores
    # Sortear um número para cada jogador
    # Criar um rank de acordo com número sorteado para cada jogador
jogo = dict()
lista = list()
print(f'<<< VALORES SORTEADOS >>>\n')

# Sortear e mostrar o número de cada jogador
for j in range(1, 5):
    jogo['Jogador'] = j
    jogo['Número'] = randint(1, 6)
    print(f'O Jogador{j} tirou: {jogo['Número']}')
    sleep(1)

    # Verificar o número sorteado para cada jogador
    if j == 1 or jogo['Número'] < lista[-1]['Número']:
        lista.append(jogo.copy())

    # Montar o rank de jogadores
    else:
        pos = 0
        while pos < len(lista):
            if jogo['Número'] >= lista[pos]['Número']:
                lista.insert(pos, jogo.copy())
                break
            pos += 1

# Retornar o rank
print('\n<<< RANKING DOS JOGADORES >>>\n')
for i, d in enumerate(lista):
    print(f'{i + 1}° Lugar: Jogador{lista[i]['Jogador']} com {lista[i]['Número']}')
    sleep(1)

# Gabarito
jogo = {'Jogador1': randint(1, 6),
        'Jogador2': randint(1, 6),
        'Jogador3': randint(1, 6),
        'Jogador4': randint(1, 6)}
ranking = list()
print('<<< VALORES SORTEADOS >>>\n')

for k, v in jogo.items():
    print(f'O {k} tirou {v}')
    sleep(1)

print('\n<<< RANKING DE JOGADORES >>>\n')
ranking = sorted(jogo.items(), key=itemgetter(1), reverse=True)

for i, j in enumerate(ranking):
    print(f'{i + 1}° Lugar: {j[0]} com {j[1]}')
    sleep(1)


