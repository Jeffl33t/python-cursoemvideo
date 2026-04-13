from random import shuffle

#Embaralhar uma lista
lista = ['maria','rose','sina','ymir']
shuffle (lista)

print('A ordem para apresentação dos trabalhos será a seguinte: {}'.format(lista))


a1 = input('Primeiro nome:')
a2 = input('Segundo nome:')
a3 = input('Terceiro nome:')
a4 = input('Quarto nome:')

lista = [a1, a2, a3, a4]

shuffle (lista)

print('A ordem para apresentação dos trabalhos será a seguinte: {}'.format(lista))