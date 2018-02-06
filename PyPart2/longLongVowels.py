# this program assumes long vowels only from 'oo' and 'ee' and not any from silent E. Indeed, 'ee' and 'oo' are considered digraphs and not necessarily long vowels proper
string = input('Input a word to elongate vowels: ')
string = string.replace('ee', 'eeeee')
string = string.replace('oo', 'ooooo')
print(string)