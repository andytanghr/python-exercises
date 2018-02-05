subtotal = float(input('Total bill amount? '))
service = input('Level of service? ').lower()
if service == 'good':
    print('Tip amount: ${}'.format(.2 * subtotal))
    print('Total amount: $'.format(1.2 * subtotal))
elif service == 'fair':
    print('Tip amount: ${}'.format(.15 * subtotal))
    print('Total amount: $'.format(1.15 * subtotal))
elif service = 'bad'
    print('Tip amount: ${}'.format(.1 * subtotal))
    print('Total amount: $'.format(1.1 * subtotal))