class Person:
  def __init__(self, name, email, phone):
    self.name = name 
    self.email = email
    self.phone = phone
    self.friends = []
    self.greeting_count = 0
    self.greeted = []

  def greet(self, other_person):
    print('Hello {}, I am {}!'.format(other_person.name, self.name))
    self.greeting_count += 1
    self.greeted.append(other_person.name)

  def print_contact_info(self):
    print('{0}\'s email: {1}, {0}\'s phone number: {2}'.format(self.name, self.email, self.phone))
  
  def add_friend(self, other_person):
    self.friends.append(other_person)
  
  def num_friends(self):
    print(len(self.friends))

  def __str__(self):
    return 'Person: {} {} {}'.format(self.name, self.email, self.phone)

  def num_unique_people_greeted(self):
    len(greeted)



class Vehicle:
  def __init__(self, make, model, year):
    self.make = make
    self.model = model
    self.year = year
  
  def print_info(self):
    print(self.year, self.make, self.model)

  





sonny = Person('Sonny', 'sonny@hotmail.com', '483-485-4948')
jordan = Person('Jordan', 'jordan@aol.com', '495-586-3456')
# sonny.greet(jordan)
# jordan.greet(sonny)
# print(sonny.email, sonny.phone)
# print(jordan.email, jordan.phone)
# sonny.print_contact_info()
# jordan.friends.append(sonny)
# sonny.friends.append(jordan)
# print(len(jordan.friends))
# print(jordan.friends)
# jordan.add_friend(sonny)
# jordan.add_friend(sonny)
# jordan.add_friend(sonny)
# print(jordan.friends)
# jordan.num_friends()

# print(sonny.greeting_count)
# sonny.greet(jordan)
# print(sonny.greeting_count)
# sonny.greet(jordan)
# print(sonny.greeting_count)

print(jordan)

# car = Vehicle('Nissan', 'Leaf', 2015)
# print(car.make, car.model, car.year)
# car.print_info()