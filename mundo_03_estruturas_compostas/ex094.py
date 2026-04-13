# Análisar os dados de um grupo de pessoas
dados = dict()
pessoa = list()
media = 0

# Coletar nome, idade e sexo
while True:
    dados['nome'] = str(input('Digite o nome: ')).title()

    while True:
        dados['sexo'] = str(input('Digite o sexo [M/F]: ')).upper()[0]

        if dados['sexo'] in 'MF':
            break
        print('ERRO. Responda apenas "M" ou "F".')

    dados['idade'] = int(input('Digite a idade: '))
    pessoa.append(dados.copy())
    media += dados['idade']

    while True:
        opcao = str(input('Continuar [S/N]: ')).upper()[0]

        if opcao in 'SN':
            break
        print('ERRO. Responda apenas "S" ou "N".')

    if opcao in 'Nn':
        break

media /= len(pessoa)

# Mostrar média de idade, qtd de total de pessoas e qtd de mulheres cadastradas
print('-=' * 30)
print(f'  - O grupo tem {len(pessoa)} pessoas.')
print(f'  - A média de idade é de {media:.2f} anos.')
print(f'  - Mulheres cadastradas: ', end='')

for p in pessoa:
    if p['sexo'] in 'F':
        print(f'{p['nome']}', end=' ')

#Mostrar pessoas com idade acima da média
print(f'\n  - Pessoas com idade acima da média:\n')

for p in pessoa:
    if p['idade'] >= media:
        print('    ', end='')

        for k, v in p.items():
            print(f'{k} = {v};', end=' ')
        print()

print('<<< ENCERRADO >>>')

