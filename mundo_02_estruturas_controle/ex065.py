<<<<<<< HEAD
#Mostrar o maior, menor e a média entre os números recebidos
soma = contador = maior = menor = media = 0
resposta = 'S'

while resposta in 'Ss':
    numero = int(input('Digite um número:'))
    contador += 1
    soma += numero
    resposta = str(input('Continuar [S/N]:')).upper()
    media = soma / contador

    if contador == 1:
        maior = menor = numero

    else:
        if maior < numero:
            maior = numero

        if menor > numero:
            menor = numero

print('O MAIOR número digitado é {}, o MENOR é {} e a MÉDIA {}'.format(maior, menor, media))



=======
#Mostrar o maior, menor e a média entre os números recebidos
soma = contador = maior = menor = media = 0
resposta = 'S'

while resposta in 'Ss':
    numero = int(input('Digite um número:'))
    contador += 1
    soma += numero
    resposta = str(input('Continuar [S/N]:')).upper()
    media = soma / contador

    if contador == 1:
        maior = menor = numero

    else:
        if maior < numero:
            maior = numero

        if menor > numero:
            menor = numero

print('O MAIOR número digitado é {}, o MENOR é {} e a MÉDIA {}'.format(maior, menor, media))



>>>>>>> db6fe22adc334c96809c710d30b7cd66b02d7359
