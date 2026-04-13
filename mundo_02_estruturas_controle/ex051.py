#Mostrar a PA de um número
print('\033[1;34mDIGITE UM NÚMERO PARA SABER A PA DELE\033[m\n')

primeiro = int(input('Primeiro termo:'))
razao = int(input('Razão:'))
decimo = primeiro + (10 - 1) * razao

for c in range(primeiro, decimo + razao, razao):
    print('{}-> '.format(c), end= '')

print(decimo + razao)
