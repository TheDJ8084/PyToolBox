import random
import subprocess
import PySimpleGUI as sg

layout = [
    [sg.Text('Random Number Generator')],
    [sg.Text('Min'), sg.Input(key='-MIN-')],
    [sg.Text('Max'), sg.Input(key='-MAX-')],
    [sg.Button('Generate Random Number')],
    [sg.Text('Output:'), sg.Text(size=(15, 1), key='-OUTPUT-')],
    [sg.Button('Back to menu')]
]

window = sg.Window('Random Number Generator', layout)

while True:
    event, values = window.read()

    if event == sg.WINDOW_CLOSED or event == 'Back to menu':
        subprocess.Popen(['python3', './main.py'])
        break

    if event == 'Generate Random Number':
        input_min = values['-MIN-']
        input_max = values['-MAX-']

        if input_min.isnumeric() and input_max.isnumeric():
            input_min = int(input_min)
            input_max = int(input_max)

            if input_min <= input_max:
                output = random.randint(input_min, input_max)
                window['-OUTPUT-'].update(output)
            else:
                window['-OUTPUT-'].update('Max must be greater than Min')
        else:
            window['-OUTPUT-'].update('Please enter valid numbers')

window.close()
