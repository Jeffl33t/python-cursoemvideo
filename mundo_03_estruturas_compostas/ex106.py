from time import sleep


# Criar um programa que personalize PyHelp
c = ('\033[m',      # 0 limpa
     '\033[1;42m',  # 1 verde
     '\033[1;44m',  # 2 azul
     '\033[7m',     # 3 branco
     '\033[1;41m')  # 4 vermelho


# Acessar o PyHelp
def ajuda(com):
    titulo(f'Acessando o comando \' {com} \'', 2)
    print(c[3], end='')
    help(com)
    print(c[0], end='')
    sleep(2)


# Criar a personalização
def titulo(txt, cor=0):
    tam = len(txt) + 4
    print(f'{c[cor]}', end='')
    print('~' * tam)
    print(txt)
    print('~' * tam)
    print(f'{c[0]}', end='')
    sleep(1)


# Programa principal
comando = ''
while True:
    titulo('  SISTEMA DE AJUDA PyHelp', 1)
    comando = str(input('Função ou Biblioteca >'))

    if comando.upper() == 'FIM':
        break

    else:
        ajuda(comando)

titulo('  FIM', 4)

