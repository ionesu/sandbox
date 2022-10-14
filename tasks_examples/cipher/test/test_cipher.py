import unittest

from ..app.code_value_cipher import Encrypt, Decrypt


key = "BCDEFGHIJKLMNOPQRSTUVWXYZA"


class EncryptionTests(unittest.TestCase):

    def test_encrypt_1(self):
        encrypted = Encrypt("AaA", key)
        self.assertEqual(encrypted, "BbB")


    def test_encrypt_2(self):
        encrypted = Encrypt("ZzZ", key)
        self.assertEqual(encrypted, "AaA")


    def test_encrypt_3(self):
        encrypted = Encrypt("CiPhEr", key)
        self.assertEqual(encrypted, "DjQiFs")


    def test_encrypt_4(self):
        encrypted = Encrypt("AbC DEfG", key)
        self.assertEqual(encrypted, "BcD EFgH")


class DecryptionTests(unittest.TestCase):

    def test_encrypt_1(self):
        decrypted = Decrypt("BbB", key)
        self.assertEqual(decrypted, "AaA")


    def test_decrypt_2(self):
        decrypted = Decrypt("AaA", key)
        self.assertEqual(decrypted, "ZzZ")


    def test_decrypt_3(self):
        decrypted = Decrypt("DjQiFs", key)
        self.assertEqual(decrypted, "CiPhEr")


    def test_decryptt_4(self):
        decrypted = Decrypt("BcD EFgH", key)
        self.assertEqual(decrypted, "AbC DEfG")
