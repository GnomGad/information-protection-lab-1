import argparse
import random
import sys
import time
import os

from os import listdir
from gronsfeld import Gronsfeld

alphabet_default = "абвгдеёжзийклмнопрстуфхцчшщъыьэюяАБВГДЕЁЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯabcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ 0123456789\n[{(]}).,-_='\":#></№!?`*\\;"

key = '2836'
origin = 'Смаргл тут! Да прибудет вам счастье.'.lower()


def write_data(file_path, text, encoding='utf-8'):
    """Записать данные в файл."""
    with open(file_path, 'w') as fp:
        fp.write(text)


def get_file_data(file_path):
    """Прочитать целиком файл по пути."""
    data = ''
    with open(file_path, 'r', encoding='utf-8') as fp:
        data = fp.read()

    return data


def get_alphabet(file_name):
    """Вернет строку алфавита."""
    return_string = alphabet_default
    alphabets_files = listdir('./')

    if file_name in alphabets_files:
        return_string = get_file_data(file_name)
    elif len(alphabets_files) > 0:
        return_string = get_file_data(alphabets_files[0])

    return return_string


def main(action, text, key, output, log = False, alp = None, con = False):
    """Выполнить весь скрипт действий."""
    origin = text
    a = Gronsfeld(key,alp)
    write_data('key.key', key)
    #print('key',key)
    encrypted = ''
    decrypted = ''
    if(action == 'encrypt'):
        encrypted = a.encrypt(text)
        write_data('encrypted.txt' if output == '' else output, encrypted)
    elif action == 'decrypt':
        decrypted = a.decrypt(text)
        write_data('decrypted.txt' if output == '' else output, decrypted)
    else:
        encrypted = a.encrypt(text)
        decrypted = a.decrypt(encrypted)
    if log:
        print('key:       {0}'.format(key))
        print('aplhabet:  {0}'.format(a.alphabet))
        print('origin:    {0}'.format(origin))
        print('encrypted: {0}'.format(encrypted))
        print('decrypted: {0}'.format(decrypted))
    if con:
        print(encrypted if encrypted else decrypted)
    #print('Выполнение программы закончено')


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument('-a', '--action', dest='action', help='Тип действия Encrypt or decrypt', required=True)
    parser.add_argument('-k', '--key', dest='key', help='Ключ для шифрования или путь к файлу с ключем.Если ключ не указан создастся случайный с длиной файла', default='')
    parser.add_argument('-i', '--input', dest='input', help='Путь к файлу', required=True)
    parser.add_argument('-o', '--output', dest='output', help='Исходящий файл, если не указан будет создан автоматически', default='')
    parser.add_argument('-l', '--logs', dest='logs', action='store_true', default=False, help='Выводить ли лог')
    parser.add_argument('--alp', dest='alphabet', help='путь к алфавиту', default=None)
    parser.add_argument('-c', dest='console', help='вывод в консоль результата', default=False)
    args = parser.parse_args()

    start_time = time.time()

    # Тип действия
    action = args.action.lower()
    # Данные файла
    text = get_file_data(args.input)
    # Ключ для шифрования

    key = ''
    if args.key.isdigit():
        key = args.key
    elif os.path.exists(args.key):
        key = get_file_data(args.key)
    else:
        key =  ''.join([str(random.randint(0, 9)) for i in range(len(text))])
    alp = get_file_data(args.alphabet) if args.alphabet and os.path.exists(args.alphabet) else None
    main(action, text.lower(), key, args.output, args.logs, alp, args.console)

    #print('Время выполнения:',time.time() - start_time, 'секунд')
