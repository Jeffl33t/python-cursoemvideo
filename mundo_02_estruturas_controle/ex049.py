#Mostrar a tabuada de um número
print('\033[1;34mTABUADA\033[m\n')

n = int(input('Digite um número para saber a tabuada:'))

for c in range(1, 11, 1):
    print('{} x {:2} = {}'.format(n, c, n*c))
