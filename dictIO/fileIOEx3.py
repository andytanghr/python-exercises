filename = input('Enter a filename: ')
with open(filename, 'r') as fileHandle:
  contents = fileHandle.read()
print(contents)
