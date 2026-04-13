from math import trunc

#Mostrar a parte inteira de um número real
num = float(input('Digite um numero real:'))
print('A parte inteira de {} é {}'.format(num, trunc(num)))

#Versão 2
num = float(input('Digite um numero real:'))
print('A parte inteira de {} é {}'.format(num, int(num)))