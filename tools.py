import os
import PySimpleGUI as sg

layout = [
    [sg.Text('==Tools==')],
    [sg.Button('Calculator')],
    [sg.Button('Dart Score')],
    [sg.Button('Dice Roller')],
    [sg.Button('Timer')],
    [sg.Button('RNG')],
    [sg.Button('Converter')],
    [sg.Button('Exit')],
]

window = sg.Window('Tools', layout)

while True:
    event, values = window.read()

    if event == sg.WIN_CLOSED:
        break

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

    if event == 'Exit':
        break

window.close()