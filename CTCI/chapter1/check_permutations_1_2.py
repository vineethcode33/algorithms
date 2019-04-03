# Given two strings, write a method to decide if one is a permutation of the other.
from collections import Counter
import unittest


def check_permutation(string1, string2):

    if len(string1) != len(string2):
        return False
    string1_counter = Counter(string1)
    string2_counter = Counter(string2)
    for each_charecter in string1_counter:
        if string1_counter[each_charecter] != string2_counter[each_charecter]:
            return False
    return True


class Test(unittest.TestCase):

    def test_check_permutaiton(self):
        self.assertTrue(check_permutation("jack", "kjca"))
        self.assertTrue(check_permutation("alex", "lexa"))
        self.assertTrue(check_permutation("324561", "356124"))
        self.assertFalse(check_permutation("test string", "sample test"))
        self.assertFalse(check_permutation("ac", "tac"))


unittest.main()
