import unittest
from gronsfeld import Gronsfeld


class TestGronsfeld(unittest.TestCase):
    def setUp(self):
        self.gronsfeld = Gronsfeld('935115151')

    def test_encrypt_decrypt(self):

        origin = "Разработать алгоритмы шифрования и дешифрования блока (потока) открытого текста заданной длины из алфавита Zn на заданном ключе с помощью метода, указанного в варианте(Если это позволяет алгоритм, длину блока взять кратной 8 бит)."
        encrypted = self.gronsfeld.encrypt(origin)
        decrypted = self.gronsfeld.decrypt(encrypted)
        self.assertEqual(origin, decrypted)

    def test_decrypt_encrypt(self):

        origin = "Щгмсбёпчбыя4бмзпхйыпА0щнххпкгтйА4й4енынхсугеосВ4вмуле0гтууппба0чхпсьчпзп8хйлтчб4иижеооук4ефлть0ни4бфчегйчб4 w2тб0мбибцрун0пмГшн2ц0рунуъЕБ4нёчпиба2шлбмбточёу0г4гессгтуё№Ёцмс2Вуп4руиксрАёч0емлсхйус:4ефлтф0ёмули2жиАчэ4лщгчопо0:0йлч',"
        decrypted = self.gronsfeld.decrypt(origin)
        encrypted = self.gronsfeld.encrypt(decrypted)
        self.assertEqual(origin, encrypted)


if __name__ == "__main__":
    unittest.main()
