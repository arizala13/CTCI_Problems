# This is question 1.1 of CTCI


def check_unique(string_input) -> bool:
    chars_in_string = {}

    for char in string_input:
        if char in chars_in_string:
            chars_in_string[char] = 2
        else:
            chars_in_string[char] = 1

    for value in chars_in_string.values():
        if value > 1:
            return False
    return True


print(check_unique("Hello"))
print(check_unique("word"))
