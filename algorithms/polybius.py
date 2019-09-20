# -*- coding: utf-8 -*-
from utils.matrix_operations import create_dict_reverse_mapping_from_iterable, \
                                    create_dict_mapping_from_iterable, \
                                    get_iterables_as_lists_from_list


class PolYBius(object):
    def __init__(self, rows, rows_code_list, columns, columns_code_list, alphabet):
        self.matrix_rows = rows
        self.matrix_columns = columns
        # Todo alphabet checker no list of lists of lists
        # TODO Check Same lenght keys rows and columns all
        # Todo Check repeated r:B E B| c:C G G
        self.alphabet = alphabet

        # If alphabet is [
        #     'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h',
        # ->  ['i', 'j'], 'k', 'l', 'm', 'n', 'o', 'p',
        #     'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z'
        # ]
        self.alphabet_distinct = [j for i in get_iterables_as_lists_from_list(alphabet) for j in i]
        # alphabet_distinct is [
        #     'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h',
        # ->  'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p',
        #     'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z'
        # ]

        self.matrix_encoder_dict = create_dict_mapping_from_iterable(
            rows, rows_code_list, columns, columns_code_list, alphabet
        )
        self.matrix_decoder_dict = create_dict_reverse_mapping_from_iterable(
            rows, rows_code_list, columns, columns_code_list,  alphabet
        )

    def encrypt(self, phrase):

        return ''.join(
            [
                ''.join(self.matrix_encoder_dict[ch])
                if ch in self.alphabet_distinct
                else ''
                for ch in phrase
            ]
        )

    def decrypt(self, phrase):
        # TODO ALL PERMUTATIONS
        pass
