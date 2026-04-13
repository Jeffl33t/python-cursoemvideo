# Análisar os dados de um jogador de futebol
dados = dict()
jogador = list()

# Coletar o nome do jogador, número de partidas e gols marcados em cada partida
while True:
    print('-' * 30)
    dados['nome'] = str(input('Digite o nome: ')).title()
    jogos = int(input(f'Quantas partidas {dados['nome']} tem: '))
    gols = list()
    tot = 0

    for j in range(1, jogos + 1):
        gol = (int(input(f'Quantos gols na partida {j}: ')))
        gols.append(gol)
        tot += gol
        dados['gols'] = gols
        dados['total'] = tot

    opcao = str(input('Continuar [S/N]: '))
    jogador.append(dados.copy())

    if opcao in 'Nn':
        break

# Mostrar uma tabela com as informações dos jogadores
print('-=' * 18)
print(f'{'COD NOME':<10} {'GOLS':>10} {'TOTAL':>15}')

for i, j in enumerate(jogador):
    print(f'{f'  {i} {j['nome']}':<16} {f'{j['gols']}':<14} {j['total']:<}')

print('-' * 36)

# Menu para visualizar as informações de forma individual
while True:
    resp = int(input('Mostrar dados de qual jogador(999 parar): '))

    if resp == 999:
        break

    if resp >= len(jogador):
        print(f'ERRO.Não existe jogador com o código {resp}! Tente novamente')

    else:
        print(f'LEVANTAMENTO DO JOGADOR {jogador[resp]['nome']}:')

        for p, g in enumerate(jogador[resp]['gols']):
            print(f'No jogo {p} fez {g} gols.')

        print('-' * 36)

print('<<< PROGRAMA ENCERRADO >>>')

# Gabarito

jogador = dict()
time = list()

while True:
    jogador['nome'] = str(input('Nome do jogador: ')).title()
    partidas = int(input(f'Quantas partida {jogador['nome']} jogou: '))
    gols = list()

    for c in range(0, partidas):
        gols.append(int(input(f'Quantos gols na {c + 1}° partida: ')))
    jogador['gols'] = gols[:]
    jogador['total'] = sum(gols)
    time.append(jogador.copy())

    while True:
        opcao = str(input('Continuar [S/N]: ')).upper()

        if opcao in 'SN':
            break
        print('ERRO. Responda apenas S ou N.')

    if opcao in 'Nn':
        break

print('-=' * 20)
print('cod ', end='')

for i in jogador.keys():
    print(f'{i:<15}', end='')

print()
print('-' * 40)

for k, v in enumerate(time):
    print(f'{k:>3} ', end='')

    for d in v.values():
        print(f'{str(d):<15}', end='')
    print()

while True:
    while True:
        print('-' * 40)
        resp = int(input('Mostrar dados de qual jogador (999 parar): '))

        if resp < len(time):
            break
        print('ERRO. Código inexistente. Tente novamente')

    for i, j in enumerate(time):
        if resp == i:
            print(f'-- LEVANTAMENTO DO JOGADOR {j['nome']}:')

            for p, g in enumerate(j['gols']):
                print(f'   Na {p + 1}° partida, fez {g} gols.')

    if resp == 999:
        break

