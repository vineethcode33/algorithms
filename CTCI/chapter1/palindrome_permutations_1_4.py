"""
Palindrome Permutation: Given a string, write a function to check if it is a
permutation of a palin- drome. A palindrome is a word or phrase that is the same
forwards and backwards. A permutation is a rearrangement of letters.
The palindrome does not need to be limited to just dictionary words.
EXAMPLE
Input: Tact Coa
Output: True (permutations: "taco cat". "atco cta". etc.)
"""
import unittest
from collections import Counter


def check_permutation_palindrome(input_string):
    input_string = input_string.replace(" ", "").lower()
    input_counter = Counter(input_string)
    if sum(input_counter[each_char] % 2 for each_char in input_counter) > 1:
        return False
    return True


class Test(unittest.TestCase):

    def test_check_permutation_palindrome(self):
        #deified, civic, radar, level, rotor, kayak, reviver, racecar
        self.assertTrue(check_permutation_palindrome("Tact Coa"))
        self.assertTrue(check_permutation_palindrome("kayak"))
        self.assertTrue(check_permutation_palindrome("level"))
        self.assertTrue(check_permutation_palindrome("reviver"))
        self.assertTrue(check_permutation_palindrome("racecar"))

    def test_check_permutation_palindrome2(self):
        self.assertFalse(check_permutation_palindrome("kayaka"))
        self.assertFalse(check_permutation_palindrome("levele"))
        self.assertFalse(check_permutation_palindrome("reviverr"))
        self.assertFalse(check_permutation_palindrome("racecarr"))


if __name__ == "__main__":
    unittest.main()
    # check_permutation_palindrome("Tact Coa")
