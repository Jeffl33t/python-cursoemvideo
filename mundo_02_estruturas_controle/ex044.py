#Simular um caixa com opções de formas de pagamento
print('\033[1;32mCALCULAR O PREÇO DE UMA COMPRA DE ACORDO COM A FORMA DE PAGAMENTO\033[m\n')

print('{:°^40}'.format('LOJAS MAK'))

preco = float(input('Digite o valor da compra: R$'))
forma = int(input('\n[1] Á VISTA'
                  '\n[2] PARCELADO\n'
                  '\nForma de pagamento:'))

if forma == 1:
    vista = int(input('\nFormas de pagamento Á VISTA:\n'
                      '\n[1] DINHEIRO (desconto 10%)'
                      '\n[2] CHEQUE (desconto 10%)'
                      '\n[3] CARTÃO (desconto 5%)\n'
                      '\nEscolha sua forma de pagamento: '))

    if vista == 1:
        print('\nPreço Total: R${:.2f}'.format(preco * 0.9))

    elif vista == 2:
        print('\nPreço Total: R${:.2f}'.format(preco * 0.9))

    elif vista == 3:
        print('\nPreço Total: R${:.2f}'.format(preco * 0.95))

if forma == 2:
    prazo = int(input('\nForma de pagamento PARCELADO:\n'
                      '\n[1] CARTÃO x 2 (sem juros)'
                      '\n[2] CARTÃO x 3 (juros de 20%)\n'
                      '\nEscolha em quantas vezes:'))

    if prazo == 1:
        print('\nPreço Total: 2 x R${:.2f}'.format(preco / 2))

    elif prazo == 2:
        print('\nPreço Total: 3 x R${:.2f}'.format((preco * 1.2) / 3))