"""
One Away: There are three types of edits that can be performed on strings:
insert a character, remove a character, or replace a character.
Given two strings, write a function to check if they are one edit
(or zero edits) away.
EXAMPLE
pale, ple -> true
pales. pale -> true
pale. bale -> true
pale. bake -> false
"""
import unittest
from collections import Counter


def replace_one(string_1, string_2):
    return True


def insert_one(string_1, string_2):
    return True


def delete_one(string_1, string_2):
    return True


class Test(unittest.TestCase):

    def test_one_away(self):
        self.assertTrue(replace_one("pales", "palessss"))


if __name__ == "__main__":
    unittest.main()
