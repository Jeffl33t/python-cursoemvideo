#Receber três valores e verificar se é possível formar um triângulo
lado1 = float(input('Insira o tamanho do primeiro lado do triângulo:'))
lado2 = float(input('Insira o tamanho do segundo lado do triângulo:'))
lado3 = float(input('Insira o tamanho do terceiro triângulo:'))

if lado1 + lado2 > lado3 and lado1 + lado3 > lado2 and lado2 + lado3 > lado1:
    print('É possível formar um triângulo')

else:
    print('Não é possível formar um triângulo.')

#Se a + b precisa ser maior que c, a + c precisa ser maior que b e b + c precisa ser maior que a.