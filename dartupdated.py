import subprocess
import PySimpleGUI as sg

current_round = 1
score = 501

layout = [
    [sg.Text('Dart Score')],
    [sg.Text(f'Round {current_round}', key='-ROUND-')],
    [sg.Text('', key='-ERROR-')],
    [sg.Text('Dart 1'), sg.Input(key='-DART1-')],
    [sg.Text('Dart 2'), sg.Input(key='-DART2-')],
    [sg.Text('Dart 3'), sg.Input(key='-DART3-')],
    [sg.Button('Submit Score')],
    [sg.Text(f'Score: {score}', key='-SCORE-')],
    [sg.Button('Back to menu')],
]

window = sg.Window('Dart Score', layout)

while True:
    event, values = window.read()
    dart1 = int(values['-DART1-'])
    dart2 = int(values['-DART2-'])
    dart3 = int(values['-DART3-'])

    darts = [dart1, dart2, dart3]

    if event == sg.WINDOW_CLOSED:
        break

    if dart1 >= 61 or dart1 <= -1 or dart2 >= 61 or dart2 <= -1 or dart3 >= 61 or dart3 <= -1:
        window['-ERROR-'].update('max. 60 points per dart')

    if event == 'Submit Score':
        if all(0 <= dart <= 60 for dart in darts):
            round_score = sum(darts)  # Calculate the sum of darts
            score -= round_score
            current_round += 1
            window['-SCORE-'].update(score)
            window['-ROUND-'].update(current_round)
        else:
            window['-ERROR-'].update('Please enter valid numbers (0-60) for darts')

    if event == 'Back to menu':
        subprocess.Popen(['python3', './main.py'])
        break

window.close()
