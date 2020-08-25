# This is question 2.1 of CTCI
#  ------ Notes to myself ----------
# Write code to remove duplicates from an unsorted
# linked list.
# Time complexity:
# Space complexity:

def remove_duplicates(passed_list):
    new_list = []
    for num in passed_list:
        if num in new_list:
            continue
        else:
            new_list.append(num)

    print(new_list)


remove_duplicates([10, 13, 18, 8, 8, 4, 10, 14])
# what does a test case for a linked list look like?
