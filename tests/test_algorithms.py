# -*- coding: utf-8 -*-
import unittest
from defs.alphabets import BRITISH_ALPHABET_LOWER, BRITISH_ALPHABET_LOWER_POLYBIUS_5_X_5
from algorithms.cesar import AveCesar
from algorithms.rail_fence import RailFence
from algorithms.polybius import PolYBius


class TestAlgorithms(unittest.TestCase):
    def test_cesar_encrypt(self):
        decrypted_phrase = (
            'it\'s the honky tonk women that gimme, gimme, gimme the honky tonk blues '
            '(honky tonk women, by the rolling stones)'
        )
        cesar = AveCesar(5, BRITISH_ALPHABET_LOWER)

        res_encrypt_phrase = cesar.encrypt(decrypted_phrase)

        expected_encrypted_phrase = (
            'ny\'x ymj mtspd ytsp btrjs ymfy lnrrj, lnrrj, lnrrj ymj mtspd ytsp gqzjx '
            '(mtspd ytsp btrjs, gd ymj wtqqnsl xytsjx)'
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
        cesar = AveCesar(5, BRITISH_ALPHABET_LOWER)

        encrypted_phrase = (
            'ny\'x ymj mtspd ytsp btrjs ymfy lnrrj, lnrrj, lnrrj ymj mtspd ytsp gqzjx '
            '(mtspd ytsp btrjs, gd ymj wtqqnsl xytsjx)'
        )

        res_decrypt_phrase = cesar.decrypt(encrypted_phrase)

        expected_decrypted_phrase = (
            'it\'s the honky tonk women that gimme, gimme, gimme the honky tonk blues '
            '(honky tonk women, by the rolling stones)'
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

    def test_cesar_drop_duplicates_from_alphabet(self):
        decrypted_phrase = (
            'it\'s the honky tonk women that gimme, gimme, gimme the honky tonk blues '
            '(honky tonk women, by the rolling stones)'
        )

        alphabet_with_duplicateds = list.copy(BRITISH_ALPHABET_LOWER)

        alphabet_with_duplicateds.extend(['a', 'a', 'b', 'c', 't'])

        cesar = AveCesar(5, BRITISH_ALPHABET_LOWER)

        res_encrypt_phrase = cesar.encrypt(decrypted_phrase)

        expected_encrypted_phrase = (
            'ny\'x ymj mtspd ytsp btrjs ymfy lnrrj, lnrrj, lnrrj ymj mtspd ytsp gqzjx '
            '(mtspd ytsp btrjs, gd ymj wtqqnsl xytsjx)'
        )

        self.assertEqual(res_encrypt_phrase, expected_encrypted_phrase)

    def test_polybius_encrypt(self):
        polibius = PolYBius(
            5, [
                'A',
                'B',
                'C',
                'D',
                'E'
            ],  # Encrypt Keys Rows
            5, ['A', 'B', 'C', 'D', 'E'],  # Decrypt Keys Columns
            BRITISH_ALPHABET_LOWER_POLYBIUS_5_X_5
        )
        original_phrase = 'hi julius'
        expected_encrypted_phrase = 'BCBDBDDECABDDEDC'

        self.assertEqual(polibius.encrypt(original_phrase), expected_encrypted_phrase)

    def test_polybius_decrypt(self):
        # self.assertEqual('', '')
        pass

    def test_rail_fence_encrypt(self):
        # self.assertEqual('', '')
        pass

    def test_rail_fence_decrypt(self):
        # self.assertEqual('', '')
        pass


if __name__ == '__main__':
    suite = unittest.TestLoader().loadTestsFromTestCase(TestAlgorithms)
    unittest.TextTestRunner(verbosity=2).run(suite)
