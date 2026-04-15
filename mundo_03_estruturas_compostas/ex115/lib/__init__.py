def menu():
    print('-' * 30)
    print(f'{"MENU PRINCIPAL":^30}')
    print('-' * 30)
    print(f'\033[1;33m 1\033[m -\033[1;34m Ver pessoas cadastradas\033[m')
    print(f'\033[1;33m 2\033[m -\033[1;34m Cadastrar nova pessoa\033[m')
    print(f'\033[1;33m 3\033[m -\033[1;34m Sair do sistema\033[m')
    print('-' * 30)


def valida_opcao():
    while True:
        try:
            opcao = int(input("\033[1;32mSua Opção: \033[m"))
            if opcao in (1, 2, 3):
                return opcao
            else:
                print(f'\033[1;31mErro: Opção invalida. Digite 1, 2 ou 3.\033[m')

        except (ValueError, TypeError):
            print(f'\033[1;31mErro: Digite apenas números.\033[m')


def cadastra_pessoa(nome_arquivo):
    print('-' * 30)
    print(f'{"CADASTRAR PESSOA":^30}')
    print('-' * 30)

    while True:
        nome = str(input('Digite o nome: ')).strip()
        if nome.replace(' ', '').isalpha():
            break
        print(f'\033[1;31mErro: Nome pode conter apenas letras.\033[m')

    while True:
        try:
            idade = int(input('Digite a idade: '))
            break
        except (ValueError, TypeError):
            print(f'\033[1;31mErro: Idade pode conter apenas números.\033[m')

    try:
        with open(nome_arquivo, 'a', encoding='utf-8') as arquivo:
            arquivo.write(f'{nome};{idade}\n')
    except:
        print(f'\033[1;31mHouve um erro ao gravar os dados.\033[m')
    else:
        print(f'\033[1;32mNovo registro adicionado com sucesso!\033[m')

    return nome, idade


def lista_cadastro(nome_arquivo):
    print('-' * 30)
    print(f'{"PESSOAS CADASTRADAS":^30}')
    print('-' * 30)

    try:
        with open(nome_arquivo, 'rt', encoding='utf-8') as arquivo:
            for linha in arquivo:
                dado = linha.replace('\n', '').split(';')
                print(f'{dado[0]:<20} {dado[1]:>3} anos')

    except FileNotFoundError:
        print('\033[1;31mArquivo não encontrado ou vazio.\033[m')
    except:
        print(f'\033[1;31mErro ao ler arquivo.\033[m')