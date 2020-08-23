# This is question 1.2 of CTCI
#  ------ Notes to myself ----------
# Check permutation: Given two strings, write a method to decide if
# one is a permutation of the other. A permutation is like an anagram, but
# does not have to be a word. Anagrams have to be words.
# Current solution: compare lengths of strings. They must be equal
# to be a permutation. If they are not return False. If they are
# sort the letters and compare them to each other and return the
# solution to that. (True or False).
# Time complexity:
# Space complexity:

def check_string(s, b):
    # base cases are the words the same?
    # are the lengths the same?

    # How would I solve this using either a hash map,
    # StringBuilder or ArrayList?
    if len(s) is not len(b):
        # print('Length of strings is not the same')
        return False
    else:
        return sorted(s) == sorted(b)


print(check_string("olhel", "hello"))
print(check_string("lol", "hello"))
print(check_string("olhei", "hello"))
