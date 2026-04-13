<<<<<<< HEAD
#Mostra maiores de idades, total de homens e mulheres menores de 20 anos
maiorIdade = mulherMenor = totHomens = 0

while True:
    idade = int(input('Digite sua idade:'))
    sexo = ' '

    while sexo not in 'MF':
        sexo = str(input('[M/F]:')).strip().upper()[0]

    if idade >= 18:
        maiorIdade += 1

    if sexo in 'M':
        totHomens += 1

    if sexo in 'F' and idade < 20:
        mulherMenor += 1

    opcao = ' '
    while opcao not in 'SN':
        opcao = str(input('[S/N]:')).strip().upper()[0]

    if opcao == 'N':
        break

print(f'Maiores de idade: {maiorIdade}')
print(f'Total de homens: {totHomens}')
print(f'Mulheres menores de 20: {mulherMenor}')
=======
#Mostra maiores de idades, total de homens e mulheres menores de 20 anos
maiorIdade = mulherMenor = totHomens = 0

while True:
    idade = int(input('Digite sua idade:'))
    sexo = ' '

    while sexo not in 'MF':
        sexo = str(input('[M/F]:')).strip().upper()[0]

    if idade >= 18:
        maiorIdade += 1

    if sexo in 'M':
        totHomens += 1

    if sexo in 'F' and idade < 20:
        mulherMenor += 1

    opcao = ' '
    while opcao not in 'SN':
        opcao = str(input('[S/N]:')).strip().upper()[0]

    if opcao == 'N':
        break

print(f'Maiores de idade: {maiorIdade}')
print(f'Total de homens: {totHomens}')
print(f'Mulheres menores de 20: {mulherMenor}')
>>>>>>> db6fe22adc334c96809c710d30b7cd66b02d7359
