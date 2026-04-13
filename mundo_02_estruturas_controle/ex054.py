from datetime import date

#Verificar maiores de idade
print('\033[1;34mDIGITE O NOME DE 5 PESSOAS PARA SABER SE SÃO OU NÃO MAIORES DE IDADE\033[m\n')

maior = 0
menor = 0

for c in range(7):
    nas = int(input('Digite a data de nascimento:'))
    atual = date.today().year
    idade = atual - nas

    if idade >=21:
        maior += 1

    else:
        menor += 1

print('Maiores de idade {}\nMenores de idade {}'.format(maior, menor))