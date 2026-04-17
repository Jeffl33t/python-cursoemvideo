def linha(tamanho = 30):
    return '-' * tamanho


def cabecalho(txt):
    print(linha())
    print(txt)
    print(linha())


def menu():
    cabecalho(f'{"MENU PRINCIPAL":^30}')
    print(f'\033[1;33m 1\033[m -\033[1;34m Ver pessoas cadastradas\033[m')
    print(f'\033[1;33m 2\033[m -\033[1;34m Cadastrar nova pessoa\033[m')
    print(f'\033[1;33m 3\033[m -\033[1;34m Sair do sistema\033[m')
    print(linha())
