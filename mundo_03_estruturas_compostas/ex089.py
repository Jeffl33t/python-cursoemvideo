'''lista = list()
alunos = list()
completa = list()
while True:
    lista.append(str(input('Nome do aluno: ')))
    lista.append(float(input('Nota 1: ')))
    lista.append(float(input('Note 2: ')))
    alunos.append(lista[:])
    lista.clear()
    for p in alunos:
        media = (p[1] + p[2]) / 2
        alunos.append(media)
        completa.append(alunos[:])
        alunos.clear()
    opcao = ' '
    while opcao not in 'SsNn':
        opcao = str(input('Continuar [S/N]: '))
    if opcao in 'Nn':
        break
print(f'{'N°  NOME':<15} {'MÉDIA':>15}')
print(f'-' * 32)
for p, a in enumerate(completa):
    print(f'{f'{p}   {a[0][0]}':<15} {f'{a[1]:.1f}':>15}')
print('-' * 32)
while True:
    notas = (int(input('Mostra notas de qual aluno (999 parar): ')))
    for p, a in enumerate(completa):
        if notas == p:
            print(f'Notas de {a[0][0]} são {a[0][1:3]}')
            print('-=' * 16)
    if notas == 999:
        break
print(f'{'<<<< PROGRAMA TERMINADO >>>>':^32}')'''

#cod2

alunos = []
while True:
    nome = str(input('Digite o nome: ')).title()
    nota1 = float(input('Digite a nota 1: '))
    nota2 = float(input('Digite a nota 2: '))
    media = (nota1 + nota2) / 2
    alunos.append([nome, [nota1, nota2], media])
    opcao = str(input('Continuar [S/N]: '))
    if opcao in 'Nn':
        break
print('-' * 30)
print(f'{'N° NOME':<10}{'MÉDIA':>10}')
print('-' * 30)
for i, a in enumerate(alunos):
    print(f'{i:<3}{a[0]:<5}{a[2]:>10}')
print('-=' * 30)
while True:
    opc = int(input('Ver nota do aluno (999 parar): '))
    if opc <= len(alunos) - 1:
        print(f'Notas de {alunos[opc][0]} são {alunos[opc][1]}')
        print('-=' * 30)
    if opc == 999:
        break
print(f'{'<<<< PROGRAMA TERMINADO >>>>':^30}')

