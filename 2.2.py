# This is question 2.2 of CTCI
#  ------ Notes to myself ----------
# Write an algorithm to find the kth to the last
# element of a singly linked list
# Original solution from: https://www.geeksforgeeks.org/nth-node-from-the-end-of-a-linked-list/
# Time complexity:
# Space complexity:

# Simple Python3 program to find
# n'th node from end
class Node:
    def __init__(self, new_data):
        self.data = new_data
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None

    # createNode and and make linked list
    def push(self, new_data):
        new_node = Node(new_data)
        new_node.next = self.head
        self.head = new_node

        # Function to get the nth node from

    # the last of a linked list
    def print_nth_from_last(self, n):
        temp = self.head  # used temp variable

        length = 0
        while temp is not None:
            temp = temp.next
            length += 1

        # print count
        if n > length:  # if entered location is greater
            # than length of linked list
            print('Location is greater than the' +
                  ' length of LinkedList')
            return
        temp = self.head
        for i in range(0, length - n):
            temp = temp.next
        print(temp.data)


# How do we get the kth element in a linked list?
# how do we count elements in linked list?
# can we count from the end in a linked list?

# Driver Code
test_list = LinkedList()
test_list.push(20)
test_list.push(4)
test_list.push(15)
test_list.push(33)
test_list.push(35)
test_list.print_nth_from_last(5)
