"""
String Compression: Implement a method to perform basic string compression using the counts
of repeated characters. For example, the string aabcccccaaa would become a2b1c5a3. If the
"compressed" string would not become smaller than the original string, your method should return
the original string. You can assume the string has only uppercase and lowercase letters (a - z).
"""

from collections import Counter


def string_compression(input_string):

    if len(input_string) == len("".join(set(input_string))):
        return input_string

    comp_count = 1
    comp_string = ""
    for _index, _value in enumerate(input_string):
        if (_index == 0):
            comp_count = 1
        elif (_index == (len(input_string)-1)):
            comp_string += input_string[_index] + str(comp_count)
            comp_count = 1
        elif (_value == input_string[_index-1]):
            comp_count += 1

        elif (_value != input_string[_index-1]):
            comp_string += input_string[_index-1] + str(comp_count)
            comp_count = 1

    return comp_string


if __name__ == "__main__":
    print(string_compression("abcdef"))
