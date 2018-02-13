import json

phonebook = {
  'Melissa': {
    'number': '584-394-5857',
    'email': 'melissa@melissa.com',
    'website': 'www.melissa.com'
  }
}

def displayMenu():
  menu = '''
  Electronic Phone Book
  =====================
  1. Look up an entry
  2. Set an entry
  3. Delete an entry
  4. List all entries
  5. Save entries
  6. Restore saved entries
  7. Quit
  '''
  print(menu)
  choice = int(input('What do you want to do (1-7)? '))
  if choice == 1:
    return printContact()

  elif choice == 2:
    return addContact()

  elif choice == 3:
    return delContact()

  elif choice == 4:
    return listAll()

  elif choice == 5:
    return savePhonebook()

  elif choice == 6:
    return restorePhonebook()

  elif choice == 7:
    print('Bye.')
    return quit()
    
# menu choice 1
def printContact():
  name = input('Name: ')
  while True:
    if name not in phonebook:
      name = input('Name not found. Enter name: ')
    else:
      number = phonebook[name]['number']
      email = phonebook[name]['email']
      website = phonebook[name]['website']
      print('Found entry for {}: {}\n{}\n{}'.format(name, number, email, website))
      return displayMenu()

# menu choice 2
def addContact():
  newName = input('Name: ')
  newNumber = input('Number: ')
  newEmail = input('Email: ')
  newWebsite = input('Website: ')
  phonebook[newName] = {'number': newNumber, 'email':newEmail, 'website':newWebsite}
  print('Entry stored for {}.'.format(newName))
  return displayMenu()

# menu choice 3
def delContact():
  name = input('Name: ')
  while True:
    if name not in phonebook:
      name = input('Name not found. Enter name: ')
    else:
      print('Entry deleted for {}.'.format(name))
      del phonebook[name]
      return displayMenu()

# menu choice 4
def listAll():
  for key, value in phonebook.items():
    print('Found entry for {}: {}'.format(key, value))
  return displayMenu()

# menu choice 5
def savePhonebook():
  with open('phonebook.json', 'w') as data:
    json.dump(phonebook, data)
  print('Entries saved to phonebookdata.json\n')
  return displayMenu()

# menu choice 6
def restorePhonebook():
  with open('phonebook.json', 'r') as data:
    global phonebook
    phonebook = json.load(data)
  print('Restored saved entries.')
  return displayMenu()

displayMenu()