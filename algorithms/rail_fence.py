# -*- coding: utf-8 -*-


class RailFence(object):
    def __init__(self, rails, alphabet):
        self.n_rails = rails
        self.alphabet = alphabet

    def _generate_rail_fence_matrix(self, phrase):
        phrase = list(phrase)

        list_flatted = [[] for _ in range(self.n_rails)]

        list_i = 0
        direction = 1

        for ch in phrase:
            list_flatted[list_i].append(ch)

            if (list_i == self.n_rails - 1 and direction > 0) or (list_i == 0 and direction < 0):
                direction *= -1

            list_i += direction

        return [j for i in list_flatted for j in i]

    def encrypt(self, phrase):
        return ''.join(self._generate_rail_fence_matrix(phrase))

    def decrypt(self, phrase):
        n_columns = len(phrase)
        res = [''] * n_columns

        # _generate_rail_fence_matrix of range phrase returns position in array of phrase_size X rails
        for ch, i in zip(phrase, self._generate_rail_fence_matrix(range(len(phrase)))):
            res[i] = ch

        return ''.join(res)
