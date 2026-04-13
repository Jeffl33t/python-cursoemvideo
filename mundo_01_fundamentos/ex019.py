from random import choice

#Cria uma lista de alunos e escolhe um deles
a1 = input('Digite o primeiro nome:')
a2 = input('Digite o segundo nome:')
a3 = input('Digite o terceiro nome:')
a4 = input('Digite o quarto nome:')

lista = [a1, a2, a3, a4]

print('O escolhido para apagar o quadro foi a: {}'.format(choice(lista)))