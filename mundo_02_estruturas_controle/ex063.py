<<<<<<< HEAD
#Mostra a sequência de Fibonacci
print('\033[1;34mSEQUÊNCIA DE FIBONACCI\033[m\n')

termos = int(input('Digite o número de termos:'))
t1 = 0
t2 = 1
print('{} → {}'.format(t1, t2), end='')

c = 3
while c <= termos:
    t3 = t1 + t2
    print(' → {}'.format(t3), end='')
    t1 = t2
    t2 = t3
    c += 1

=======
#Mostra a sequência de Fibonacci
print('\033[1;34mSEQUÊNCIA DE FIBONACCI\033[m\n')

termos = int(input('Digite o número de termos:'))
t1 = 0
t2 = 1
print('{} → {}'.format(t1, t2), end='')

c = 3
while c <= termos:
    t3 = t1 + t2
    print(' → {}'.format(t3), end='')
    t1 = t2
    t2 = t3
    c += 1

>>>>>>> db6fe22adc334c96809c710d30b7cd66b02d7359
print(' → FIM')