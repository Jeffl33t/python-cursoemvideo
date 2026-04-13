#Criar uma lista de palavras, verificar e mostrar as vogais para cada palavra
print('\033[1;34mCRIE UM PROGRAMA QUE MOSTRA AS VOGAIS DE PALAVRAS DENTRO DE UMA TUPLA\033[m\n')

palavras = ('ESTUDAR', 'APRENDER', 'PROGRAMADOR', 'ESTUDANTE', 'ESFORÇO', 'VONTADE', 'DETERMINAÇAO', 'CHEGADA')
vogais = 'AEIOU'

for palavra in palavras:
    vog = ''

    for letra in palavra:
        if letra in vogais:
            vog += letra

    print(f'À palavra {palavra} possui as vogais {vog}')

#gabarito

palavras = ('ESTUDAR', 'APRENDER', 'PROGRAMADOR', 'ESTUDANTE', 'ESFORÇO', 'VONTADE', 'DETERMINAÇAO', 'CHEGADA')
for palavra in palavras:
    print(f'\nNa palavra {palavra} temos as vogais ', end='')

    for letra in palavra:
        if letra.upper() in 'AEIOU':
            print(f'{letra}', end=' ')
