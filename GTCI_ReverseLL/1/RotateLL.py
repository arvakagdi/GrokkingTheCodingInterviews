'''

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


def rotate(head, rotations):
    end_node = head

    ll_len = 1

    while end_node.next:
        end_node = end_node.next
        ll_len += 1

    end_node.next = head
    rotations %= ll_len

    k = ll_len - rotations - 1
    list_end = head

    while k > 0:
        list_end = list_end.next
        k -= 1

    newstart = list_end.next
    list_end.next = None

    return newstart


def main():
  head = Node(1)
  head.next = Node(2)
  head.next.next = Node(3)
  head.next.next.next = Node(4)
  head.next.next.next.next = Node(5)
  head.next.next.next.next.next = Node(6)

  print("Nodes of original LinkedList are: ", end='')
  head.print_list()
  result = rotate(head, 3)
  print("Nodes of rotated LinkedList are: ", end='')
  result.print_list()


main()
