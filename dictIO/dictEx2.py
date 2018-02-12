ramit = {
  'name': 'Ramit',
  'email': 'ramit@gmail.com',
  'interests': ['movies', 'tennis'],
  'friends': [
    {
      'name': 'Jasmine',
      'email': 'jasmine@yahoo.com',
      'interests': ['photography', 'tennis']
    },
    {
      'name': 'Jan',
      'email': 'jan@hotmail.com',
      'interests': ['movies', 'tv']
    }
  ]
}

# 1. Write a Python expression that gets the email address of Ramit.
ramitEmail = ramit['email']
print(ramitEmail)

# 2. Write a Python expression that gets the first of Ramit's interests.
ramitInterest = ramit['interests'][0]
print(ramitInterest)

# 3. Write a Python expression that gets the email address of Jasmine.
jasmineEmail = ramit['friends'][0]['email']
print(jasmineEmail)

# 4. Write a Python expression that gets the second of Jan's two interests.
janInterests = ramit['friends'][1]['interests'][1]
print(janInterests)