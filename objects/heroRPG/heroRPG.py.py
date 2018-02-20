#!/usr/bin/env python

# In this simple RPG game, the hero fights the goblin. He has the options to:

# 1. fight goblin
# 2. do nothing - in which case the goblin will attack him anyway
# 3. flee

import random

def main():
  class Character:
    def __init__(self, name, health, power, agility=False, charSkill=False):
      self.name = name
      self.health = health
      self.power = power
      self.agility = agility
      self.charSkill = charSkill

    def alive(self):
      return self.health > 0

    def print_status(self):
      print("The {} has {} health and {} power.".format(self.name, self.health, self.power))

    def attack(self, enemy):
      if enemy.evade():
        print('The {}\'s attack has missed the {}'.format(self.name, enemy))
        return False # False is needed to exit the attack function

      # attack sequence
      # chance to activate charSkill
      if random.randint(1, 100) < 20 and self.charSkill:
        self.charSkill(enemy)
      # no damage to antihero if hero attacks
      elif enemy.name == 'antihero':
        print('The hero\'s attack has missed the antihero. An antihero is his own worst enemy!')
      # medic heals itself if hero attacks
      elif enemy.name == 'medic'and random.randint(1, 100) < 20 and enemy.alive():
        print('The {}\'s attack has missed the {}'.format(self.name, enemy))
        enemy.charSkill()
      
      # attack goes through
      else:
        enemy.health -= self.power #-  enemy.armor
        print("The {} does {} damage to the {}.".format(self.name, self.power, enemy))

      if not enemy.alive():
        print("The {} is dead.".format(enemy))
        
    def evade(self):
        if random.randint(1, 100) < self.agility and self.agility:
            return True
        else: return False

    def __str__(self):
      return self.name

  class Hero(Character):
    def __init__(self):
      self.name = 'hero'
      self.health = 10
      self.maxHealth = 10
      self.power = 5
      self.coins = 20 # default value from hero_rpg_part2.py
      self.armor = 0
      self.agility = 0
    def charSkill(self, enemy):
      enemy.health -= self.power
      print('The {} does {} extra damage to {}'.format(self.name, self.power, enemy))

  class Goblin(Character):
    def __init__(self):
      self.name = 'goblin'
      self.health = 6
      self.power = 2
      self.coins = 5
      self.agility = 1
      self.charSkill = None

  class Medic(Character):
    def __init__(self):
      self.name = "medic"
      self.health = 6
      self.power = 3
      self.coins = 5
      self.agility = False

    def charSkill(self, enemy):
      self.health += 2
      print('The {} has healed and regenerated 2 hp!'.format(self.name))

  class Shadow(Character):
    def __init__(self):
      self.name = 'shadow'
      self.health = 1
      self.power = 1
      self.coins = 5
      self.agility = 90
      self.charSkill = None

  class Zombie(Character):
    def __init__(self):
      self.name = 'zombie'
      self.health = 6
      self.power = 2
      self.coins = 99
      self.agility = 99
      self.charSkill = None

    def alive(self):
      return True

  class Wizard(Character):
    def __init__(self):
      self.name = 'wizard'
      self.health = 8
      self.power = 2
      self.coins = random.randint(0, 40)
      self.agility = 60
    def charSkill(self, enemy):
      enemy.health -= 8
      print('The {} shoots a freaking lightning bolt at {}'.format(self.name, enemy.name))

  class Antihero(Character):
    def __init__(self):
      self.name = 'antihero'
      self.health = 10 # An antihero is just a regular guy, except that he is his own worst enemy
      self.power = 5 # An antihero hurts himself as much as he hurts others
      self.agility = 50 # An antihero is a survivor, constantly having to dodge out of danger
      self.coins = -5 # Antihero often is in need of money

    def charSkill(self, enemy):
      self.health += self.power
      print('The {} does -{} damage to {}. An antihero is his own worst enemy!'.format(self.name, self.power, self.name))

  class GuardianAngel(Character):
    def __init__(self):
      self.name = 'guardian angel'
      self.power = 10

    def saveTheDay(self, charToSave, enemy):
      if charToSave.health > 2 and random.randint(1, 100) < 5 and charToSave.alive():
        print('A {} steps in and deals {} damage to the {} before mysteriously disappearing'.format(self.name, self.power, enemy))
        enemy.health -= self.power

  class BattleField():
    def do_battle():
      randomIndex = random.randint(0, 5)
      enemy = enemies[randomIndex]
      while enemy.alive() and hero.alive():
        #BATTLEFIELD MENU FUNCTION:
          hero.print_status()
          enemy.print_status()
          print("An enemy approaches. Steel yourself, brave warrior...\n")

          print("A {} comes out of nowhere itching to fight\n".format(enemy))
          print("What do you want to do?")
          print("1. fight {}".format(enemy))
          print("2. do nothing")
          print("3. flee")
          print("4. Open Inventory")
          print("> ", end=' ')
          raw_input = input()
          if raw_input == "1":

            hero.attack(enemy)
          elif raw_input == "2":
            if enemy.name == 'antihero':
              hero.attack(enemy)
            pass
          elif raw_input == "3":
            print("You flee like a coward. Nope, not like. You ARE a coward.")
            MainMenu.displayMainMenu(hero)
          elif raw_input == "4":
            inventory.inventory_options(hero, enemy)
          else:
            print("Invalid input {}".format(raw_input))

          if enemy.alive():
            # enemy attacks hero
            enemy.attack(hero)
            if not hero.alive():
                print("You done got killed")
                main()
            guardianAngel.saveTheDay(hero, enemy)
          else:
              defeatedEnemies.append(enemy)
              hero.coins += enemy.coins



  class Inventory:
      def __init__(self):
          self.items = {
  #             armor : 1
  #             evade : 1
              'supertonic' : 1,
              'grenade' : 0 #- deals a certain amount of damage to all : 0
          }
          self.size = len(self.items)
      def print_inventory(self):
              print('You have {} slots in your inventory:\n\n {} \n\n'.format(self.size, str(self.items)))

      def inventory_options(self, hero, enemy):
            enemy = enemy
            while True:
              self.print_inventory()
              print('       INVENTORY OPTIONS:    ')

              if self.items['supertonic'] > 0:
                print('1. Use 1 of {} supertonics'.format(self.items['supertonic']))
              if self.items['grenade'] > 0:
                  print('2. Use 1 of {} grenades'.format(self.items['grenade']))
              if self.items['grenade'] == 0 and self.items['supertonic'] == 0:
                print('You have no items to use!\n \n')
                break
              print('3. Go back')
              raw_input = input()
              if raw_input == "1" and self.items['supertonic'] > 0:
                self.use_items(hero, self.items['supertonic'])
              elif raw_input == "2" and self.items['grenade'] > 0:
                self.use_items(hero, self.items['grenade'], enemy)
                break
              elif raw_input == "3":
                break

      def use_items(self, hero, item, enemy):
              if item == self.items['supertonic'] and self.items['supertonic'] > 0:
                  if hero.health + 10 > hero.maxHealth:
                      print('The hero has healed\n')
                      hero.health = hero.maxHealth
                  else:
                      hero.health += 10
                      print("The hero has healed")
                  self.items['supertonic'] -= 1

              elif item == self.items['grenade'] and self.items['grenade'] > 0:
                  print("BOOOOOOOOOMMMMM you threw a grenade \nDoes 8 damage to {} and {} ".format(hero, enemy))
                  hero.health -= 8
                  enemy.health -= 8
                  self.items['grenade'] -= 1
              else:
                  print('Cannot find item')

  class MainMenu():
      def displayMainMenu(self, hero):
        while True:
          print("=====================")
          print("WELCOME TO CAMELOT")
          print("=====================")
          print("			OPTIONS			")
          print('''
1. Start game
2. Do nothing
3. Go to store
4. Check inventory
5. Quit game
>
              ''', end=' ')
          raw_input = input(" What would you like to do? ")
          if raw_input == '1':
              BattleField.do_battle()
          elif raw_input == '2':
              pass
          elif raw_input == '3':
              Store.displayStore(hero)
          elif raw_input == '4':
              inventory.print_inventory()
          elif raw_input == '5':
              exit(0)
          else:
              print("Invalid input")

  class Store():
    def displayStore(self, hero):
      while True:
        print('''
You have {} coins.
1. Show inventory
2. Buy one SuperTonic
3. Buy one Armor
4. Buy one Evade
5. Buy one Protein
6. Buy one Grenade
7. Leave store
>
        ''', end=' '.format(hero.coins))
        raw_input = input()
        if hero.coins < 5:
          print("You're all out of cash! You can't shop here, peasant!")
          break
        else:
          if raw_input == '1':
              inventory.print_inventory()
          elif raw_input == '2':
              hero.coins -= 5
              inventory.items['supertonic'] += 1
              print('One supertonic has been added to your inventory')
          elif raw_input == '3':
              hero.coins -= 5
              hero.armor += 1
              print('Your armor has been increased by 1')
          elif raw_input == '4':
              hero.coins -= 5
              hero.agility += 1
              print('Your agility has increased by 1.')
          elif raw_input == '5':
              hero.coins -= 5
              hero.maxHealth += 1
              hero.health += 1
              print('Your current health and max health have increased by 1')
          elif raw_input == '6':
              hero.coins -= 5
              inventory.items['grenade'] += 1
              print('One grenade has been added to your inventory')
          elif raw_input == '7':
              print('')
              print('Pleasure doing business with you!')
              break
          else:
            print('Invalid input')

  MainMenu = MainMenu()
  Store = Store()
  inventory = Inventory()
  Battlefield = BattleField()

  #allies
  hero = Hero()
  guardianAngel = GuardianAngel()

	#enemies
  goblin = Goblin()
  wizard = Wizard()
  shadow = Shadow()
  medic = Medic()
  antihero = Antihero()
  zombie = Zombie()

  enemies = [goblin, wizard, shadow, medic, antihero, zombie]
  defeatedEnemies = []

  MainMenu.displayMainMenu(hero)
  if len(defeatedEnemies) == len(enemies):
     	print("YOU DID IT YOU WON THE GAME!!!!!!")
     	exit(0)

if __name__ == "__main__":
  main()