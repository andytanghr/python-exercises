filename = input('Enter a filename to read: ')
with open(filename, 'r') as file_handle:
  contents = file_handle.read()
  print(contents)

