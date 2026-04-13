<<<<<<< HEAD
#Calcular o preço de uma passagem de acordo com à distância
distancia = int(input('Digite a distancia do seu destino:'))

if distancia <= 200:
    print('O preço da sua passagem é de: R${}'.format(distancia * 0.50))

else:
    print('O preço da sua passagem é de: R${}'.format(distancia * 0.45))

#gabarito
distancia = float(input('Qual é a distancia da sua viajem?'))
print('Você está prestes a começar uma viagem de {}Km'.format(distancia))

if distancia <= 200:
    preco = distancia * 0.50

else:
    preco = distancia * 0.45

=======
#Calcular o preço de uma passagem de acordo com à distância
distancia = int(input('Digite a distancia do seu destino:'))

if distancia <= 200:
    print('O preço da sua passagem é de: R${}'.format(distancia * 0.50))

else:
    print('O preço da sua passagem é de: R${}'.format(distancia * 0.45))

#gabarito
distancia = float(input('Qual é a distancia da sua viajem?'))
print('Você está prestes a começar uma viagem de {}Km'.format(distancia))

if distancia <= 200:
    preco = distancia * 0.50

else:
    preco = distancia * 0.45

>>>>>>> db6fe22adc334c96809c710d30b7cd66b02d7359
print('O preço de sua passagem sera de R${:.2f}'. format(preco))