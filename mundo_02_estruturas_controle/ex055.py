#Verificar maior e menor peso
print('\033[1;34mENTER 5 WEIGHTS TO FIND OUT THE LARGEST AND SMALLEST AMONG THEM.\033[m\n')

lst = []

for c in range(0, 5):
    weight = float(input('Enter de weight(Kg):'))
    lst.append(weight)

low = min(lst)
high = max(lst)

print('largest weight: {}\nSmallest weight: {}'.format(high, low))

#gabarito
maior = 0
menor = 0

for p in range(1, 6):
    peso = float(input('Digite o peso da {} pessoa:'.format(p)))

    if p == 1:
        maior = peso
        menor = peso

    else:
        if peso > maior:
            maior = peso

        if peso < menor:
            menor = peso

print('O maior peso é {}Kg'.format(maior))
print('O menor peso é {}Kg'.format(menor))