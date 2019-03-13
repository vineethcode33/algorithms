# Given two strings, write a method to decide if one is a permutation of the other.
from collections import Counter


def check_permutation(string1, string2):
    string1_counter = Counter(string1)
    string2_counter = Counter(string2)
    for each_charecter in string1_counter:
        if string1_counter[each_charecter] != string2_counter[each_charecter]:
            return False
    return True


if __name__ == "__main__":
    print(check_permutation("sample", "ample"))
    print(check_permutation("act", "tac"))
