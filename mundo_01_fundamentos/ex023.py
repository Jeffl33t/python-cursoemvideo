<<<<<<< HEAD
#Separar e contar unidade, dezena, centena e milhar de um número
num = int(input('Digite um numero:'))

num1 = num // 1 % 10
num2 = num // 10 % 10
num3 = num // 100 % 10
num4 = num // 1000 % 10

print('Unidade: {}\nDezena: {}\nCentena: {}\nMilhar: {}'.format(num1, num2, num3, num4))

#cod. outra forma de fazer.(gabarito)*só funciona se o numero tiver 4 digitos
num = int(input('Digite um numero:'))
str(num)

print('Analisando o numero: {}'.format(num))
print('Unidade: {}'.format(3))
print('Dezena: {}'.format(2))
print('Centena: {}'.format(1))
=======
#Separar e contar unidade, dezena, centena e milhar de um número
num = int(input('Digite um numero:'))

num1 = num // 1 % 10
num2 = num // 10 % 10
num3 = num // 100 % 10
num4 = num // 1000 % 10

print('Unidade: {}\nDezena: {}\nCentena: {}\nMilhar: {}'.format(num1, num2, num3, num4))

#cod. outra forma de fazer.(gabarito)*só funciona se o numero tiver 4 digitos
num = int(input('Digite um numero:'))
str(num)

print('Analisando o numero: {}'.format(num))
print('Unidade: {}'.format(3))
print('Dezena: {}'.format(2))
print('Centena: {}'.format(1))
>>>>>>> db6fe22adc334c96809c710d30b7cd66b02d7359
print('Milhar: {}'.format(0))