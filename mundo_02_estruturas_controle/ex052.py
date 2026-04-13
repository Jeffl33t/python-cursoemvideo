<<<<<<< HEAD
#Verificar se um número é primo
print('\033[1;34mDIGITE UM NÚMERO PARA SABER SE ELE É OU NÃO UM NÚMERO PRIMO\033[m\n')

cont = 0
n = int(input('Digite um número:'))

for c in range(n, 0, -1):
    d = n / c
    if n % c == 0:
        cont += 1
        print('{:.0f} '.format(d),  end= '-> ')

if cont > 2:
    print('\nO número {} é divisível {} vezes e nao é um número primo'.format(n, cont))

else:
    print('\nO número {} é divisível apenas {} vezes e é um número primo'.format(n, cont))
=======
#Verificar se um número é primo
print('\033[1;34mDIGITE UM NÚMERO PARA SABER SE ELE É OU NÃO UM NÚMERO PRIMO\033[m\n')

cont = 0
n = int(input('Digite um número:'))

for c in range(n, 0, -1):
    d = n / c
    if n % c == 0:
        cont += 1
        print('{:.0f} '.format(d),  end= '-> ')

if cont > 2:
    print('\nO número {} é divisível {} vezes e nao é um número primo'.format(n, cont))

else:
    print('\nO número {} é divisível apenas {} vezes e é um número primo'.format(n, cont))
>>>>>>> db6fe22adc334c96809c710d30b7cd66b02d7359
