import os
import time
import random

# Function to clear the console screen
def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

#generates the number#
def generate():
  clear_screen()
  print('---------------------------------')
  min = int(input('min: '))
  max = int(input('max: '))
  print('---------------------------------')
  time.sleep(1)
  clear_screen()

  print('---------------------------------')
  print('min: '+ str(min))
  print('max: '+str(max))
  print('---------------------------------')

  rng = random.randint(min,max)
  print('output: ' + str(rng))
  exitrng()

#asks if you wanna exit#
def exitrng():
  print('---------------------------------')
  choice = input('generate another number? (y/n)')
  if choice == 'y':
    generate() 
  elif choice == 'n':
    print('---------------------------------')
    print('exiting...')
    time.sleep(3)
    os.system("python tools.py")
  else:
    print('invalid option, exiting...')
    time.sleep(3)
    os.system("python tools.py")
    time.sleep(3)


generate()
