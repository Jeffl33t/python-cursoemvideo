#Mostra o antecessor e sucessor de um número
n = int(input('Digite um numero:'))

s = n - 1
s2 = n + 1

print('O antecessor de {} é {}'.format(n, s), end=' ')
print('e o sucessor é {}'.format(s2))

#versão 2
n = int(input('Digite um numero:'))

print('O antecessor de {} é {} e o sucessor é {}'.format(n, (n-1), (n+1)))