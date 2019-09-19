from collections.abc import Iterable


def create_matrix_from_iterable(n_rows, n_columns, iterable_l):
    if not isinstance(iterable_l, Iterable):
        raise Exception('You passed a non iterable!')

    iterable_l = list(iterable_l)

    if n_rows * n_columns != len(iterable_l):
        raise Exception('That\s not possible ma friend %s X %s != %s' % (n_rows, n_columns, iterable_l))

    return list(zip(*[iter(iterable_l)]*n_rows))


def create_dict_mapping_from_iterable(n_rows, rows_code_list, n_columns, columns_code_list, iterable_l):
    if not isinstance(rows_code_list, Iterable) or not isinstance(columns_code_list, Iterable):
        raise Exception('You passed a non iterable as rows or columns code list!')

    rows_code_list = list(rows_code_list)
    columns_code_list = list(columns_code_list)

    if n_rows != len(rows_code_list):
        raise Exception('Size of rows codes list is distinct than number of rows')

    if n_columns != len(columns_code_list):
            raise Exception('Size of columns codes list is distinct than number of rows')

    list_of_tuples = create_matrix_from_iterable(n_rows, n_columns, iterable_l)

    res_dict = {}

    for i in range(0, n_rows):
        for j in range(0, n_columns):
            values_to_be_mapped = list_of_tuples[i][j]
            res_dict[rows_code_list[i], columns_code_list[j]] = values_to_be_mapped

    return res_dict


def remove_duplicates_from_list(some_list: list or tuple):
    return list(dict.fromkeys(some_list))
