#Criar uma simulação de financiamento
print('\033[4m\033[1mSIMULAÇÃO DE FINANCIAMENTO\033[m\n')

casa = float(input('Insira o preço da casa: \033[1;32mR$\033[m'))
salario = float(input('Insira o valor do seu salário: \033[1;32mR$\033[m'))
tempo = int(input('Insira em quanto tempo voçê gostaria de pagar:'))
prestacoes = casa / (tempo * 12)

if prestacoes < (salario * 0.3):
    print('\n\033[1;;42mFINANCIAMENTO APROVADO!\033[m'
          '\n\033[1;34mO número de prestações será de: \033[1;32m{}\033[mx'
          '\n\033[1;34mO preço mensal a ser pago é de: \033[1;32mR${:.2f}\033[m'
          '\n\033[1;34mEm um periodo de \033[m\033[1;32m{}\033[m\033[1;34m anos.\033[m'.format((tempo * 12), prestacoes, tempo ))

else:
    print('\n\033[1;30;41mFINANCIAMENTO NEGADO!\033[m'
          '\n*\033[1;33mNas condições inseridas o seu financiamento foi recusado,'
          '\npois o valor das prestações excedem \033[m\033[1;31m30%\033[m\033[1;33m de sua renda mensal.'
          '\nMas\033[m \033[1;32mNÃO DESISTA\033[m\033[1;33m ainda!. Ajuste o período de pagamento e tente novamente!.')

#(solucionar o problema numero de prestação x valor da prestação)