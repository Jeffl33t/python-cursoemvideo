def leia_dinheiro(txt):
    valido = False

    while not valido:
        num = str(input(txt)).replace(',', '.').strip()

        if num.isalpha() or num == '':
            print(f'\033[1;31mERRO: "{num}" é um preço inválido.\033[m')

        else:
            valido = True
            return float(num)


def leia_num(txt):
    valor = 0

    while True:
        num = str(input(txt)).replace(',', '.').strip()

        if num.isnumeric():
            valor = int(num)
            break

        elif num.replace('.', '').isnumeric():
            valor = float(num)
            break

        else:
            print(f'\033[1;31mERRO: \'{num}\' é um preço inválido.\033[m')

    return valor
