#Converter temperatura de celsius para fahrenheit
c = int(input('Insira a temperatura em c°: c°'))
f = c*1.8+32

print('A temperatura de c°{} é de f°{}.'.format(c, f))

#Versão 2
c = int(input('Insira a temperatura em c°: c°'))

print('A temperatura de c°{} é de f°{}.'.format(c, c*1.8+32))