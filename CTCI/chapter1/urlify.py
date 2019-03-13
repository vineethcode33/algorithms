"""
Chapter 1.3
URLify: Write a method to replace all spaces in a string with '%20'.
You may assume that the string has sufficient space at the end to hold the
additional characters, and that you are given the "true" length of the string.
EXAMPLE
Input: "Mr John Smith      ", 13
Output: "Mr%20John%20Smith"
"""
import unittest


def urlify(string_to_urlify, len_of_str):
    string_urlified = string_to_urlify[:len(
        string_to_urlify) - (len(string_to_urlify)-len_of_str)]
    string_urlified = "".join(string_urlified).replace(" ", "%20")
    return string_urlified


class Test(unittest.TestCase):

    def test_urlify(self):
        output = urlify("Mr John Smith      ", 13)
        self.assertEqual(output, "Mr%20John%20Smith")

    def test_urlify2(self):
        output = urlify('much ado about nothing      ', 22)
        self.assertEqual(output, 'much%20ado%20about%20nothing')


if __name__ == "__main__":
    unittest.main()
