#Verificar tipo de triângulos
print('\033[1;34mDIGITAR TRÊS MEDIDAS PARA SABER SE ELAS PODEM FORMAR UM TRIÂNGULO E SE SIM DE QUE TIPO\033[m\n')

lado1 = float(input('Digite a primeira medida:'))
lado2 = float(input('Digite a segunda medida:'))
lado3 = float(input('Digite a terceira medida:'))

if lado1 + lado2 > lado3 and lado1 + lado3 > lado2 and lado2 + lado3 > lado1:
    print('\nÈ possível formar um triângulo.\n')

    if lado1 == lado2 == lado3:
        print('O triângulo formado é do tipo Equilátero.')

    elif lado1 == lado2 != lado3 or lado1 == lado3 != lado2 or lado2 == lado3 != lado1:
        print('O triângulo formado é do tipo Isósceles.')

    elif lado1 != lado2 != lado3 != lado1:
        print('O triângulo formado é do tipo Escaleno.')
else:
    print('\nNão é possível formar um triângulo.')

#gabarito
l1 = float(input('Digite o primeiro lado:'))
l2 = float(input('Digite o segundo lado:'))
l3 = float(input('Difite o terceiro lado:'))

if l1 < l2 + l3 and l2 < l1 + l3 and l3 < l1 + l2:
    print('\nÈ possível formar um triângulo.\n')

    if l1 == l2 == l3:
        print('O triângulo formado é do tipo EQUILÁTERO.')

    elif l1 != l2 != l3 != l1:
        print('O triângulo formado é do tipo ESCALENO')

    elif l1 == l2 != l3 or l2 == l3 != l1 or l1 == l3 != l2:
        print('O triângulo formado é do tipo ISÓSCELES')
   #else:
       #print('O triângulo formado é do tipo ISÓSCELES')
else:
    print('Não é possível formar um TRIÂNGULO')