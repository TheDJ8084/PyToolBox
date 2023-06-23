import os
import time

punten = 501
beurtscore = 0
beurten = 0
x = 0
y = 4

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

#de variabelen#
def vari(punten,beurtscore,beurten,x,y):
  punten = 501
  beurtscore = 0
  beurten = 0
  x = 0
  y = 4
  ronde(punten,beurtscore,beurten,x,y)

#vraagt naar de score van de pijl, en checkt of die tussen de 0 en 60 zit#
def pijl(punten,beurtscore,beurten,x,y):
  print('')
  pijl = int(input('dart:'))
  
  #als de punten buiten de 0 t/m 60 zitten vraagt hij opnieuw naar de score#
  if pijl >= 61 or pijl <= -1:
    print('max 60 points')
    pijl(punten,beurtscore,beurten,x,y)

  
  #als de punten binnen de 0 t/m 60 zit voegt hij het door aan de beurtscore en gaat hij door naar pijl 2#
  elif pijl <= 60 and pijl >= 0:
    beurtscore += pijl
    y += 1
    ronde(punten,beurtscore,beurten,x,y)

#de main loop, wat er allemaal in een ronde gebeurt#
def ronde(punten,beurtscore,beurten,x,y):

  #checkt of er nog pijlen gegooid moeten worden, zo niet dan start hij een nieuwe ronde#
  if y <= 2:
    pijl(punten,beurtscore,beurten,x,y)

  else:
    y = 0
    
    #checken of de beurtscore de punten niet onder de 0 brengt, zo ja dan telt hij de scores niet mee op de punten variabel#
    x = (punten - beurtscore)
    if x <= -1:
      print('negative amount of points: ' + str(x))
    
    elif x >= 1:
      punten = x
    
    #als de punten 0 is stopt het programma na 15 seconden#
    elif x == 0:
      punten = x
      print('')
      print('---------------')
      print('you won!')
      print('')
      print('turns = ' + str(beurten))
      print('points = ' + str(punten))
      print('')
      print('---------------')

      choice = input('go again? (y/n)')

      if choice == 'y':
        vari(punten,beurtscore,beurten,x,y)
      elif choice == 'n':
        print('')
        print('---------------------------------')
        print('exiting...')
        time.sleep(3)
        subprocess.Popen(['python3', './main.py'])
      else:
        print('invalid option, exiting...')
        time.sleep(3)

    #zet de beurtscore weer op 0#
    beurtscore = 0  

    #voeg een extra beurt toe#
    beurten += 1
  
    print('')
  
    #de momentele score#
    print('---------------')
    print('turn = ' + str(beurten))
    print('points = ' + str(punten))

    #start een nieuwe ronde#
    ronde(punten,beurtscore,beurten,x,y)

clear_screen()
vari(punten,beurtscore,beurten,x,y)