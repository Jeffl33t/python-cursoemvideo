<<<<<<< HEAD
#Mostrar o fatorial de um número
print('\033[1;33mDIGITE UM NÚMERO PARA SABER SEU FATORIAL\033[m')

num = int(input('Digite um número:'))
c = num
a = num

while c != 1:
    c -= 1
    resultado = c * a
    a = resultado
    print( "x", c, "=",resultado, end= '→ ')

print('\nFatorial do número {}!'.format(num))
=======
#Mostrar o fatorial de um número
print('\033[1;33mDIGITE UM NÚMERO PARA SABER SEU FATORIAL\033[m')

num = int(input('Digite um número:'))
c = num
a = num

while c != 1:
    c -= 1
    resultado = c * a
    a = resultado
    print( "x", c, "=",resultado, end= '→ ')

print('\nFatorial do número {}!'.format(num))
>>>>>>> db6fe22adc334c96809c710d30b7cd66b02d7359
