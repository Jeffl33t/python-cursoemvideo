from time import sleep


# Criar um contador de passos
def contador(inicio, fim, passo):
    if passo == 0:
        passo = 1

    if passo < 0:
        passo *= (-1)

    print('-=' * 20 )
    print(f'Contagem de {inicio} até {fim} de {passo} em {passo}.')

    # Contar de trás para a frente
    if inicio > fim:
        for c in range(inicio, fim - 1, -passo):
            print(c, end=' ')
            sleep(0.5)

    else:
        for c in range(inicio, fim + 1, passo):
            print(c, end=' ')
            sleep(0.5)

    print('FIM')

# Programa principal
contador(1, 10, 1)
contador(10, 0, -2)
print('-=' * 20)
print('Contagem personalizada:')
i = int(input('Inicio: '))
f = int(input('Fim...: '))
p = int(input('Passo.: '))
contador(i, f, p)
