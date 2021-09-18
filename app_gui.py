import os
import PySimpleGUI as sg
from PySimpleGUI.PySimpleGUI import In
from random import *

from gronsfeld import Gronsfeld
from app import get_file_data, write_data


# Слои
layout = [
    [
      sg.Text("Приложения по защите информации \"Лабораторная работа 1\"")
    ],
    [
        sg.Button('Зашифровать  ', key='-ENCRYPT-'), sg.Text('откуда'), sg.InputText(key="-FOLDER_1-"), sg.FileBrowse(button_text="открыть"),
        sg.Text('куда'),sg.InputText(key="-FOLDER_1_OUT-")
    ],
    [
        sg.Button('Расшифровать', key='-DECRYPT-'),sg.Text('откуда'), sg.InputText(key="-FOLDER_2-"), sg.FileBrowse(button_text="открыть"),
        sg.Text('куда'), sg.InputText(key="-FOLDER_2_OUT-")
    ],
    [
      sg.Text('Ключ цифровой'), sg.InputText(key="-KEY-",default_text='0'), sg.Button('Сгенерировать',key='-KEY_GENERATE-'),
      sg.Button('Очистить поле с текстом',key='-CLEAR-')
    ],
    [
      sg.Multiline(size=(140, 20), key='-OUT-')
    ],
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
    
    if event == '-KEY_GENERATE-':
        field = window.FindElement('-KEY-')
        len_of_data = len(values['-OUT-'])
        if len_of_data == 0:
            if values['-FOLDER_1-'] != '':
                len_of_data = len(get_file_data(values['-FOLDER_1-']))
            elif values['-FOLDER_2-'] != '':
                len_of_data = len(get_file_data(values['-FOLDER_2-']))
            else :
                continue
        
        field.Update(''.join([str(randint(0,9)) for i in range(len_of_data)]))

    if event == '-ENCRYPT-':
        file = values['-FOLDER_1-']
        key = key_in if key_in else '0'
        encrypt_path = values['-FOLDER_1_OUT-']
        encrypt_path = encrypt_path if len(encrypt_path) > 0 else 'encrypt.txt'
        gr = Gronsfeld(key)

        # Если есть путь то шифруем
        if os.path.exists(file):
            file_data = get_file_data(file)
            encrypted = gr.encrypt(file_data)

        # шифровка из поля
        elif len(values['-OUT-']) > 0:
            file_data = values['-OUT-']
            encrypted = gr.encrypt(file_data)

        else:
            break
        write_data(encrypt_path, encrypted)
        out.Update(encrypted)

    if event == '-DECRYPT-':
        file = values['-FOLDER_2-']
        key = key_in if key_in else '0'
        decrypt_path = values['-FOLDER_2_OUT-']
        decrypt_path = decrypt_path if len(decrypt_path) else 'decrypt.txt'
        gr = Gronsfeld(key)

        # Если есть путь то шифруем
        if os.path.exists(file):
            file_data = get_file_data(file)
            decrypt = gr.decrypt(file_data)

        # шифровка из поля
        elif len(values['-OUT-']) > 0:
            file_data = values['-OUT-']
            decrypt = gr.decrypt(file_data)
        else:
            break

        write_data(decrypt_path, decrypt)
        out.Update(decrypt)

    if event == '-CLEAR-':
        out.Update('')

window.close()