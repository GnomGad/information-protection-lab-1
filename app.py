import sys
from os import listdir, path


alphabet_default = 'абвгдеёжзийклмнопрстуфхцчшщъыьэюя -.,:!'

key = '2836'
origin = 'Смаргл тут! Да прибудет вам счастье.'.lower()


def shift(alp, symb, step):
    """Вернуть string

    Сделает необходимый сдвиг и вернет новый символ
    """
    new_index = alp.index(symb) + step
    if new_index >= len(alp):
        new_index -= len(alp)
    return alp[new_index]


def enumerate(alp, text, key, factor=1):
    """Вернуть string

    Сделает необходимый сдвиг и вернет новый символ
    """
    key_counter = 0
    for i in text:
        yield shift(alp, i, factor * int(key[key_counter]))
        key_counter += 1
        if key_counter == len(key):
            key_counter = 0


def encrypt(alp, text, key):
    """Вернуть string

    Вернет зашифрованные данные
    """
    return ''.join([i for i in enumerate(alp, text, key)])


def decrypt(alp, text, key):
    """Вернуть string

    Вернет дешифрованные данные
    """
    return ''.join([i for i in enumerate(alp, text, key, -1)])


def write_data(file_path, text):
    """
    Записать данные в файл
    """
    with open(file_path, 'w') as fp:
        fp.write(text)


def get_file_data(file_path):
    """Return string

    Прочитать целиком файл по пути
    """
    data = ''
    with open(file_path) as fp:
        data = fp.read()
    return data


def get_alphabet(file_name):
    """Вернуть string

    Вернет строку алфавита,
    """

    return_string = alphabet_default
    alphabets_files = listdir('./')

    if file_name in alphabets_files:
        return_string = get_file_data(file_name)
    elif len(alphabets_files) > 0:
        return_string = get_file_data(alphabets_files[0])

    return return_string


def main(alp, action, text, key):
    current_alphabet = alp
    origin = text
    encrypted = ''
    decrypted = ''
    if(action == 'encrypt'):
        encrypted = encrypt(current_alphabet, text, key)
        write_data('encrypted.txt',encrypted)
    elif action == 'decrypt':
        decrypted = decrypt(current_alphabet, text, key)
        write_data('decrypted.txt',decrypted)
    else:
        encrypted = encrypt(current_alphabet, text, key)
        decrypted = decrypt(current_alphabet, encrypted, key)
    print('key:       {0}'.format(key))
    print('aplhabet:  {0}'.format(current_alphabet))
    print('origin:    {0}'.format(origin))
    print('encrypted: {0}'.format(encrypted))
    print('decrypted: {0}'.format(decrypted))


if __name__ == "__main__":
    action = sys.argv[1]
    alp_path = sys.argv[2]
    file_name = sys.argv[3]
    key = sys.argv[4]

    alp = get_alphabet(alp_path)
    text = get_file_data(file_name)
    main(alp, action, text, key)
