from lib import *
import time

while True:
    menu()
    entrada = valida_opcao()
    if entrada == 1:
        lista_cadastro('cadastro.txt')
        time.sleep(1)

    elif entrada == 2:
        cadastra_pessoa('cadastro.txt')
        time.sleep(1)

    elif entrada == 3:
        print('-' * 30)
        print('<<<  PROGRAMA ENCERRADO  >>>')
        break
