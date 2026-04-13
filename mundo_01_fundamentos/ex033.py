#Veirificar qual é o maior e o menor número
print('Type three numbers to find out the higher and lower between them.')

num1 = float(input('Enter the first number:'))
num2 = float(input('Enter the second number:'))
num3 = float(input('Enter the third number:'))

if num1 < num2 > num3:
    print('The higher number is {}.'.format(num2))

elif num1 < num3 > num2:
    print('The higher number is {}.'.format(num3))

elif num2 < num1 > num3:
    print('The higher number is {}.'.format(num1))

if num1 > num2 < num3:
    print('The lower number is {}.'.format(num2))

elif num1 > num3 < num2:
    print('The lower number is {}.'.format(num3))

elif num2 > num1 < num3:
    print('The lower number ir {}.'.format(num1))

#Versão 2
a = int(input('Enter the first number:'))
b = int(input('Enter the second number:'))
c = int(input('Enter the third number:'))
lower = a

if b < a and b < c:
    lower = b

elif c < a and c < b:
    lower = c

higher = a

if b > a and b > c:
    higher = b

elif c > a and c > b:
    higher = c

print('The lower number is {}.'.format(lower))
print('The hiher number is {}.'.format(higher))

