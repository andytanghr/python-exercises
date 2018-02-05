subtotal = float(input('Total bill amount? '))
service = input('Level of service? ').lower()
split = int(input('Split how many ways? '))
tips = {'good' : 1.2, 'fair' : 1.15, 'bad':1.1}
tip = tips[service]
total = tip * subtotal
print('Tip amount: ${:.2f}'.format(tip))
print('Total amount: ${:.2f}'.format(total))
print('Amount per person: {:.2f}'.format(total / split))
# if service == 'good':

# elif service == 'fair':
#     print('Tip amount: ${:.2f}'.format(.15 * subtotal))
#     print('Total amount: ${:.2f}'.format(1.15 * subtotal))
#     print('Amount per person: {}'.format(total= total / split))
# elif service == 'bad':
#     print('Tip amount: ${:.2f}'.format(.1 * subtotal))
#     print('Total amount: ${:.2f}'.format(1.1 * subtotal))
#     print('Amount per person: {}'.format(total= total / split))