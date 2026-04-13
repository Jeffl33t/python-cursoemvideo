def area(a, b):
    r = (a * b)
    print(f'A área de um terreno {a:.1f}x{b:.1f} é de {r}m²')


print('Controle de Terreno')
print('-' * 20)
largura = float(input('LARGURA (m): '))
comprimento = float(input('COMPRIMENTO (m): '))
area(largura, comprimento)