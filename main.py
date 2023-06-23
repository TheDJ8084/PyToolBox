import os
import PySimpleGUI as sg

menu_def = [
  ['PyToolbox', ['Exit']],
  ['Tools', ['Calculator', 'Dart Score', 'Dice Roller', 'Timer', 'RNG', 'Converter']],
  ['Games', ['Hangman', 'Rock Paper Scissors', 'Snake']],
]

layout = [
  [sg.Menu(menu_def)],
  [sg.Image('./graphics/menu/PyToolBox-Logo.png', expand_x=True, expand_y=True)]
]

window = sg.Window('PyToolBox', layout)

while True:
  event, values = window.read()

  if event == 'Calculator':
    os.system('python calcmenu.py')
    break

  if event == 'Dart Score':
    os.system('python dart.py')
    break

  if event == 'Dice Roller':
    os.system('python dice.py')
    break

  if event == 'Timer':
    os.system('python timer.py')
    break

  if event == 'RNG':
    os.system('python rng.py')
    break

  if event == 'Converter':
        os.system('python converter.py')
        break

  if event == 'Hangman':
    os.system('python hangman.py')
    break

  if event == 'Rock Paper Scissors':
    os.system('python rockpaperscissors.py')
    break

  if event == 'Snake':
    os.system('python snake.py')
    break

  if event == 'Exit':
    break

window.close()