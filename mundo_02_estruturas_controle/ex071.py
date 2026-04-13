#Simular um caixa eletrônico
re1 = re2 = re3 = 0

valor = int(input('Valor á sacar: R$'))
re = valor // 50

if valor % 50 != 0:
    re1 = valor % 50 // 20
    re2 = valor % 50 % 20 // 10
    re3 = valor % 50 % 20 % 10 // 1

print(f"total de cédulas: \n- R$50 = {re} \n- R$20 = {re1} \n- R$10 = {re2} \n- R$1  = {re3}")


#gabarito
valor = int(input('Digite o valor a sacar: R$'))
total = valor
ced = 50
totced = 0

while True:
    if total >= ced:
        total -= ced
        totced += 1

    else:
        if totced > 0:
            print(f'O total de cédulas são {totced}: R$ {ced} ')

        if ced == 50:
            ced = 20

        elif ced == 20:
            ced = 10

        elif ced == 10:
            ced = 1
        totced = 0

        if total == 0:
            break