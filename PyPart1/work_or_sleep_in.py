days = ['Sunday', 'Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday']
inputDay = int(input('Day (0-6)? '))
if inputDay == 0 or inputDay == 6:
    print('Sleep in')
else:
    print('Go to work')