<<<<<<< HEAD
from datetime import date

#Verificar se um ano é ou não bissexto
ano = int(input('Digite o ano:'))

if ano == 0:
    ano = date.today().year

elif ano % 4 == 0 and ano % 100 != 0 or ano % 400 == 0:
    print('O ano {} é BISSEXTO!'.format(ano))

else:
    print('O ano {} não é BISSEXTO!'.format(ano))






=======
from datetime import date

#Verificar se um ano é ou não bissexto
ano = int(input('Digite o ano:'))

if ano == 0:
    ano = date.today().year

elif ano % 4 == 0 and ano % 100 != 0 or ano % 400 == 0:
    print('O ano {} é BISSEXTO!'.format(ano))

else:
    print('O ano {} não é BISSEXTO!'.format(ano))






>>>>>>> db6fe22adc334c96809c710d30b7cd66b02d7359
