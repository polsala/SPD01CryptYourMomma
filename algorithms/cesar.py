# -*- coding: utf-8 -*-
from utils.matrix_operations import remove_duplicates_from_list


class AveCesar(object):
    def __init__(self, n: int, alphabet: list or tuple):
        self.secret_number = n
        self.alphabet = remove_duplicates_from_list(alphabet)
        self.alpha_size = len(alphabet)

    def encrypt(self, phrase):
        return ''.join(
            [
                self.alphabet[(self.alphabet.index(ch) + self.secret_number) % self.alpha_size]
                if ch in self.alphabet
                else ch
                for ch in phrase
            ]
        )

    def decrypt(self, phrase):
        return ''.join(
            [
                self.alphabet[(self.alphabet.index(ch) - self.secret_number) % self.alpha_size]
                if ch in self.alphabet
                else ch
                for ch in phrase
            ]
        )
