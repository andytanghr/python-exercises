encrypted = input('Enter encrypted text to decode: ')
cipher = 13 # 13 for Caesar shift
decrypted = ['']
for char in range(len(encrypted)):
    if not encrypted[char].isalpha() or encrypted[char].isspace():
        decrypted.append(encrypted[char])
    if encrypted[char].isalpha():
        if encrypted[char].isupper():
            # letter = ord(encrypted[char]) - 65
            # letter += cipher
            # letter = chr((letter % 26) + 65)
            letter = chr(((ord(encrypted[char]) - 65) + cipher) % 26 + 65)
            decrypted.append(letter)
        if encrypted[char].islower():
            # letter = ord(encrypted[char]) - 97
            # letter += cipher
            # letter = chr((letter % 26) + 97)
            letter = chr(((ord(encrypted[char]) - 97) + cipher) % 26 + 97)
            decrypted.append(letter)
print(''.join(decrypted))