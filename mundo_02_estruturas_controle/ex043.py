#Calcular o IMC
print('\033[1;34mINSIRA SUAS MEDIDAS PARA SABER SEU IMC')

peso = float(input('Insira seu peso (Kg):'))
altura = float(input('Insira sua altura (m):'))
imc = peso / (altura ** 2)

if imc <= 18.5:
    print('Abaixo {:.2f}'.format(imc))

elif imc <= 25:
    print('Ideal {:.2f}'.format(imc))

elif imc <=30:
    print('Sobre {:.2f}'.format(imc))

elif imc <= 40:
    print('Obesidade {:.2f}'.format(imc))

else:
    print('Obesidade Mórbida {:.2f} '.format(imc))
