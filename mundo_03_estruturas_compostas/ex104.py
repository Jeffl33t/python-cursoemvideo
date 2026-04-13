# Criar uma função que leia um inteiro
def leiaint(txt):
    ok = False
    valor = 0

    while not ok:
        num = str(input(txt))

        if num.isnumeric():
            valor = int(num)
            ok = True

        else:
            print(f'Valor Inválido. \'{num}\' Tente novamente')

    return valor


# Programa principal
n = leiaint('Digite um número: ')
print(f'Voce digitou o número {n}')


