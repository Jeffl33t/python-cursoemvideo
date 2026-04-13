price = float(input('Enter the purchase amount: US$'))
form = int(input('\n[1] CASH PAYMENT'
                 '\n[2] INSTALLMENT PAYMENT\n'
                 '\nPayment method:'))
if form == 1:
    cash = int(input('\nPayment method CASH PAYMENT:\n'
                     '\n[1] CASH (discounted 10%)'
                     '\n[2] CHEQUE (discounte 10%)'
                     '\n[3] CREDIT CARD (discounted 5%)\n'
                     '\nChoose payment method:'))

    if cash == 1:
        print('\nPrice to Pay: US${:.2f}'.format(price * 0.9))

    elif cash == 2:
        print('\nPrice to Pay: US${:.2f}'.format(price * 0.9))

    elif cash == 3:
        print('\nPrice to Pay: US${:.2f}'.format(price * 0.95))

if form == 2:
    installment = int(input('\nPayment method INSTALLMENT PAYMENT:\n'
                      '\n[1] CREDIT CARD x 2 (sem juros)'
                      '\n[2] CREDIT CARD x 3 (juros de 20%)\n'
                      '\nChoose how many times:'))

    if installment == 1:
        print('\nPrice to Pay: 2 x US${:.2f}'.format(price / 2))

    elif installment == 2:
        print('\nPrice to Pay: 3 x US${:.2f}'.format((price * 1.2) / 3))
