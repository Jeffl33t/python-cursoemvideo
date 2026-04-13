<<<<<<< HEAD
#Checar quantas letras "a" existe em uma frase
frase = input('Digite uma frase:').strip().lower()

f = frase.count('a')
a1 = frase.find('a')+1
a2 = frase.rfind('a')+1

print('Na frase digitada exitem {} as.\n'
      'Sendo a primeira posição {} e ultima posição {} .'.format(f, a1, a2))

#Versão 2
frase = str(input('Digite uma frase:')).strip().lower()

print('A frase "{}" possui {} letras as sendo a primera na posição {} e a ultima {}.'
      .format(frase, frase.count('a'), frase.find('a')+1, frase.rfind('a')+1))
=======
#Checar quantas letras "a" existe em uma frase
frase = input('Digite uma frase:').strip().lower()

f = frase.count('a')
a1 = frase.find('a')+1
a2 = frase.rfind('a')+1

print('Na frase digitada exitem {} as.\n'
      'Sendo a primeira posição {} e ultima posição {} .'.format(f, a1, a2))

#Versão 2
frase = str(input('Digite uma frase:')).strip().lower()

print('A frase "{}" possui {} letras as sendo a primera na posição {} e a ultima {}.'
      .format(frase, frase.count('a'), frase.find('a')+1, frase.rfind('a')+1))
>>>>>>> db6fe22adc334c96809c710d30b7cd66b02d7359
