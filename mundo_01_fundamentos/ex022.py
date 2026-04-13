<<<<<<< HEAD
#Análisando uma string
nome = str(input('Digite seu nome completo:')).strip()

print('Seu nome maiusculo é: {}'.format(nome.upper()))
print('Seu nome minusculo é: {}'.format(nome.lower()))
print('Seu nome tem ao todo {} letras.'.format(len(nome) - nome.count(' ')))
=======
#Análisando uma string
nome = str(input('Digite seu nome completo:')).strip()

print('Seu nome maiusculo é: {}'.format(nome.upper()))
print('Seu nome minusculo é: {}'.format(nome.lower()))
print('Seu nome tem ao todo {} letras.'.format(len(nome) - nome.count(' ')))
>>>>>>> db6fe22adc334c96809c710d30b7cd66b02d7359
print('Seu primeiro nome tem {} letras.'.format(nome.find(' ')))