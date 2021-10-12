import argparse
import random
import sys

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


def main(action, text, key, output):
    """Выполнить весь скрипт действий."""
    origin = text
    a = Gronsfeld(key)
    encrypted = ''
    decrypted = ''
    if(action == 'encrypt'):
        encrypted = a.encrypt(text)
        write_data('encrypted.txt', encrypted)
    elif action == 'decrypt':
        decrypted = a.decrypt(text)
        write_data('decrypted.txt', decrypted)
    else:
        encrypted = a.encrypt(text)
        decrypted = a.decrypt(encrypted)
    print('key:       {0}'.format(key))
    print('aplhabet:  {0}'.format(a.alphabet))
    print('origin:    {0}'.format(origin))
    print('encrypted: {0}'.format(encrypted))
    print('decrypted: {0}'.format(decrypted))


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument('-a', '--action', dest='action', help='Тип действия Encrypt or decrypt', required=True)
    parser.add_argument('-k', '--key', dest='key', help='Ключ для шифрования', default='')
    parser.add_argument('-i', '--input', dest='input', help='Входящий файл', required=True)
    parser.add_argument('-o', '--output', dest='output', help='Исходящий файл, если не указан будет создан автоматически out.txt', default='out.txt')
    args = parser.parse_args()

    print(args)

    # Тип действия
    action = args.action.lower()
    # Данные файла
    text = get_file_data(args.input)
    # Ключ для шифрования
    key = args.key if args.key != '' else ''.join([str(random.randint(0, 9)) for i in range(len(text))])
    print(key)
    
      #  alp_path = sys.argv[2]

   # alp = get_alphabet(alp_path)
    #
    main(action, text, key, args.output)

    #write_data('decrypted.txt', a.decrypt(text))
