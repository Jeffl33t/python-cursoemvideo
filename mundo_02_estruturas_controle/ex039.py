from datetime import date

#Verificar alistamento
print('\033[1;32mALISTAMENTO PARA O EXERCITO BRASILEIRO\033[m\n')

nasc = int(input('Digite seu ano de nascimento:'))
atual = date.today().year
idade = atual - nasc

if idade == 18:
    print('Você tem {} anos, esta na sua hora de se ALISTAR'.format(idade))

elif idade < 18:
    print('Você tem {} anos, ainda falta {} anos para chegar sua hora de se ALISTAR'.format(idade, 18 - idade))

else:
    print('Você tem {} anos, seu tempo de ALISTAMENTO já passou há {} anos'.format(idade, idade - 18))

#gabarito
nasc = int(input('Digite seu ano de nascimento:'))
atual = date.today().year
idade = atual - nasc

if idade == 18:
    print('Você tem {} anos, esta na sua hora de se ALISTAR'.format(idade))

elif idade < 18:
    saldo = 18 - idade
    alistamento = atual + saldo
    print('Você tem {} anos, ainda falta {} anos para chegar sua hora de se ALISTAR'.format(idade, saldo))
    print('Seu ALISTAMENTO será no de {}'.format(alistamento))

else:
    saldo = idade - 18
    alistamento = atual - saldo
    print('Você tem {} anos, seu tempo de ALISTAMENTO já passou há {} anos'.format(idade, saldo))
    print('Seu ano de ALISTAMENTO foi em {}'.format(alistamento))
