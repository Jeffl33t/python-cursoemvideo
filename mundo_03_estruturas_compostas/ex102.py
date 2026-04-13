def fatorial(num, show=False):
    """
    -> Calcula o fatorial de um número
    :param num: Recebe o número que será calculado o fatorial
    :param show: (Opcional) Mostra o fatorial completo ou apenas o resultado
    :return: Retorna o fatorial de um número (num)
    """
    f = 1
    for c in range(num, 0, -1):
        f *= c

        if show:
            print(f'{c}', end='')

            if c > 1:
                print(f' x ', end='')

            else:
                print(f' = ', end='')

    return f


# Programa principal
print(fatorial(4, show=True))