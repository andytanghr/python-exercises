filename = input('Enter a filename: ')
contents = ''
with open(filename, 'w') as file_handle:
  while True:
    contents = input('Enter file contents (Enter nothing to break): ')
    if contents == '':
      break
    else:
      file_handle.write(contents)
