#Análisando a entrada do teclado
print('\033[4m\033[1mDigite algo para para que seja análisado\033[m:\n')

d = input('\033[4m\033[1mO que voce quer analisara?\033[m:')

print('O tipo primitivo desse valor é', type(d))
print('Tem numeros?', d.isnumeric())
print('Tem letras?', d.isalpha())
print('É um alfanumerico?',d.isalnum())
print('Tem maiusculas?', d.isupper())
print('Tem minusculas', d.islower())
print('Esta capitalizada', d.istitle())