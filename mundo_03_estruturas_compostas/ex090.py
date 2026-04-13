# Criar um dicionário com nome e média de um aluno
aluno = dict()
aluno['Nome'] = str(input('Digite o nome do aluno: '))
aluno['Média'] = float(input(f'Média de {aluno['Nome']}: '))

if aluno['Média'] >= 6:
    aluno['Situação'] = 'APROVADO'

else:
    aluno['Situação'] = 'REPROVADO'

for k, v in aluno.items():
    print(f'{k} é igual a {v}.')