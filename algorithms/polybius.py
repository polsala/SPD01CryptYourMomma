# -*- coding: utf-8 -*-
from utils.matrix_operations import create_dict_reverse_mapping_from_iterable, \
                                    create_dict_mapping_from_iterable, \
                                    get_iterables_as_lists_from_list


class PolYBius(object):
    def __init__(self, rows, rows_code_list, columns, columns_code_list, alphabet, multiply_non_alpha=False):
        p_key_len = len(rows_code_list[0])

        if not all([len(k) == p_key_len for k in rows_code_list + columns_code_list]):
            raise Exception('Length of keys should be the same')

        self.key_len = p_key_len * 2
        self.matrix_rows = rows
        self.matrix_columns = columns
        # Todo Check repeated r:B E B| c:C G G
        self.alphabet = alphabet

        # If alphabet is [
        #     'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h',
        # ->  ['i', 'j'], 'k', 'l', 'm', 'n', 'o', 'p',
        #     'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z'
        # ]
        self.alphabet_distinct = [j for i in get_iterables_as_lists_from_list(alphabet) for j in i]

        if not all([not isinstance(c, list) for c in self.alphabet_distinct]):
            raise Exception('List of list of lists not allowed as a valid alphabet!')

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

        self.multiply_non_alpha = multiply_non_alpha

    def encrypt(self, phrase):

        return ''.join(
            [
                ''.join(self.matrix_encoder_dict[ch])
                if ch in self.alphabet_distinct
                else ('' if not self.multiply_non_alpha else ch * self.key_len)
                for ch in phrase
            ]
        )

    def decrypt(self, phrase):
        # TODO ALL PERMUTATIONS
        pass
