# -*- coding: utf-8 -*-
from utils.matrix_operations import create_matrix_from_iterable, create_dict_mapping_from_iterable


class PolYBius(object):
    def __init__(self, rows, rows_code_list, columns, columns_code_list, alphabet):
        self.matrix_rows = rows
        self.matrix_columns = columns
        self.alphabet = alphabet
        self.matrix_decoder = create_matrix_from_iterable(rows, columns, alphabet)
        self.matrix_encoder_dict = create_dict_mapping_from_iterable(
            rows, rows_code_list, columns, columns_code_list,  alphabet
        )

    def encrypt(self, phrase):
        pass

    def decrypt(self, phrase):
        pass
