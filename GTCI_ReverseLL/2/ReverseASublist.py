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
    prev = None
    current = head

    ReverseStart = p
    while ReverseStart > 1:
        prev = current
        current = current.next
        ReverseStart -= 1

    end_of_first_half = prev
    end_of_reverse_list = current

    reverselistLen = q - p + 1

    prev, nextnode = None, None
    while reverselistLen > 0:
        nextnode = current.next
        current.next = prev
        prev = current
        current = nextnode
        reverselistLen -= 1

    if end_of_first_half:
        end_of_first_half.next = prev
    else:
        head = prev
    
    end_of_reverse_list.next = current 
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
