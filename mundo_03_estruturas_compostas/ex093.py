# Análisar o desempenho de um jogador de futebol
jogador = dict()
partidas = list()

# Receber o nome e total de partidas do jogador
jogador['nome'] = str(input('Nome do jogador: '))
tot = int(input(f'Quantas partidas {jogador['nome']} jogou: '))

# Receber a quantidade de gols marcados por partida
for c in range(1, tot + 1):
    partidas.append(int(input(f'  Quantos gols na {c}° partida: ')))

# Mostrar os gols marcados por partida e o total
jogador['gols'] = partidas[:]
jogador['total'] = sum(partidas)
print('-=' * 20)
print(jogador)
print('-=' * 20)

# Mostrar os valores para cada campo coletado
for k, v in jogador.items():
    print(f'O campo {k} tem valor {v}')

# Mostrar uma tabela com cada gols marcados em cada partida
print('-=' * 20)
print(f'O jogador {jogador['nome']} jogou {len(partidas)} partidas.')

for i, v in enumerate(partidas):
    print(f'  => Na {i + 1}° partida fez {v} gols.')

print(f'Foi um total de {jogador['total']} gols.')

# Versão 2

dados = dict()
gols = list()
dados['Nome'] = str(input('Digite o nome do jogador: '))
jogos = int(input(f'Quantas partidas {dados['Nome']} jogou: '))
tot = 0

for p in range(1, jogos + 1):
    gol = int(input(f'Quantos gols na partida {p}: '))
    gols.append(gol)
    tot += gol
    dados['Gols'] = gols
    dados['Total'] = tot

print('-=' * 30)
print(f'{dados}')
print('-=' * 30)

for k, v in dados.items():
    print(f'O campo {k} tem o valor {v}')

print('-=' * 30)
print(f'O jogador {dados['Nome']} jogou {len(gols)} partidas.')

for i, v in enumerate(gols):
    print(f'{'=>':>5} Na partida {i + 1}, fez {v} gols')

print(f'Foi um total de {dados['Total']} gols')