from collections.abc import Iterable


def create_matrix_from_iterable(n_rows, n_columns, iterable_l):
    if not isinstance(iterable_l, Iterable):
        raise Exception('You passed a non iterable!')

    iterable_l = list(iterable_l)

    if n_rows * n_columns != len(iterable_l):
        raise Exception('That\s not possible ma friend %s X %s != %s' % (n_rows, n_columns, iterable_l))

    # Todo Implement
    return [['A'*n_rows] * n_columns]
