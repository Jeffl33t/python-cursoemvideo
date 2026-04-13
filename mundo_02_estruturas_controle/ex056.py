<<<<<<< HEAD
#Análisar grupo de pessoas:
#Nome do homem mais velho, média de idade e mulheres menores de 20 anos
somaIdade = 0
mediaIdade = 0
maisVelho = 0
nomeVelho = ''
mulher20 = 0

#Receber as informações
for p in range(1, 5):
    print('----- {}º PESSOA -----'.format(p))
    nome = str(input('Nome:')).strip().title()
    idade = int(input('Idade:'))
    sexo = str(input('Sexo [M/F]:'))
    somaIdade += idade
    mediaIdade = somaIdade / 4

    #Verificar se é homem
    if p == 1 and sexo == 'Mm':
        maisVelho = idade
        nomeVelho = nome

    #Verificar o homem mais velho e nome
    if sexo in 'Mm' and idade > maisVelho:
        maisVelho = idade
        nomeVelho = nome

    #Verificar se é mulher e menor de 20 anos
    if sexo in 'Ff' and idade < 20:
        mulher20 += 1

print('A media de idade do grupo é {}'.format(mediaIdade))
print('O homem mais velho tem {} de idade e o nome é {}'.format(maisVelho, nomeVelho))
print('Mulheres abaixo de 20 anos {}'.format(mulher20))
=======
#Análisar grupo de pessoas:
#Nome do homem mais velho, média de idade e mulheres menores de 20 anos
somaIdade = 0
mediaIdade = 0
maisVelho = 0
nomeVelho = ''
mulher20 = 0

#Receber as informações
for p in range(1, 5):
    print('----- {}º PESSOA -----'.format(p))
    nome = str(input('Nome:')).strip().title()
    idade = int(input('Idade:'))
    sexo = str(input('Sexo [M/F]:'))
    somaIdade += idade
    mediaIdade = somaIdade / 4

    #Verificar se é homem
    if p == 1 and sexo == 'Mm':
        maisVelho = idade
        nomeVelho = nome

    #Verificar o homem mais velho e nome
    if sexo in 'Mm' and idade > maisVelho:
        maisVelho = idade
        nomeVelho = nome

    #Verificar se é mulher e menor de 20 anos
    if sexo in 'Ff' and idade < 20:
        mulher20 += 1

print('A media de idade do grupo é {}'.format(mediaIdade))
print('O homem mais velho tem {} de idade e o nome é {}'.format(maisVelho, nomeVelho))
print('Mulheres abaixo de 20 anos {}'.format(mulher20))
>>>>>>> db6fe22adc334c96809c710d30b7cd66b02d7359
