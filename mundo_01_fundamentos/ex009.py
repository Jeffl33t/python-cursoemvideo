#Tabuada de um número
n = int(input(' Digite um numero para saber sua tabuada:'))

r1 = n * 1
r2 = n * 2
r3 = n * 3
r4 = n * 4
r5 = n * 5
r6 = n * 6
r7 = n * 7
r8 = n * 8
r9 = n * 9
r10 = n * 10

print('-'*15)
print('| {} x  1 = {:2} |'.format(n, r1))
print('| {} x  2 = {:2} |'.format(n, r2))
print('| {} x  3 = {:2} |'.format(n, r3))
print('| {} x  4 = {:2} |'.format(n, r4))
print('| {} x  5 = {:2} |'.format(n, r5))
print('| {} x  6 = {:2} |'.format(n, r6))
print('| {} x  7 = {:2} |'.format(n, r7))
print('| {} x  8 = {:2} |'.format(n, r8))
print('| {} x  9 = {:2} |'.format(n, r9))
print('| {} x 10 = {:2} |'.format(n, r10))
print('|_____________|')

#Versão 2
n = int(input('Digite um numero para saber sua tabuada:'))

print('_'*12)
print('n x  1 = {}\nn x  2 = {}\nn x  3 = {}\nn x  4 = {}\nn x  5 = {}\nn x  6 = {}\nn x  7 = {}\nn x  8 = {}\nn x  9 = {}\nn x 10 = {}'. format(n*1, n*2, n*3, n*4, n*5, n*6, n*7, n*8, n*9, n*10))
print('_'*12)