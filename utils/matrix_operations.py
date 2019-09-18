from collections.abc import Iterable


def create_matrix_from_iterable(n_rows, n_columns, iterable_l):
    if not isinstance(iterable_l, Iterable):
        raise Exception('You passed a non iterable!')

    # Todo Implement
    return [['A'*n_rows] * n_columns]
