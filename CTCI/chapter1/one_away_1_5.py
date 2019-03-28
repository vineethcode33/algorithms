"""
One Away: There are three types of edits that can be performed on strings:
insert a character, remove a character, or replace a character.
Given two strings, write a function to check if they are one edit
(or zero edits) away.

EXAMPLE
-------
pale , ple  -> true
pales, pale -> true
pale , bale -> true
pale , bake -> false
"""

import unittest
from collections import Counter


def replace_one(string_1, string_2):
    one_replaced = False

    for _ in range(len(string_1)):
        if(string_1[_] != string_2[_]):
            if(one_replaced):
                return False
            one_replaced = True

    return True


def insert_delete_one(string_1, string_2):

    if len(string_1) > len(string_2):
        first_string = string_1
        second_string = string_2
    else:
        first_string = string_2
        second_string = string_1

    string_removed = False
    for _index, _value in enumerate(first_string):
        if (_index != len(second_string)):
            if first_string[_index] != second_string[_index]:
                if string_removed:
                    return False
                else:
                    string_removed = True
        else:
            if string_removed:
                return False
            else:
                return True


def one_away(string_1, string_2):
    if (len(string_1) == len(string_2)):
        return replace_one(string_1, string_2)
    elif(abs(len(string_1) - len(string_2)) == 1):
        return insert_delete_one(string_1, string_2)
    return False


class Test(unittest.TestCase):

    def test_one_away(self):
        self.assertTrue(one_away("pales", "bales"))
        self.assertTrue(one_away("pal", "bal"))
        self.assertTrue(one_away("pales", "pale"))
        self.assertFalse(one_away("pales", "bale"))


if __name__ == "__main__":
    unittest.main()
