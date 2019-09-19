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


if __name__ == '__main__':
    suite = unittest.TestLoader().loadTestsFromTestCase(TestMatrixUtils)
    unittest.TextTestRunner(verbosity=2).run(suite)
