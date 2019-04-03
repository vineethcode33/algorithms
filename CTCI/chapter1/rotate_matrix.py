"""
Rotate Matrix: Given an image represented by an NxN matrix, where each pixel in the image is 4
bytes, write a method to rotate the image by 90 degrees. Can you do this in place?
"""

import numpy
from pprint import pprint
import unittest


def rotate_ninty(_input):
    output = numpy.zeros(shape=(len(_input), len(_input)))
    output.astype(int)

    if (len(_input) == 0 or (len(_input[0]) != len(_input))):
        return False

    for each in range(int(len(_input)/2)):
        for every in range(each, len(_input)-each):

            # top to right
            output[every][len(_input)-1 - each] = _input[each][every]

            # right to bottom
            output[len(_input)-1 - each][len(_input)-1 -
                                         every] = _input[every][len(_input)-1 - each]
            # bottom to left
            output[every][each] = _input[len(_input)-1 - each][every]

            # left to top
            output[each][every] = _input[len(_input)-1-every][each]

    return numpy.array(output.astype(int)).tolist()


class Test(unittest.TestCase):
    def test_rotate_ninty(self):
        mat1 = [[1, 2], [3, 4]]
        mat2 = [[3, 1], [4, 2]]
        self.assertEqual(rotate_ninty(mat1), mat2)

        mat5 = [[1, 2, 3, 4], [5, 6, 7, 8], [
            9, 10, 11, 12], [13, 14, 15, 16]]
        mat6 = [[13, 9, 5, 1], [14, 10, 6, 2], [15, 11, 7, 3], [16, 12, 8, 4]]
        self.assertEqual(rotate_ninty(mat5), mat6)


if __name__ == "__main__":
    unittest.main()
