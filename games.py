import os
import PySimpleGUI as sg

layout = [
    [sg.Text('==Games==')],
    [sg.Button('Hangman')],
    [sg.Button('Rock Paper Scissors')],
    [sg.Button('Snake')],
    [sg.Button('Exit')],
]

window = sg.Window('Tools', layout)

while True:
    event, values = window.read()

    if event == sg.WIN_CLOSED:
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