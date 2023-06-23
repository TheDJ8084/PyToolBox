import os
import time

# Function to clear the console screen
def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

def asktime():
  print('---------------------------------')
  Minutes = int(input("Minutes: "))
  Seconds = int(input("Seconds: "))
  if int(Seconds) >= 61:
    print('error, max 60 sec')
    time.sleep(2)
    clear_screen()
    asktime()
  if int(Seconds) <= 60:
    print('---------------------------------')
    print(str(Minutes)+':'+str(Seconds))
    startinput = input("Start timer? (y/n) ")
    if startinput == 'n':
      asktime()
    elif startinput == 'y':
      updatetimer(Minutes,Seconds)

def updatetimer(Minutes,Seconds):
  print('---------------------------------')
  time.sleep(1)
  clear_screen()
  print('---------------------------------')
  print(str(Minutes)+':'+str(Seconds))
  Seconds -= 1
  if Seconds == 0 and Minutes == 0:
    clear_screen()
    print('---------------------------------')
    print(str(Minutes)+':'+str(Seconds))
    print('---------------------------------')

    print('Timer stopped')
    print('---------------------------------')
    choice = input('set another timer? (y/n)')
    if choice == 'y':
      asktime() 
    elif choice == 'n':
      print('---------------------------------')
      print('exiting...')
      time.sleep(3)
      subprocess.Popen(['python3', './main.py'])
    else:
      print('invalid option, exiting...')
      time.sleep(3)
      subprocess.Popen(['python3', './main.py'])
      time.sleep(3)
  
  if Seconds == 0:
    Seconds = 60
    Minutes -= 1
  updatetimer(Minutes,Seconds)
  



asktime()