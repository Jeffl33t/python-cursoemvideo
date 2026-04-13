#Verificar se uma expressão é válida
lista = []
expre = str(input('Digite a expressão: '))

# Verificar parênteses
for i in expre:
    # Verificar se a expressão começa com parêntese aberto
    if i in '(':
        lista.append('(')

    # Verificar se a expressão termina com parêntese fechado
    elif i in ')':
        # Se parêntese não foi aberto então será removido o parêntese fechado
        if len(lista) > 0:
            lista.pop()
        # Se parêntese foi aberto então parêntese fechado é adicionado
        else:
            lista.append(')')
        break

# Retornar se a expressão é válida
if len(lista) == 0:
    print('Expressão válida.')

else:
    print('Expressão inválida.')







