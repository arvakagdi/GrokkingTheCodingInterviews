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
    ReverseStart = p
    previous = None
    current = head

    while ReverseStart > 1:
        previous = current
        current = current.next
        ReverseStart -= 1

    end_first_half = previous
    sub_end = current

    reveseListLen = q - p + 1
    next, previous = None, None

    while reveseListLen > 0:
        next = current.next
        current.next = previous
        previous = current
        current = next
        reveseListLen -= 1
    
    if end_first_half is not None:
        end_first_half.next = previous
    else:
        head = previous
    
    sub_end.next = current
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