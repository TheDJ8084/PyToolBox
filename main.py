import subprocess
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

  if event == sg.WIN_CLOSED:
    break

  if event == 'Calculator':
    subprocess.Popen(['python3', './calculator.py'])
    break

  if event == 'Dart Score':
    subprocess.Popen(['python3', './dart.py'])
    break

  if event == 'Dice Roller':
    subprocess.Popen(['python3', './dice.py'])
    break

  if event == 'Timer':
    subprocess.Popen(['python3', './timer.py'])
    break

  if event == 'RNG':
    subprocess.Popen(['python3', './rng.py'])
    break

  if event == 'Converter':
    subprocess.Popen(['python3', './converter.py'])
    break

  if event == 'Hangman':
    subprocess.Popen(['python3', './hangman.py'])
    break

  if event == 'Rock Paper Scissors':
    subprocess.Popen(['python3', './rockpaperscissors.py'])
    break

  if event == 'Snake':
    subprocess.Popen(['python3', './snake.py'])
    break

  if event == 'Exit':
    break

window.close()