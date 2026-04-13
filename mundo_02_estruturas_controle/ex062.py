#Calcular a PA de um número
print('\033[1;34mGERADOR DE PA (APRIMORADO)\033[m\n')

primeiro = int(input('Primeiro termo:'))
razao = int(input('Razão:'))
termos = primeiro
cont = 1
totTermos = 10
mais = 0

#Armazenar o número total de termos
while True:
    totTermos = totTermos + mais

    #Calcular a PA
    while cont <= totTermos:
        primeiro += razao
        cont += 1
        print(primeiro, end="→")
    print()

    #Receber mais termos
    mais = int(input("Mais termos:"))
    if mais == 0:
        break

print("Programa finalizado... Total de termos mostrados {}.".format(totTermos))

#Gabarito
primeiro = int(input('Primeiro termo:'))
razao = int(input('Razão:'))
termos = primeiro
c = 1
total = 0
mais = 10
while mais != 0:
    total = total + mais
    while c <= total:
        print('{} →'.format(termos), end='')
        termos += razao
        c += 1
    print('PAUSA')
    mais = int(input('Mais termos:'))
print('Progressão finalizada o total de termos mostrados {}'.format(total))
