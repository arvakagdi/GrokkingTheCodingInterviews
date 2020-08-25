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


def reverse_alternate_k_elements(head, k):
    previous = None
    current = head

    while True:
        end_first_half = previous
        sub_list_end = current

        sublistLen,next = 0, None
        while current and sublistLen < k:
            next = current.next
            current.next = previous
            previous = current
            current = next
            sublistLen += 1

        if end_first_half is not None:
            end_first_half.next = previous
        else:
            head = previous
        
        sub_list_end.next = current
        sublistLen = 0
        while sublistLen < k and current:
            previous = current
            current = current.next
            sublistLen += 1

        if current is None:
            break

    return head


def main():
  head = Node(1)
  head.next = Node(2)
  head.next.next = Node(3)
  head.next.next.next = Node(4)
  head.next.next.next.next = Node(5)
  head.next.next.next.next.next = Node(6)
  head.next.next.next.next.next.next = Node(7)
  head.next.next.next.next.next.next.next = Node(8)

  print("Nodes of original LinkedList are: ", end='')
  head.print_list()
  result = reverse_alternate_k_elements(head, 2)
  print("Nodes of reversed LinkedList are: ", end='')
  result.print_list()


main()
