<<<<<<< HEAD
from random import randint

#Jogo de adivinhação
#Computador escolhe um número
computador = randint(0, 10)
jogador = ''
cont = 0
print('COMPUTADOR: hmmm... Pensei em um número entre 0 e 10.')

#Jogador escolhe um número
while jogador != computador:
    jogador = int(input('Tente adivinhar:'))
    cont += 1
    #Verificar acerto e conta quantidade de vezes que jogador errou
    if jogador == computador:
        print('Computador {} e {} Jogador. ACERTOU!!!. Tentativas {}'.format(computador, jogador, cont))

    elif jogador > computador:
        print('ERROU!. O número é menor. Tente denovo.')

    elif jogador < computador:
        print('ERROU!. O número é maior. tente denovo.')

#gabarito
computador = randint(0, 10)
acertou = False
cont = 0
print('Pensei em um número de 0 a 10')

while not acertou:
    jogador = int(input('Tente adivinhar:'))
    cont += 1

    if computador == jogador:
        acertou = True

    else:
        if computador < jogador:
            print('Menos...')

        elif computador > jogador:
            print('Mais...')

print('ACERTOU {} tentativas {}'.format(computador, cont))
=======
from random import randint

#Jogo de adivinhação
#Computador escolhe um número
computador = randint(0, 10)
jogador = ''
cont = 0
print('COMPUTADOR: hmmm... Pensei em um número entre 0 e 10.')

#Jogador escolhe um número
while jogador != computador:
    jogador = int(input('Tente adivinhar:'))
    cont += 1
    #Verificar acerto e conta quantidade de vezes que jogador errou
    if jogador == computador:
        print('Computador {} e {} Jogador. ACERTOU!!!. Tentativas {}'.format(computador, jogador, cont))

    elif jogador > computador:
        print('ERROU!. O número é menor. Tente denovo.')

    elif jogador < computador:
        print('ERROU!. O número é maior. tente denovo.')

#gabarito
computador = randint(0, 10)
acertou = False
cont = 0
print('Pensei em um número de 0 a 10')

while not acertou:
    jogador = int(input('Tente adivinhar:'))
    cont += 1

    if computador == jogador:
        acertou = True

    else:
        if computador < jogador:
            print('Menos...')

        elif computador > jogador:
            print('Mais...')

print('ACERTOU {} tentativas {}'.format(computador, cont))
>>>>>>> db6fe22adc334c96809c710d30b7cd66b02d7359
