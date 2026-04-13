#Mostrar - Nome e preço do produto mais barato
#        - Quantidade de produtos com o preço a cima de 1000
#        - Preço total
menorPreco = menorNome = total = maisMil = cont = 0

while True:
    produto = str(input('Nome do produto:')).strip().title()
    preco = float(input('Preco: R$'))
    cont += 1
    total += preco

    if preco > 1000:
        maisMil += 1

    if cont == 1 or preco < menorPreco:
        menorPreco = preco
        menorNome = produto

    opc = ' '
    while opc not in 'SN':
        opc = str(input('Continuar [S/N]:')).strip().upper()[0]

    if opc == 'N':
        break

print(f'Preço Total: R${total:.2f}')
print(f'Produtos mais caros que $1000,00: {maisMil}')
print(f'Produto mais barato: {menorNome}, R${menorPreco:.2f}')
