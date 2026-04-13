from datetime import date


# Análisar dados cadastrados
dados = dict()

# Receber os dados a serem análisados
dados['Nome'] = str(input('Digite o nome: ')).title()
nasc = int(input('Data de nascimento: '))
dados['Idade'] = date.today().year - nasc
dados['Ctps'] = int(input('N° Carteira de trabalho: '))

# Verificar se possui carteira de trabalho e retornar o tempo até a aposentadoria
if dados['Ctps'] != 0:
    dados['Contratacao'] = int(input('Ano de contratação: '))
    dados['Salario'] = float(input('Digite o salário: R$'))
    dados['Aposentar'] = dados['Contratacao'] + 35 - date.today().year + dados['Idade']

print('-=-' * 30)
print(dados)
print('-=-' * 30)

# Retorna os dados
for k, v in dados.items():
    print(f'  - {k} tem o valor {v}')
