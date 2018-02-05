subtotal = float(input('Total bill amount? '))
service = input('Level of service? ').lower()
tips = {'good' : 1.2, 'fair' : 1.15, 'bad':1.1}
tip = tips[service]
total = tip * subtotal
print('Tip amount: ${:.2f}'.format(tip))
print('Total amount: ${:.2f}'.format(total))
# #use a dictionary to convert level of service to percent tip?
# if service == 'good':
#     print('Tip amount: ${:.2f}'.format(.2 * subtotal))
#     print('Total amount: ${:.2f}'.format(1.2 * subtotal))
# elif service == 'fair':
#     print('Tip amount: ${:.2f}'.format(.15 * subtotal))
#     print('Total amount: ${:.2f}'.format(1.15 * subtotal))
# elif service == 'bad':
#     print('Tip amount: ${:.2f}'.format(.1 * subtotal))
#     print('Total amount: ${:.2f}'.format(1.1 * subtotal))