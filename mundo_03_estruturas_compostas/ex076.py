#Criar um tabelamento de produtos
print('\033[1;34mLISTA DE PRODUTOS COM SEUS VALORES\033[m\n')
print('-='* 19)
print(f'{"LOJÃO OBA OBA":^37}')
print('-='* 19)

produtos = ('Caneta', 3.00,
            'Lápis', 1.50,
            'Borracha', 1.00,
            'Estojo', 15.50,
            'Caderno', 17.99,
            'Lápis de Cor', 9.99,
            'Régua', 5.99,
            'Mochila', 69.90)

for item in range(0, len(produtos), 2):
    print(f'{produtos[item]:.<30}R$ {produtos[item + 1]:>5.2f}')
