from mundo_03_estruturas_compostas.ex115.lib.interface import *
from mundo_03_estruturas_compostas.ex115.lib.funcoes import *
from time import sleep


while True:
    menu()
    entrada = valida_opcao()
    if entrada == 1:
        cabecalho('CONSULTAR CADASTRO')
        lista_cadastro('cadastro.txt')
        sleep(1)

    elif entrada == 2:
        cabecalho('NOVO CADASTRO')
        cadastra_pessoa('cadastro.txt')
        sleep(1)

    elif entrada == 3:
        print('-' * 30)
        print('<<<  PROGRAMA ENCERRADO  >>>')
        break
