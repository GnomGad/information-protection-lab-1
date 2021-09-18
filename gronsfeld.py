class Gronsfeld:
    """Класс реализующий работу алгритма шифрования Гронсфельда"""

    def __init__(self, key, alphabet=''):
        self.key = key
        self.alphabet = alphabet if alphabet else "абвгдеёжзийклмнопрстуфхцчшщъыьэюяАБВГДЕЁЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯabcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ 0123456789[]/>$`*\{\}-.,:!?()#№'\"`_=\n"

    def encrypt(self, text):
        """Вернуть string

        Вернет зашифрованные данные
        """
        return ''.join([i for i in self.enumerate(text)])


    def decrypt(self, text):
        """Вернуть string

        Вернет дешифрованные данные
        """
        return ''.join([i for i in self.enumerate(text, -1)])

    def shift(self, symb, step):
        """Вернуть string

        Сделает необходимый сдвиг и вернет новый символ
        """
        new_index = self.alphabet.index(symb) + step
        if new_index >= len(self.alphabet):
            new_index -= len(self.alphabet)
        return self.alphabet[new_index]


    def enumerate(self, text, factor = 1):
        """Вернуть string

        Сделает необходимый сдвиг и вернет новый символ
        """
        key_counter = 0
        for i in text:
            try:
                yield self.shift(i, factor * int(self.key[key_counter]))
                key_counter += 1
                if key_counter == len(self.key):
                    key_counter = 0
            except:
                print("В алфавите нету символа, он не будет использоваться {0} -> {1}".format(i,ord(i)))
