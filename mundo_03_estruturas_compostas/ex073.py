#Análisar a tabela do Brasileirão
print('\033[1;34mTABELA DO BRASILEIRÃO\033[m\n')

pos = ('Palmeiras', 'Flamengo', 'Bragantino', 'Cruzeiro', 'Fluminense',
       'Bahia', 'Ceará', 'Corinthians', 'Morangos', 'São Paulo',
       'Botafogo', 'Grêmio', 'Vasco', 'Juventude', 'Mirassol',
       'Fortaleza', 'Atlético MG', 'Vitória', 'Santos', 'Sport')

print(f'Os 5 primeiros colocados são {pos[0:5]}')
print(f'Os 4 ultimos são {pos[-4:]}')
print(f'Os times em ordem alfabética {sorted(pos)}')
print(f'O Grêmio está na colocação {(pos.index('Grêmio') + 1)}')