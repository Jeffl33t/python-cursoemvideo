#Converter para dólar e euro
r = float(input('Digite o valor: R$'))

d = r / 6.0193
e = r / 6.6399

print('\nO valor convertido para dólar é de: US${:.2f}\nO valor convertido para euro é de: £{:.2f}'.format(d, e))

#Versão 2
r = float(input('Digite o valor: R$'))

print('\nO valor convertido para dólar é de: US${:.2f}\nO valor convertido para euro é de: £{:.2f}'.format(r/6.0193, r/6.6399))