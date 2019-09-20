# -*- coding: utf-8 -*-
import unittest
from utils.matrix_operations import *
from defs.alphabets import BRITISH_ALPHABET_LOWER_POLYBIUS_5_X_5


class TestMatrixUtils(unittest.TestCase):
    def test_remove_duplicates_from_list_or_tuple_same_order(self):
        example_list = [4, 3, 1, 8, 4, 4, 7, 3, 1, 5]
        example_tuple = (4, 3, 1, 8, 4, 4, 7, 3, 1, 5)
        expected_list_result = [4, 3, 1, 8, 7, 5]

        result = remove_duplicates_from_list(example_list)

        self.assertEqual(result, expected_list_result)

        result2 = remove_duplicates_from_list(example_tuple)

        self.assertEqual(result2, expected_list_result)

    def test_create_matrix_from_iterable(self):
        result_matrix = create_matrix_from_iterable(5, 5, BRITISH_ALPHABET_LOWER_POLYBIUS_5_X_5)
        expected_matrix = [
            ('a', 'b', 'c', 'd', 'e'),
            ('f', 'g', 'h', ['i', 'j'], 'k'),
            ('l', 'm', 'n', 'o', 'p'),
            ('q', 'r', 's', 't', 'u'),
            ('v', 'w', 'x', 'y', 'z')
        ]
        self.assertEqual(result_matrix, expected_matrix)

    def test_create_dict_reverse_mapping_from_iterable(self):
        result_dict = create_dict_reverse_mapping_from_iterable(
            5, ['A', 'B', 'C', 'D', 'E'],
            5, ['A', 'B', 'C', 'D', 'E'],
            BRITISH_ALPHABET_LOWER_POLYBIUS_5_X_5
        )

        expected_result = {
            ('A', 'A'): 'a', ('A', 'B'): 'b', ('A', 'C'): 'c', ('A', 'D'): 'd', ('A', 'E'): 'e',
            ('B', 'A'): 'f', ('B', 'B'): 'g', ('B', 'C'): 'h', ('B', 'D'): ['i', 'j'], ('B', 'E'): 'k',
            ('C', 'A'): 'l', ('C', 'B'): 'm', ('C', 'C'): 'n', ('C', 'D'): 'o', ('C', 'E'): 'p',
            ('D', 'A'): 'q', ('D', 'B'): 'r', ('D', 'C'): 's', ('D', 'D'): 't', ('D', 'E'): 'u',
            ('E', 'A'): 'v', ('E', 'B'): 'w', ('E', 'C'): 'x', ('E', 'D'): 'y', ('E', 'E'): 'z'}

        self.assertEqual(result_dict, expected_result)

    def test_create_dict_mapping_from_iterable(self):
        result_dict = create_dict_mapping_from_iterable(
            5, ['A', 'B', 'C', 'D', 'E'],
            5, ['A', 'B', 'C', 'D', 'E'],
            BRITISH_ALPHABET_LOWER_POLYBIUS_5_X_5
        )

        expected_result_dict = {
            'a': ('A', 'A'), 'b': ('A', 'B'), 'c': ('A', 'C'), 'd': ('A', 'D'), 'e': ('A', 'E'),
            'f': ('B', 'A'), 'g': ('B', 'B'), 'h': ('B', 'C'), 'i': ('B', 'D'), 'j': ('B', 'D'),
            'k': ('B', 'E'), 'l': ('C', 'A'), 'm': ('C', 'B'), 'n': ('C', 'C'), 'o': ('C', 'D'),
            'p': ('C', 'E'), 'q': ('D', 'A'), 'r': ('D', 'B'), 's': ('D', 'C'), 't': ('D', 'D'),
            'u': ('D', 'E'), 'v': ('E', 'A'), 'w': ('E', 'B'), 'x': ('E', 'C'), 'y': ('E', 'D'),
            'z': ('E', 'E')}

        self.assertEqual(result_dict, expected_result_dict)

    def test_get_iterables_as_list_from_list(self):
        entry_list = [[], 22, 99.9, [1, 2], 'A', tuple([]), (1, 2), iter((5, 5)), 4, 'B']
        res_list = get_iterables_as_lists_from_list(entry_list)
        expected_res_list = [[], [1, 2], ['A'], [], [1, 2], [5, 5], ['B']]

        self.assertEqual(res_list, expected_res_list)

        res_list2 = get_iterables_as_lists_from_list([])
        expected_res_list2 = []

        self.assertEqual(res_list2, expected_res_list2)


if __name__ == '__main__':
    suite = unittest.TestLoader().loadTestsFromTestCase(TestMatrixUtils)
    unittest.TextTestRunner(verbosity=2).run(suite)
