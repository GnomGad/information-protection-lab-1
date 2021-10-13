from random import shuffle


class Gronsfeld:
    """Класс реализующий работу алгритма шифрования Гронсфельда."""
    
    def __init__(self, key, alphabet=''):
        """Принимает числовой ключ и алфавит."""
        alp_1 = "абвгдеёжзийклмнопрстуфхцчшщъыьэюяАБВГДЕЁЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯabcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ 0123456789\n[{(]}).,-_='\":#></№!?`*\\"
        alp_2 = "абвгдеёжзийклмнопрстуфхцчшщъыьэюяАБВГДЕЁЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯabcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789"
        alp_3 = "1Дёoй9DсTJRэOиЗizYnКУЁЕwuЭ7ПdMМjgyKUИФIxхCЩо4пШfзщю56жБeQеЙbSGОXаpвЦьрNнcBНmЧLЛдыЪъ2ЬZТГЯкqaчWВ8я0цvЖPHбшFРмфAh3rСVkЮтуlEsгАЫХлt"
        self.key = key
        self.alphabet = alphabet if alphabet else alp_3

    def encrypt(self, text):
        """Вернет зашифрованные данные."""
        return ''.join([i for i in self.enumerate(text)])

    def decrypt(self, text):
        """Вернет дешифрованные данные."""
        return ''.join([i for i in self.enumerate(text, -1)])

    def shift(self, symb, step):
        """Сделает необходимый сдвиг и вернет новый символ."""
        new_index = self.alphabet.index(symb) + step
        if new_index >= len(self.alphabet):
            new_index -= len(self.alphabet)
        return self.alphabet[new_index]

    def enumerate(self, text, factor=1):
        """Сделает необходимый сдвиг и вернет новый символ."""
        key_counter = 0
        for i in text:
            try:
                yield self.shift(i, factor * int(self.key[key_counter]))
                key_counter += 1
                if key_counter == len(self.key):
                    key_counter = 0
            except:
                #print( "В алфавите нету символа, он будет использоваться как есть {0} -> {1}".format(i, ord(i)))
                yield i
                    