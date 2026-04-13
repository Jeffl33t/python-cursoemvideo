#Solicitar dado até que seja válido
print('\033[1;34mPROGRAMA QUE PEÇA PARA DIGITAR [M/F], CASO ERRE PEÇA PARA DIGITAR NOVAMENTE\033[m')

sexo = ''
while sexo != 'M' and sexo != 'F':
    sexo = str(input('Digite o sexo [M/F]:')).upper()

    if sexo == 'M' or sexo == 'F':
        print('Continue')

    else:
        print('Inválido')

#Gabarito
sexo = str(input('Digite o Sexo [M/F]:')).strip().upper()[0]

while sexo not in 'MmFf':
    sexo = str(input('Dados inválidos. Digite o sexo:')).strip().upper()[0]

print('Sexo {} registrado com sucesso.'.format(sexo))
