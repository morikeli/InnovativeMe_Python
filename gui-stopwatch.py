"""
    2022 ALL RIGHTS RESERVED.
    Program created, developed and maintained by Mori Keli.
    Created 09/04/2022 1800hrs EAT
"""
# GUI Stopwatch with pysimpleGUI
import PySimpleGUI as sg
import time


def create_new_window():
    sg.theme('black')
    button_size = (6, 3)
    layout = [
        # [sg.Image('')]
        [sg.VPush()],
        [sg.Text('', font='Times 25', key='time')],
        [sg.Button('Start', expand_x=True, button_color=('white', 'green'), border_width=0, key='start'),
         sg.Button('Lap', expand_x=True, border_width=0, key='lap', visible=False)],
        [sg.Column([[]], key='laps')],
        [sg.VPush()]
    ]

    return sg.Window(
        'Stopwatch',
        layout,
        size=(300, 300),
        # no_titlebar=True,
        element_justification='center')


window = create_new_window()

start_timer = 0
active = False
num_lap = 1
while True:
    event, values = window.read(timeout=10)     # timeout in milliseconds.

    if event == sg.WIN_CLOSED:
        break

    if event == 'start':
        if active:
            active = False
            window['start'].update('reset')
            window['lap'].update(visible=False)

        else:
            if start_timer > 0:
                window.close()
                window = create_new_window()
                start_timer = 0
                num_lap = 1
            else:
                start_timer = time.time()
                active = True
                window['start'].update('stop')
                window['lap'].update(visible=True)

    if active:
        elapsed_time = round(time.time()-start_timer, 1)
        window['time'].update(elapsed_time)

    if event == 'lap':
        # elapsed_time = round(time.time()-start_timer, 1)
        window.extend_layout(window['laps'], [[sg.Text(num_lap), sg.VSeparator(), sg.Text(elapsed_time)]])
        num_lap += 1


window.close()
