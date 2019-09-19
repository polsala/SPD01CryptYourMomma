# -*- coding: utf-8 -*-


class AveCesar(object):
    def __init__(self, n: int, alphabet: list or tuple):
        self.secret_number = n
        self.alphabet = alphabet
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
        pass
