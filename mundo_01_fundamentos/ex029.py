#Simulação de radar rodoviário
v = float(input('Qual a velocidade:'))
m = (v - 80) * 7
print('Voçê passou no radar em uma velocidade de {}Km/h'.format(v))

if v > 80:
    print('Voçê passou na rodovia á {}Km/h ultrapassando o limite de velocida de 80Km/h, sua multa é: R${:.2f}'.format(v, m))

else:
    print("Voce passou na rodovia dentro do limite de 80Km/h de velocida. Siga em frente e BOA VIAJEM!")

