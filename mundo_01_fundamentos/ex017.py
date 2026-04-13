from math import hypot

#Calcular a Hipotenusa
co = float(input('Insira o tamanho do C.O:'))
ca = float(input('Insira o tamanho do C.A:'))

print('Em um triângulo retângulo de C.O {} e C.A {} o comprimento da hipotenusa é {:.3f}'.format(co, ca, hypot(co, ca)))

#Versão 2
co = float(input('Insira o tamanho do C.O:'))
ca = float(input('Insira o tamanho do C.A:'))

hi = (co ** 2 + ca ** 2) ** (1/2)

print('Em um triângulo retângulo de C.O {} e C.A {} o comprimento da hipotenusa é {:.3f}'.format(co, ca, hi))

