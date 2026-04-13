#Calcular a PA de um número
print('\033[1;34mGERADOR DE PA\033[m\n')

primeiro = int(input('Primeiro termo:'))
razao = int(input('Razão:'))
c = 0

while c < 10:
    c += 1
    pa = primeiro + (c - 1) * razao
    print(pa, end='→ ')
