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
      sg.Text('Файл 1'), sg.InputText(key="-FOLDER_1-"), sg.FileBrowse(), sg.Button('Зашифровать', key='-ENCRYPT-'), sg.InputText(key="-FOLDER_1_OUT-")
    ],
    [
      sg.Text('Файл 2'), sg.InputText(key="-FOLDER_2-"), sg.FileBrowse(),sg.Button('Расшифровать', key='-DECRYPT-'), sg.InputText(key="-FOLDER_2_OUT-")
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
        decrypt_path = decrypt_path if len(decrypt_path) else 'decrypt.txtx'
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
            

window.close()