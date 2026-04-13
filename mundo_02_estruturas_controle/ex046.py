from time import sleep

#Contagem regressiva
print('\033[1;34mPREPARE SE PARA A CONTAGEM REGRESSIVA\n\033[m')

for c in range(10, -1, -1):
    sleep(1)
    print(c)

sleep(1)
print('BOOOOOOM')


