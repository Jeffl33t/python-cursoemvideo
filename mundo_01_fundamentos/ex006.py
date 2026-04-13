<<<<<<< HEAD
#Mostrar o dobro, triplo e raiz quadrada de um número
n = int(input('Digite um numero:'))

d = n * 2
t = n * 3
r = n ** (1/2)

print('O dobro de {} é {}'.format(n, d))
print('O triplo de {} é {}'.format(n, t))
print ('A raiz quadrada de {} é {:.2f}'.format (n, r))

#versão 2
n = int(input('Digite um numero:'))

=======
#Mostrar o dobro, triplo e raiz quadrada de um número
n = int(input('Digite um numero:'))

d = n * 2
t = n * 3
r = n ** (1/2)

print('O dobro de {} é {}'.format(n, d))
print('O triplo de {} é {}'.format(n, t))
print ('A raiz quadrada de {} é {:.2f}'.format (n, r))

#versão 2
n = int(input('Digite um numero:'))

>>>>>>> db6fe22adc334c96809c710d30b7cd66b02d7359
print('O dobro de {} é {}, o triplo é {} e a raiz quadrada é {:.2f}.'.format (n, (n*2), (n*3), pow(n, (1/2))))