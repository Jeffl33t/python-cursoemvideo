def notas(* num, sit=False):
    """

    :param num: notas do aluno que serão analisadas
    :param sit: (opcional) mostrar a situação do aluno
    :return: mostra o total de notas, maior nota, menor nota, média e situação do aluno
    """
    aluno = dict()
    maior = menor = media = 0

    for i, n in enumerate(num):
        aluno['total'] = len(num)
        aluno['maior'] = maior
        aluno['menor'] = menor
        aluno['média'] = media
        media += n / len(num)

        if i == 0 or  n > maior:
            maior = n

        if i == 0 or n < menor:
            menor = n

    if sit:
        if media < 6:
            aluno['situação'] = 'ruim'

        elif 6 < media <= 7:
            aluno['situação'] = 'razoável'

        else:
            aluno['situação'] = 'ótima'

    return aluno


# Programa principal
resp = notas(7, 9, 9, 9, sit=True)
print(resp)

# Gabarito

def notas(*num, sit=False):
    aluno = dict()
    aluno['total'] = len(num)
    aluno['maior'] = max(num)
    aluno['menor'] = min(num)
    aluno['média'] = sum(num) / len(num)

    if sit:
        if aluno['média'] > 7:
            aluno['situação'] = 'ÓTIMA'

        elif 7 > aluno['média'] >= 5:
            aluno['situação'] = 'RAZOÁVEL'

        else:
            aluno['média'] = 'RUIM'

    return aluno


resp = notas(9, sit=True)
print(resp)