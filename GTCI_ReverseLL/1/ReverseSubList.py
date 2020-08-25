'''
Problem Statement #
Given the head of a LinkedList and two positions ‘p’ and ‘q’, reverse the LinkedList from position ‘p’ to ‘q’.
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


def reverse_sub_list(head, p, q):
    current = head
    prev = None
    if p == q:
        return head
    
    sub_start = p
    while current and sub_start > 1:
        prev = current
        current = current.next
        sub_start -= 1

    last_node_first_half = prev
    last_node_sub_list = current
    next = None

    sublen = q - p + 1
    while current and sublen > 0:
        next = current.next
        current.next = prev
        prev = current
        current = next
        sublen -= 1

    if last_node_first_half is not None:
        last_node_first_half.next = prev
    else:
        head = prev
    
    last_node_sub_list.next = current
    return head

        
def main():
  head = Node(1)
  head.next = Node(2)
  head.next.next = Node(3)
  head.next.next.next = Node(4)
  head.next.next.next.next = Node(5)

  print("Nodes of original LinkedList are: ", end='')
  head.print_list()
  result = reverse_sub_list(head, 2, 4)
  print("Nodes of reversed LinkedList are: ", end='')
  result.print_list()

main()
