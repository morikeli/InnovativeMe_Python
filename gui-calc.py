"""
    2022 ALL RIGHTS RESERVED.
    Program created, debugged & maintained by Mori Keli.
    Created: 09/04/2022 1430hrs EAT
"""
# Creating a simple Calculator using PySimpleGUI module.
import PySimpleGUI as sg

sg.theme('BlueMono')    # set theme of our calculator. A list of supported themes ill be printed on the console if you type incorrect theme
sg.set_options(font='Verdana 13', button_element_size=(5, 3))   # font & font_size.
button_size = (6, 3)    # dimensions: (width, height); units: characters, e.g. button - 6 characters wide, 3 characters high.
theme_menu = ['menu', ['LightGrey1', 'dark', 'DarkGray8']]

layout = [
    [sg.Text('', font='Times 16', justification='right', expand_x=True, pad=(10, 15), right_click_menu=theme_menu, key='Text')],    # 1st row
    [sg. Button('Clear', expand_x=True), sg.Button('Enter', expand_x=True)],  # 2nd row
    [sg.Button('7', size=button_size), sg.Button('8', size=button_size), sg.Button('9', size=button_size), sg.Button('*', size=button_size)],
    [sg.Button('4', size=button_size), sg.Button('5', size=button_size), sg.Button('6', size=button_size), sg.Button('/', size=button_size)],
    [sg.Button('1', size=button_size), sg.Button('2', size=button_size), sg.Button('3', size=button_size), sg.Button('-', size=button_size)],
    [sg.Button('0', expand_x=True), sg.Button('.', size=button_size), sg.Button('+', size=button_size)],   # last row
]
window = sg.Window('Calculator', layout)
current_num = []
operation = []

while True:
    event, values = window.read()

    if event == sg.WIN_CLOSED:
        break

    # if event in theme_menu[1]:
    #     window.layout(event)

    # Print a clicked button.
    if event in ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', '.']:
        current_num.append(event)
        num_string = ''.join(current_num)
        window['Text'].update(num_string)

    elif event in ['+', '-', '/', '*']:
        operation.append(''.join(current_num))
        current_num = []
        operation.append(event)
        window['Text'].update('')

    elif event == 'Enter':
        operation.append(''.join(current_num))
        result = eval(''.join(operation))
        window['Text'].update(result)
        operation = []
    else:
        current_num = []
        operation = []
        window['Text'].update('')

window.close()
