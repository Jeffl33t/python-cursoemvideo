# Criar uma função que verifique a obrigatoriedade do voto
def voto(nasc):
    from datetime import date
    idade = date.today().year - nasc

    if idade >= 60 or idade < 18 >= 16:
        return f'Com {idade} anos: VOTO OPCIONAL'

    elif idade >= 18:
        return f'Com {idade} anos: VOTO OBRIGATÓRIO'

    else:
        return f'Com {idade} anos: NEGADO'


# Programa principal
ano = int(input('Ano de nascimento: '))
print(voto(ano))