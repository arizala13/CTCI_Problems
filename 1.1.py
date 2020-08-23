# This is question 1.1 of CTCI
#  ------ Notes to myself ----------
# Currently this solves the problem, but how can I improve it?
# It needs to work where lets say it cannot have more than
# N letters. Where N is 2 and the word cannot have more than N
# unique letters in the word.
# Time complexity:
# Space complexity:

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
