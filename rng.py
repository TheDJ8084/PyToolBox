import random
import PySimpleGUI as sg


layout = [
  [sg.Text('Random Number Generator')],
  [sg.Text('Min')],
  [sg.Input(key = '-MIN-')],
  [sg.Text('Max')],
  [sg.Input(key = '-MAX-')],
  [sg.Button('Generate Random Number')],
  [sg.Text('Output')]
  [sg.Button('Back to menu')]
]

window = sg.Window('Random Number Generator', layout)

while True:
  event, values = window.read()

  if event == 'Generate Random Number':
    input_min = int(values['-MIN-'])
    input_max = int(values['-MAX-'])
    if input_min.isnumeric() and input_max.isnumeric():
      output = random.randint(input_min,input_max)
      window['Output'].update(output)

    else:
      window['Output'].update('Please enter two numbers')

  if event == 'Back to menu':
    break

window.close()