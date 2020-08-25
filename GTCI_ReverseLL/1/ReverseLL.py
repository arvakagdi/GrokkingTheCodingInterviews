'''
Problem Statement #
Given the head of a Singly LinkedList, reverse the LinkedList. Write a function to return the new head of the reversed LinkedList.
'''

from __future__ import print_function
class Node:
  def __init__(self, value, next=None):
    self.value = value
    self.next = next

  def print_list(self):
    temp = self
    while temp is not None:
      print(temp.value, end=" ")
      temp = temp.next
    print()


def reverse(head):
    prev = None
    curr_node = head
    while curr_node:
        next_node = curr_node.next    # temporarily store the next node
        curr_node.next = prev         # reverse the current node
        prev = curr_node              # before we move to the next node, point previous to the current node
        curr_node = next_node         # move to next node
    return prev


def main():
  head = Node(2)
  head.next = Node(4)
  head.next.next = Node(6)
  head.next.next.next = Node(8)
  head.next.next.next.next = Node(10)

  print("Nodes of original LinkedList are: ", end='')
  head.print_list()
  result = reverse(head)
  print("Nodes of reversed LinkedList are: ", end='')
  result.print_list()


main()

'''
Time complexity #
The time complexity of our algorithm will be O(N) where ‘N’ is the total number of nodes in the LinkedList.

Space complexity #
We only used constant space, therefore, the space complexity of our algorithm is O(1)
'''