"""
Page # 90
1.1 Is Unique: Implement an algorithm to determine if a string has all unique
characters. What if you cannot use additional data structures?

"""


def unique(given_string):

    # ASCII characters 128 starting from 000 -> 127
    if len(given_string) > 128:
        return False

    char_set = [False for _ in range(128)]

    for char in given_string:
        val = ord(char)
        if char_set[val]:
            return False
        char_set[val] = True

    return True


def unique2(given_string):
    return len(given_string) == len(set(given_string))


if __name__ == "__main__":
    print(unique("dfahiuysdgfagfui"))
    print(unique("abcdefghijklmnopqrstuvwxyz"))

    # alternate approach
    print(unique2("dfahiuysdgfagfui"))
    print(unique2("abcdefghijklmnopqrstuvwxyz"))
