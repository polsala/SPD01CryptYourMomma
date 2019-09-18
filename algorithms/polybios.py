# -*- coding: utf-8 -*-
from utils.matrix_operations import create_matrix_from_iterable


class PolYBios(object):
    def __init__(self, rows, columns, alphabet):
        self.matrix_rows = rows
        self.matrix_columns = columns
        self.alphabet = alphabet
        self.matrix = create_matrix_from_iterable(rows, columns, alphabet)

    def encrypt(self, phrase):
        pass

    def decrypt(self, phrase):
        pass
