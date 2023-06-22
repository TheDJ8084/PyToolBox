import os
import time
import random as r

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

def rolldice():
  total = 0
  print('---------------------------------')
  hdice = 0
  tdice = 0
  hdice = int(input('dice amount =  '))
  tdice = int(input('dice type =  '))
  print('-')
  print('output: ')
  while hdice >= 1:
    hdice -= 1
    result = (r.randint(1,tdice))
    print(str(result))
    total += result
  print('total = ' + str(total))
  
  print('-')
  choice = input('roll again? (y/n)')

  if choice == 'y':
    rolldice() 
  elif choice == 'n':
    print('---------------------------------')
    print('exiting...')
    time.sleep(3)
    os.system("python tools.py")
  else:
    print('invalid option, exiting...')
    time.sleep(3)
    
clear_screen()
rolldice()