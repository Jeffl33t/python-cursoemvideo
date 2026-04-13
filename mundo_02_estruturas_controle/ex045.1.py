from random import randint

#Criar o jogo Jokenpô
print('\33[1;34mJOO... KEEN... PÔÔÔÔ!!!\033[m\n', '-=' * 20)
print('Para escolher digite:\n'
      '\n[0] PEDRA'
      '\n[1] PAPEL'
      '\n[2] TESOURA\n')
print('-=' * 20)

#Receber a jogado do computador e do jogador
item = ('PEDRA', 'PAPEL', 'TESOURA')
computador = randint(0, 2)
jogador = int(input('\nQual a sua jogada:'))

print('\n','-=' * 20)
print('\nComputador {}\nJogador {}\n'.format((item[computador]), (item[jogador])))

#Verificar condições de vitória
if computador == 0:
    if jogador == 0:
        print('EMPATE')

    elif jogador == 1:
        print('JOGADOR VENCE')

    elif jogador == 2:
        print('COMPUTADOR VENCE')

    else:
        print('JOGADA INVALIDA. Tente Novamente.')

elif computador == 1:
    if jogador == 1:
        print('EMPATE')

    elif jogador == 2:
        print('JOGADOR VENCE')

    elif jogador == 0:
        print('COMPUTADOR VENCE')

    else:
        print('JOGADA INVALIDA. Tente Novamente.')

elif computador == 2:
    if jogador == 2:
        print('EMPATE')

    elif jogador == 0:
        print('JOGADOR VENCE')

    elif jogador == 1:
        print('COMPUTADOR VENCE')

    else:
        print('JOGADA INVALIDA. Tente Novamente.')