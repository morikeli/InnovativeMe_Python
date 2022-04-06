"""
    2022 ALL RIGHTS RESERVED.
    Program developed, maintained, debugged by Mori Keli.
    Created 06/04/2020 1330hrs EAT
"""
# Program to detect KeyPress using the pynput module.
from pynput import keyboard

def on_press(key):
    """ Return value of key pressed by the user. """
    txt_file = open('data.txt', 'a')
    try:
        print(f'Alphanumeric key pressed {key.char}')
        try:

            print(f'Key pressed: {key}', file=txt_file)
        except FileNotFoundError:
            print('log file not found.')

    except AttributeError:
        print(f'Special key pressed {key}')
        print(f'Special key pressed{key}', file=txt_file)

def on_release(key):
    """ Alert the user once the pressed key is released. """

    print(f'Key released {key}')
    if key == keyboard.Key.esc:
        # Stop Listener
        return False
    try:
        txt_file = open('data.txt', 'a')
        print(f'Key released: {str(key)}', file=txt_file)
    except FileNotFoundError:
        print('log file not found.')


with keyboard.Listener(on_press=on_press, on_release=on_release) as listener:
    listener.join()

