filename = input('Enter a filename: ')
contents = ''
with open(filename, 'w') as fileHandle:
  while True:
    contents = input('Enter file contents (Enter nothing to break): ')
    if contents == '':
      break
    else:
      fileHandle.write(contents)
