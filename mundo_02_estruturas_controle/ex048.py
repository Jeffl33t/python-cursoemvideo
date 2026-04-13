print('\033[1;34mSOME TODOS OS NÚMEROS ÍMPARES MÚLTIPLOS DE 3 NO INTERVALO DE 1 Á 500.\033[m\n')

#Somar os valores ímpares no intervalo
s = 0
cont = 0

for c in range(0, 500, 3):
    if c % 2 == 1:
        cont += 1 # ou cont = cont + 1
        s += c # ou s = s + c

print('A soma de todos os {} valores é {}'.format(cont, s))
