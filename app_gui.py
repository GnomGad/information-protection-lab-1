import os
import PySimpleGUI as sg
from PySimpleGUI.PySimpleGUI import In

from gronsfeld import Gronsfeld
from app import get_file_data, write_data


# Слои
layout = [
    [
      sg.Text("Приложения по защите информации лабараторная работа 1")
    ],
    [
      sg.Text('Файл 1'), sg.InputText(key="-FOLDER_1-"), sg.FileBrowse(), sg.Button('Зашифровать', key='-ENCRYPT-')
    ],
    [
      sg.Text('Файл 2'), sg.InputText(key="-FOLDER_2-"), sg.FileBrowse(),sg.Button('Расшифровать', key='-DECRYPT-')
    ],
    [
      sg.Text('Ключ цифровой'), sg.InputText(key="-KEY-",default_text='0')
    ],
    [
      sg.Multiline(size=(88, 20), key='-OUT-')
      ],
    [sg.Submit(), sg.Cancel()]
]


# Окно
window = sg.Window('Lab 1', layout)


# Цикл
while True:
    event, values = window.read()
    key_in = '0'
    out = window.FindElement('-OUT-')

    if event in (None, 'Exit', 'Cancel', sg.WIN_CLOSED):
        break
    if values['-KEY-'] == None or len(values['-KEY-']) == 0 or  not values['-KEY-'].isdigit():
        continue
    else:
        key_in = values['-KEY-']
    
    if event == '-ENCRYPT-':
        file = values['-FOLDER_1-']
        key = key_in if key_in else '0'
        # Если есть путь то шифруем
        if os.path.exists(file):
            file_data = get_file_data(file)
            gr = Gronsfeld(key)
            out.Update(gr.encrypt(file_data))
        # шифровка из поля
        elif len(values['-OUT-']) > 0:
            file_data = values['-OUT-']
            gr = Gronsfeld(key)
            out.Update(gr.encrypt(file_data))
    if event == '-DECRYPT-':
        file = values['-FOLDER_2-']
        key = key_in if key_in else '0'
        # Если есть путь то шифруем
        if os.path.exists(file):
            file_data = get_file_data(file)
            gr = Gronsfeld(key)
            out.Update(gr.decrypt(file_data))
        # шифровка из поля
        elif len(values['-OUT-']) > 0:
            file_data = values['-OUT-']
            gr = Gronsfeld(key)
            out.Update(gr.decrypt(file_data))

            

window.close()