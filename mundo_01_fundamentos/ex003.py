#Soma de variáveis
print('\033[4mDigite dois numeros e descubra sua soma\033[m!!!\n')

n1 = int(input('\033[0;31mDigite um numero\033[m:'))
n2 = int(input('\033[0;31mDigite mais um numero:\033[m'))
s = n1+n2

print('\nA soma de \033[1;31m{}\033[m + \033[1;34m{}\033[m é = \033[1;35m{}'.format(n1, n2, s))