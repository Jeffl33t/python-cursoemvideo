def leiaint(txt):
    while True:
        try:
            numero = int(input(txt))

        except (ValueError, TypeError):
            print('ERRO: por favor, digite um número inteiro.')
            continue

        except KeyboardInterrupt:
            print('O usuário optou por não informar um número inteiro.')
            return 0

        else:
            print(f'Voçê digitou o número inteiro {numero}')
            return numero


def leiafloat(txt):
    numero = ''
    while True:
        try:
            entrada = str(input(txt)).replace(',', '.').strip()
            numero = float(entrada)

            if numero % 1 == 0:
                print('ERRO: por favor, digite um número real.')

        except (ValueError, TypeError):
            print('ERRO. por favor, digite um número real.')
            continue

        except KeyboardInterrupt:
            print('O usuário optou por não informar um número real.')
            return 0

        else:
            print(f'Voçê digitou o número real {entrada}')
            return numero


ni = leiaint('Digite um número inteiro: ')
nr = leiafloat('Digite um número real: ')


