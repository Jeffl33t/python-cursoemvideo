<<<<<<< HEAD
#Buscando uma palavra específica em uma frase
cidade = str(input('Digite o nome de uma cidade:'))
c = cidade.strip().capitalize()

print('Santo'in c)

#Versão 2
cidade = str(input('Digite o nome de uma cidade:')).strip().capitalize()
print(cidade[:5] == 'Santo')

#Versão 3
cidade = str(input('Digite o nome de uma cidade:')).strip().upper()
print(cidade[:5] == 'SANTO')

=======
#Buscando uma palavra específica em uma frase
cidade = str(input('Digite o nome de uma cidade:'))
c = cidade.strip().capitalize()

print('Santo'in c)

#Versão 2
cidade = str(input('Digite o nome de uma cidade:')).strip().capitalize()
print(cidade[:5] == 'Santo')

#Versão 3
cidade = str(input('Digite o nome de uma cidade:')).strip().upper()
print(cidade[:5] == 'SANTO')

>>>>>>> db6fe22adc334c96809c710d30b7cd66b02d7359
