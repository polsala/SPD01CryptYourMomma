import unittest
from .context import algorithms
from .context import alphabets


class TestAlgorithms(unittest.TestCase):
    def test_cesar_encrypt(self):
        decrypted_phrase = (
            'It\'s the honky tonk women that gimme, gimme, gimme the honky tonk blues '
            '(honky tonk women, by the rolling Stones)'
        )
        cesar = algorithms.AveCesar(5)

        res_encrypt_phrase = cesar.encrypt(decrypted_phrase)

        expected_encrypted_phrase = (
            'Ny\'x ymj mtspd ytsp btrjs ymfy lnrrj, lnrrj, lnrrj ymj mtspd ytsp gqzjx '
            '(mtspd ytsp btrjs, gd ymj wtqqnsl Xytsjx)'
        )

        self.assertEqual(res_encrypt_phrase, expected_encrypted_phrase)

        cesar.secret_number = -7

        decrypted_phrase = (
            'empty spaces. what are we living for? abandoned places. '
            'i guess we know the score. (show must go on, by queen)'
        )

        res_encrypt_phrase = cesar.encrypt(decrypted_phrase)

        expected_encrypted_phrase = (
            'xfimr litvxl. patm tkx px ebobgz yhk? tutgwhgxw ietvxl. '
            'b znxll px dghp max lvhkx. (lahp fnlm zh hg, ur jnxxg)'
        )

        self.assertEqual(res_encrypt_phrase, expected_encrypted_phrase)

    def test_cesar_decrypt(self):
        cesar = algorithms.AveCesar(5)

        encrypted_phrase = (
            'Ny\'x ymj mtspd ytsp btrjs ymfy lnrrj, lnrrj, lnrrj ymj mtspd ytsp gqzjx '
            '(mtspd ytsp btrjs, gd ymj wtqqnsl Xytsjx)'
        )

        res_decrypt_phrase = cesar.decrypt(encrypted_phrase)

        expected_decrypted_phrase = (
            'It\'s the honky tonk women that gimme, gimme, gimme the honky tonk blues '
            '(honky tonk women, by the rolling Stones)'
        )

        self.assertEqual(res_decrypt_phrase, expected_decrypted_phrase)

        cesar.secret_number = -7

        encrypted_phrase = (
            'xfimr litvxl. patm tkx px ebobgz yhk? tutgwhgxw ietvxl. '
            'b znxll px dghp max lvhkx. (lahp fnlm zh hg, ur jnxxg)'
        )

        res_decrypt_phrase = cesar.decrypt(encrypted_phrase)

        expected_decrypted_phrase = (
            'empty spaces. what are we living for? abandoned places. '
            'i guess we know the score. (show must go on, by queen)'
        )

        self.assertEqual(res_decrypt_phrase, expected_decrypted_phrase)

    def test_poly_bios_encrypt(self):
        # self.assertEqual('', '')
        pass

    def test_poly_bios_decrypt(self):
        # self.assertEqual('', '')
        pass

    def test_rail_fence_encrypt(self):
        # self.assertEqual('', '')
        pass

    def test_rail_fence_decrypt(self):
        # self.assertEqual('', '')
        pass
