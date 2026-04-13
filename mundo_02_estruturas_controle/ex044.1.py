#Simular um caixa com opções de formas de pagamento
print('{:°^40}'.format('LOJAS MAK'))

preco = float(input('\nDigite o valor das suas compras: R$'))

#Escolher forma de pagamento
print('\nFormas de Pagamento:\n'
      '\n[1] Á VISTA'
      '\n[2] PARCELADO')
forma = int(input('\nPagamento á vista ou parcelado:'))

#Calcular desconto para as formas de pagamento á vista
if forma == 1:
    total = 0
    print('\nSelecione a opção desejada:\n'
          '\n[1] DINHEIRO/CHEQUE (desconto 10%)'
          '\n[2] CARTÃO (desconto 5%)\n')
    pago = int(input('\nPagamento em:'))

    if pago == 1:
        total = (preco * 0.9)

    elif pago == 2:
        total = (preco * 0.95)

    print('\nPreço: R${}\nPreço Total com Desconto: R${}'.format(preco, total))

#Calcular juros para as formas de pagamento parcelado
elif forma == 2:
    pago = int(input('\nSelecione a opção desejada:\n'
                     '\n[1] CARTÃO em 2 vezes (sem juros)'
                     '\n[2] CARTÃO em até 10 vezes(juros 20%)\n'
                     '\nPagamento em:'))
    if pago == 1:
        total = preco / 2
        print('\nPreço Total: R${}\nPreço das Parcelas: R${} x 2'.format(preco, total))

    elif pago == 2:
        vezes = int(input('Em quantas vezes:'))
        parcelas= (preco * 1.2) / vezes
        total = preco * 1.2
        print('\nPreço: R${}\nPreço das Parcelas: R${} x {}\nPreço Total com Juros: R$:{}'.format(preco, parcelas, vezes, total))

    #Verificar se a forma de pagamento parcelado é válida
    elif pago != 1 or pago != 2:
        print('OPÇÃO INVÁLIDA de pagamento. Tente Novamente.')

else:
    total = 0
    print('OPÇÃO INVÁLIDA de pagamento. Tente Novamente.')