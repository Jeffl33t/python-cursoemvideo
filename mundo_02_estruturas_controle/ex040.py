#Calcular a média de um aluno
print('\033[1;34mCALCULE A MÉDIA DO ALUNO\033[m\n')

nota1 = float(input('Digite a primeira nota:'))
nota2 = float(input('Digite a segunda nota:'))
media = (nota1 + nota2) / 2

if media < 5:
    print('\033[1;31mREPROVADO\033[m!!!. A média do aluno é de \033[1;31m{:.1f}'.format(media))

elif  5 <= media <= 6.9:
    print('\033[1;33mRECUPERAÇÃO\033[m!. A média do aluno é de \033[1;33m{:.1f}'.format(media))

elif media >= 7:
    print('\033[1;34mAPROVADO\033[m!!!. A média do aluno é de \033[1;34m{:.1f}'.format(media))