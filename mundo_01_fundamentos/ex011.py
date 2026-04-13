<<<<<<< HEAD
#Calcular a área do quadrado e a quantidade de tinta para pinta la
b = float(input('Largura da parede:'))
h = float(input('Altura da parede:'))

a = b * h
t = a / 2

print('Sua parede possui as dimensões de {}x{} e sua área é de {}m²'.format(b, h, a))
print('Será necessário {}l de tinta para pinta lá'.format(t))

#Versão 2
h = float(input('Largura da parede:'))
b = float(input('Altura da parede:'))

=======
#Calcular a área do quadrado e a quantidade de tinta para pinta la
b = float(input('Largura da parede:'))
h = float(input('Altura da parede:'))

a = b * h
t = a / 2

print('Sua parede possui as dimensões de {}x{} e sua área é de {}m²'.format(b, h, a))
print('Será necessário {}l de tinta para pinta lá'.format(t))

#Versão 2
h = float(input('Largura da parede:'))
b = float(input('Altura da parede:'))

>>>>>>> db6fe22adc334c96809c710d30b7cd66b02d7359
print('Sua parede possui as dimensões de {}x{} e sua área é de {}m².\nSerá necessário {}l de tinta para pinta lá.'.format(h, b, h*b, h*b/2 ))