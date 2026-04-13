# Criar uma função com parâmetros opcionais
def ficha(nome=None, gols=0):
    if nome:
        nome = n

    else:
        nome = '<desconhecido>'

    print(f'O jogador {nome} fez {gols} gols no campeonato.')


# Programa principal
n = str(input('Nome do jogador: ')).title()
g = str(input('Gols marcados: '))

if g.isnumeric():
    g = int(g)

else:
    g = 0

ficha(n, g)