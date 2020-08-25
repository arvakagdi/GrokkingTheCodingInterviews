'''
Problem Statement #
Given the head of a Singly LinkedList that contains a cycle, write a function to find the starting node of the cycle.
'''


from __future__ import print_function


class Node:
  def __init__(self, value, next=None):
    self.value = value
    self.next = next

  def print_list(self):
    temp = self
    while temp is not None:
      print(temp.value, end='')
      temp = temp.next
    print()


def find_cycle_start(head):
    fast,slow = head,head
    
    while (fast is not None and fast.next is not None):
        slow = slow.next
        fast = fast.next.next

        if fast == slow:
            cycle_length = calculate_cycle_length(slow)
            break
    
    return calculate_start(cycle_length, head)
    
    
def calculate_cycle_length(slow):
    current = slow
    length = 0

    while True:
        current = current.next
        length += 1

        if slow == current:
            break
    return length
    

def calculate_start(length, head):
    slow,fast = head,head

    while length > 0:
        fast = fast.next
        length -= 1

    while slow != fast:
        slow = slow.next
        fast = fast.next

    return slow
            


def main():
  head = Node(1)
  head.next = Node(2)
  head.next.next = Node(3)
  head.next.next.next = Node(4)
  head.next.next.next.next = Node(5)
  head.next.next.next.next.next = Node(6)

  head.next.next.next.next.next.next = head.next.next
  print("LinkedList cycle start: " + str(find_cycle_start(head).value))

  head.next.next.next.next.next.next = head.next.next.next
  print("LinkedList cycle start: " + str(find_cycle_start(head).value))

  head.next.next.next.next.next.next = head
  print("LinkedList cycle start: " + str(find_cycle_start(head).value))


main()
