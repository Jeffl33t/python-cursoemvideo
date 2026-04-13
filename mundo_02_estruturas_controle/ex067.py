<<<<<<< HEAD
#Mostrar a tabuada de um número
while True:
    num = int(input('Quer ver a tabuáda de qual valor:'))

    if num <= 0:
        break

    for c in range(1, 11):
        print(f'{c:>2} x {num} = {c*num}')

=======
#Mostrar a tabuada de um número
while True:
    num = int(input('Quer ver a tabuáda de qual valor:'))

    if num <= 0:
        break

    for c in range(1, 11):
        print(f'{c:>2} x {num} = {c*num}')

>>>>>>> db6fe22adc334c96809c710d30b7cd66b02d7359
print('FIM')