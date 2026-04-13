from random import randint
from time import sleep


print('\033[1;35mBORA UMA PARTIDA DE JOKENPÔ?!\033[m\n')

print('-=' * 20)
print('\n\033[1;35mEscreva:\033[m\n'
      '\n[1] PEDRA \u270A '
      '\n[2] PAPEL \u270B '
      '\n[3] TESOURA \u270C\uFE0F\n')
print('-=' * 20)

#Receber a jogada do computador e do jogador
cpu = randint(1,3)
user = int(input('\n\033[1;35mO que voce vai jogar?:\033[m'))
sleep(1)
print('\n\033[1;34mJO\033[m...')
sleep(2)
print('\n~~~~~\033[1;31mKEN\033[m...')
sleep(1)
print('\n~~~~~~~~~~~~\033[1;33mPÔ\033[m!!!')
sleep(1)

pedra = '\u270A'
papel = '\u270B'
tesoura = '\u270C\uFE0F'

#condições de vitória do jogador:
if user == 2 and cpu == 1:
    print('\nJogador {} x {} Computador. {} \033[1;34mJOGADOR VENCE!!!'.format(papel, pedra, papel))

elif user == 3 and cpu == 2:
    print('\nJogador {} x {} Computador. {} \033[1;34mJOGADOR VENCE!!!'.format(tesoura, papel, tesoura))

elif user == 1 and cpu == 3:
    print('\nJogador {} x {} Computador. {} \033[1;34mJOGADOR VENCE!!!'.format(pedra, tesoura, pedra))

#condições de derrota do jogador:
if cpu == 2 and user == 1:
    print('\nComputador {} x {} Jogador. {} \033[1;31mCOMPUTADOR VENCE!!!'.format(papel, pedra, papel))

elif cpu == 3 and user == 2:
    print('\nComputador {} x {} Jogador. {} \033[1;31mCOMPUTADOR VENCE!!!'.format(tesoura, papel, tesoura))

elif cpu == 1 and user == 3:
    print('\nComputador {} x {} Jogador. {} \033[1;31mCOMPUTADOR VENCE!!!'.format(pedra, tesoura, pedra))

#condições de empate:
if user == 1 and cpu == 1:
    print('\nJogador {} x {} Computador. {} \033[1;33mEMPATE!!!'.format(pedra, pedra, pedra))

elif user == 2 and cpu == 2:
    print('\nJogador {} x {} Computador. {} \033[1;33mEMPATE!!!'.format(papel, papel, papel))

elif user == 3 and cpu == 3:
    print('\nJogador {} x {} Computador. {} \033[1;33mEMPATE!!!'.format(tesoura, tesoura, tesoura))
