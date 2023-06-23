import PySimpleGUI as sg
from time import time
import subprocess


def create_window():
    sg.theme('black')
    layout = [
        [sg.Push(), sg.Image('./graphics/stopwatch/cross.png', pad=0, key='-CLOSE-', enable_events=True)],
        [sg.VPush()],
        [sg.Text('', font='Arial 50', key='-TIME-')],
        [sg.Button('Start', button_color=('#FFFFFF', '#FF0000'), border_width=0, key='-STARTSTOP-'),
         sg.Button('Lap', button_color=('#FFFFFF', '#FF0000'), border_width=0, key='-LAP-', visible=False)],
        [sg.Button('Back to menu', button_color=('#FFFFFF', '#FF0000'), border_width=0)],
        [sg.Column([[]], key='-LAPS-')],
        [sg.VPush()],
    ]

    return sg.Window('Stopwatch', layout, size=(300, 300), no_titlebar=True, element_justification='center')


window = create_window()
start_time = 0
active = False
lap_amount = 1

while True:
    event, values = window.read(timeout=10)
    if event in (sg.WIN_CLOSED, '-CLOSE-'):
        break

    if event == '-STARTSTOP-':
        if active:
            # from active to stop
            active = False
            window['-STARTSTOP-'].update('Reset')
            window['-LAP-'].update(visible=False)
        else:
            # from stop to reset
            if start_time > 0:
                window.close()
                window = create_window()
                start_time = 0
                lap_amount = 1
            # from start to active
            else:
                start_time = time()
                active = True
                window['-STARTSTOP-'].update('Stop')
                window['-LAP-'].update(visible=True)

    if active:
        elapsed_time = round(time() - start_time, 1)
        window['-TIME-'].update(elapsed_time)

    if event == '-LAP-':
        window.extend_layout(window['-LAPS-'], [[sg.Text(lap_amount), sg.VSeparator(), sg.Text(elapsed_time)]])
        lap_amount += 1

    if event == 'Back to menu':
        subprocess.Popen(['python3', './main.py'])
        break

window.close()
