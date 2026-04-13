#Calcular aumento salárial
salario = float(input('Digite o valor do seu salário: R$'))

if salario <= 1250:
    print('Seu salário com o aumento de 10% fica R${:.2f}.'.format(salario * 1.15))

else:
    print('Seu salário com o aumento de 15% fica R${:.2f}.'.format(salario * 1.10))