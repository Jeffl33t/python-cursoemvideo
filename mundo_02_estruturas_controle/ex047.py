from time import sleep

#Mostrar números pares
print('\033[1;34mMOSTRA TODOS OS NÚMEROS PARES DE 1 Á 50\n\033[m')

for c in range(2, 51, 2):
    sleep(0.5)
    print( c, end=' ')

print('ACABOU')