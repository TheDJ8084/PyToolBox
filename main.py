import os
import PySimpleGUI as sg

layout = [
  [sg.Text('==Main Menu==')],
  [sg.Button('Tools')],
  [sg.Button('Games')],
  [sg.Button('Exit')]
]

window = sg.Window('PyToolBox', layout)

while True:
  event, values = window.read()

  if event == sg.WIN_CLOSED:
    break

  if event == 'Tools':
    os.system('python tools.py')
    break

  if event == 'Games':
    os.system('python games.py')
    break

  if event == 'Exit':
    break

window.close()