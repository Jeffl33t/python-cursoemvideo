#Calcular o preço do aluguel de um carro
d = int(input('Quantos dias o carro foi alugado:'))
km = float(input('Quantos Km rodados:'))

print('Preço á pagar por diárias: R${:.2f}\nPreço á pagar por km rodado: R${:.2f}\nPreço Total: R${:.2f}'.format(d*60, km*0.15, (d*60)+(km*0.15)))
print('\n*O valor por diária é de R$60 mais R$0.15 por km rodado')
