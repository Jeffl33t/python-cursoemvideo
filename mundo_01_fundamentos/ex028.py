<<<<<<< HEAD
from random import choice
from random import randint
from time import sleep

#Jogo de adivinhar um número
print('Pensei em um numero entre 0 e 5. Tente advinhar...')

num = int(input('Adivinhe o numero:'))
lista = [0,1,2,3,4,5]
sorte = choice(lista)

print('O numero sorteado foi... {}'.format(sorte))

if num == sorte:
    print('Voçê acertou! PARABENS!')

else:
    print('Voçê errou! tente outra vez!')

#gabarito
computador = randint(0, 5) # Faz o computador "PENSAR"

print('-=-' * 20)
print('Vou pensar em um número entre 0 e 5. Tente adivinhar...')
print('-=-' * 20)

jogador = int(input('Em que número eu pensei? ')) # Jogador tenta adivinhar
print('PROCESSANDO...')
sleep(3)

if jogador == computador:
    print('PARABÉNS! Você conseguiu me vencer!')

else:
    print('GANHEI! Eu pensei no número {} e não no {}!'.format(computador, jogador))
=======
from random import choice
from random import randint
from time import sleep

#Jogo de adivinhar um número
print('Pensei em um numero entre 0 e 5. Tente advinhar...')

num = int(input('Adivinhe o numero:'))
lista = [0,1,2,3,4,5]
sorte = choice(lista)

print('O numero sorteado foi... {}'.format(sorte))

if num == sorte:
    print('Voçê acertou! PARABENS!')

else:
    print('Voçê errou! tente outra vez!')

#gabarito
computador = randint(0, 5) # Faz o computador "PENSAR"

print('-=-' * 20)
print('Vou pensar em um número entre 0 e 5. Tente adivinhar...')
print('-=-' * 20)

jogador = int(input('Em que número eu pensei? ')) # Jogador tenta adivinhar
print('PROCESSANDO...')
sleep(3)

if jogador == computador:
    print('PARABÉNS! Você conseguiu me vencer!')

else:
    print('GANHEI! Eu pensei no número {} e não no {}!'.format(computador, jogador))
>>>>>>> db6fe22adc334c96809c710d30b7cd66b02d7359
