from datetime import date

#Verificar categoria por idade
print('\033[1;34mSEPARAR ATLETAS POR CATEGORIA NA NATAÇÃO\033[m\n')

nasc = int(input('Digite o ano de nascimento do atleta:'))
hoje = date.today().year
idade = hoje - nasc

if idade <= 9:
    print('\nCategoria: MIRIM')

elif 9 < idade <= 14:
    print('\nCategoria: INFANTIL')

elif idade <= 19:
    print('\nCategoria: JUNIOR')

elif idade <= 20:
    print('\nCategoria: SÊNIOR')

else:
    print('\nCategoria: MASTER')
