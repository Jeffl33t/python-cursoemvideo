def aumentar(num=0, taxa=0, form=False):
    res = num + (num * taxa / 100)
    return res if form is False else moeda(res)


def diminuir(num=0, taxa=0, form=False):
    res = num - (num * taxa / 100)
    return res if form is False else moeda(res)


def dobro(num=0, form=False):
    res = num * 2
    return res if not form else moeda(res)


def metade(num=0, form=False):
    res = num / 2
    return res if not form else moeda(res)


def moeda(num=0.0, cifra='R$'):
    return f'{cifra}{num:>.2f}'.replace('.',',')

def resumo(num=0, aum=10, red=5):
    print('-' * 30)
    print(f'{'RESUMO DE VALOR':^30}')
    print('-' * 30)
    print(f'Preço analisado: \t{moeda(num)}')
    print(f'Dobro do preço: \t{dobro(num, True)}')
    print(f'Metade do preço: \t{metade(num, True)}')
    print(f'{aum:>2}% de aumento: \t{aumentar(num, aum, True)}')
    print(f'{red:>2}% de redução: \t{diminuir(num, red, True)}')
    print('-' * 30)