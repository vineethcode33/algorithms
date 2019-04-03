"""Zero Matrix: Write an algorithm such that if an element in an MxN matrix is 0, its entire row and
column are set to O
"""

# TODO: Performance enhancements


import unittest
from pprint import pprint


def zero_matrix(_input):
    for _index, _value in enumerate(_input):
        for sub_index, sub_value in enumerate(_value):
            if sub_value == 0:
                column = sub_index
                row = _index
    _input[row] = [0]*len(_input[row])
    for each in range(len(_input)):
        _input[each][column] = 0
    pprint(_input)
    return ""


class Test(unittest.TestCase):

    def test_zero_matrix(self):
        self.assertEqual(zero_matrix([[1, 2, 3], [4, 0, 6]]), "")


if __name__ == "__main__":
    unittest.main()
