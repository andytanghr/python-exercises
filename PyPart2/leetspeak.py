string = input('Input text to convert to l33tspeak: ')
leetDict = {
    'A': '4',
    'E': '3',
    'G': '6',
    'I': '1',
    'O': '0',
    'S': '5',
    'T': '7'
}

stringLeet = ''
for character in string:
    if character.upper() in leetDict:
        stringLeet += leetDict[character.upper()]
    else:
        stringLeet += character
print(stringLeet)
