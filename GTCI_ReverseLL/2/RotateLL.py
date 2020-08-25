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
    if head is None or head.next is None or rotations < 1:
        return head

    rotatepoint = head       
    len_list = 1
    while rotatepoint.next:             # get the length and last node of the list
        rotatepoint = rotatepoint.next
        len_list += 1
        
    rotations %= len_list               ##rotations no more than len of list
    k = len_list - rotations - 1
    i = 0
    new_tail,start = head, head

    while i < k:                        # skip n-k nodes to reach the new tail
        new_tail = new_tail.next
        i += 1

    newstart = new_tail.next            # update new head
    new_tail.next = None                # set next of tail to None
    rotatepoint.next = start            # join the list
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
  result = rotate(head, 2)
  print("Nodes of rotated LinkedList are: ", end='')
  result.print_list()


main()



''''
TIme: O(N)
Space: O(1)
'''