"""
Created on Thu Aug 26 after failed interview

@author: David Sergeev
"""

# the task is to make a function that return head of the reversed linked list
# turn this a -> b -> c -> d -> e -> None
# in this a <- b <- c <- d <- e equal to e -> d -> c -> b -> a -> None
import unittest


class Node:
    def __init__(self, name: str = None):
        self.name: str = name
        self.next: Node or None = None


def ll_to_list(head: Node) -> list:
    anime = list()
    while head:
        anime.append(head.name)
        head = head.next
    return anime


def print_linked_list(head: Node) -> None:
    while head:
        print(head.name, end=" -> ")
        head = head.next
    print("None \n")


# optimal solution
def solution_one(head: Node or None) -> Node or None:
    # Time complexity - O(n)
    # Space complexity O(2) = O(1)

    # a -> b -> c
    # a <- b <- c
    # ^
    # prev_node = None
    # in cycle:
    #   i need to save a.next in next_node to iterate over linked list
    #   change a.next to prev_node which is None
    #   head = temp_pointer

    # a -> b -> c
    # a <- b <- c
    #      ^
    # prev_node = a
    # next_node = b.next
    # b.next = prev_node
    # prev_node = b

    prev_node: Node or None = None

    while head:
        next_node: Node = head.next
        head.next = prev_node
        prev_node = head
        head = next_node
    return prev_node


def solution_two(head: Node) -> Node:
    # Time complexity - O(3n) = O(n)
    # Space complexity -

    # in this solution i am transforming LL in list of LL values
    # then reversing list and making new LL from it
    # it is not optimal, but there's might be a problem with "pointers" solution

    node_values = list()
    while head:
        next_node: Node or None = head.next
        node_values.append(head.name)
        del head.next, head.name, head
        head = next_node

    node_values.reverse()

    temp: Node or None = None
    for node_name in node_values:
        if temp is None:
            temp = Node(node_name)
            head = temp
            continue
        temp.next = Node(node_name)
        temp = temp.next

    return head


class TestReverse(unittest.TestCase):
    def test_many_elements(self):
        a, b, c, d, e = Node("a"), Node("b"), Node("c"), Node("d"), Node("e")
        a.next, b.next, c.next, d.next, e.next = b, c, d, e, None

        before = list(reversed(ll_to_list(a)))

        after = ll_to_list(solution_one(a))
        self.assertListEqual(after, before)

        a, b, c, d, e = Node("a"), Node("b"), Node("c"), Node("d"), Node("e")
        a.next, b.next, c.next, d.next, e.next = b, c, d, e, None

        after = ll_to_list(solution_two(a))
        self.assertListEqual(after, before)

    def test_one_element(self):
        a = Node("a")
        a.next = None
        self.assertListEqual([solution_one(a).name, solution_one(a).next], [a.name, a.next])
        self.assertListEqual([solution_two(a).name, solution_two(a).next], [a.name, a.next])


def main():
    a = Node("a")
    result = solution_two(a)
    print(a == result)


if __name__ == '__main__':
    main()
