from random import randint

#Cria jogo de par ou ímpar
cont = 0

#Receber a jogada do computador e do jogador
while True:
    computador = randint(0, 11)
    jogador = int(input('Digite o valor:'))
    cont += 1
    soma = computador + jogador
    escolha = ' '

    #Verificar condições de vitória e vitórias consecutivas
    while escolha not in 'PI':
        escolha = str(input('Par ou impar? [P/I]:')).strip().upper()[0]

    if escolha == 'P' and soma % 2 == 0:
        print(f'Jogador(par) VENCE! {computador} + {jogador} = {soma}. Vitorias consecutivas {cont}')

    elif escolha == 'I' and soma % 2 == 1:
        print(f'Jogador(ímpar) VENCE! {computador} + {jogador} = {soma}. Vitorias consecutivas {cont}')

    else:
        break

print(f'Jogador PERDE! {computador} + {jogador} = {soma}')
