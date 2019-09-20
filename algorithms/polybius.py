# -*- coding: utf-8 -*-
from utils.matrix_operations import create_dict_reverse_mapping_from_iterable, \
                                    create_dict_mapping_from_iterable, \
                                    get_iterables_as_lists_from_list


class PolYBius(object):
    def __init__(self, rows_code_list, columns_code_list, alphabet, multiply_non_alpha=False):
        # Todo Problem if pass '[' or ']' as keys for parsing decrypt response after call decrypt method
        p_key_len = len(rows_code_list[0])

        if not all([len(k) == p_key_len for k in rows_code_list + columns_code_list]):
            raise Exception('Length of keys should be the same')

        self.key_len = p_key_len * 2
        self.matrix_rows = len(rows_code_list)
        self.matrix_columns = len(columns_code_list)

        if len(rows_code_list) != len(set(rows_code_list)):
            raise Exception('Duplicated keys on rows keys list')

        self.rows_code_list = rows_code_list
        self.columns_code_list = columns_code_list

        if len(columns_code_list) != len(set(columns_code_list)):
            raise Exception('Duplicated keys on columns keys list')

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
            rows_code_list, columns_code_list, alphabet
        )
        self.matrix_decoder_dict = create_dict_reverse_mapping_from_iterable(
            rows_code_list, columns_code_list,  alphabet
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
        list_tuples_group_key_len = list(zip(*[iter(phrase)] * self.key_len))

        return ''.join(
            [
                (
                    self.matrix_decoder_dict[ch]
                    if not isinstance(self.matrix_decoder_dict[ch], list)
                    else '{}'.format(self.matrix_decoder_dict[ch])
                )
                if ch in self.matrix_decoder_dict.keys()
                else ('' if not self.multiply_non_alpha else ch[0])
                for ch in list_tuples_group_key_len
            ]
        )
