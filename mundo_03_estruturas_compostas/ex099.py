from time import sleep


# Criar uma função que informe o maior valor recebido como parâmetro
def maior(* num):
    valorm = 0
    print('-=' * 30)
    print(f'Analisando valores passados...')

    for i, v in enumerate(num):
        if i == 0 or v > valorm:
            valorm = v

        print(f'{v}', end=' ')
        sleep(0.5)

    print(f'Foram informados ao todo {len(num)} valores.')
    print(f'O maior valor informado foi {valorm}.')

# Programa principal
maior(1, 2, 3, 4, 5, 6, 7)
maior(2, 4, 5, 9, 3, 4)
maior(0)
maior()
