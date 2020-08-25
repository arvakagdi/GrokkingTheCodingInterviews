from __future__ import print_function
from collections import deque


class TreeNode:
  def __init__(self, val):
    self.val = val
    self.left, self.right, self.next = None, None, None

  # level order traversal using 'next' pointer
  def print_level_order(self):
    nextLevelRoot = self
    while nextLevelRoot:
      current = nextLevelRoot
      nextLevelRoot = None
      while current:
        print(str(current.val) + " ", end='')
        if not nextLevelRoot:
          if current.left:
            nextLevelRoot = current.left
          elif current.right:
            nextLevelRoot = current.right
        current = current.next
      print()


def connect_level_order_siblings(root):
    result = []
    queue = deque()
    queue.append(root)
    curr_list = []

    while queue:
        level_len = len(queue)
        prev = None

        for _ in range(level_len):
            curr_Node = queue.popleft()
            if prev is not None:
                prev.next = curr_Node
            
            prev = curr_Node

            if curr_Node.left:
                queue.append(curr_Node.left)
            if curr_Node.right:
                queue.append(curr_Node.right)
        result.append(curr_Node)

    return result


def main():
  root = TreeNode(12)
  root.left = TreeNode(7)
  root.right = TreeNode(1)
  root.left.left = TreeNode(9)
  root.right.left = TreeNode(10)
  root.right.right = TreeNode(5)
  connect_level_order_siblings(root)

  print("Level order traversal using 'next' pointer: ")
  root.print_level_order()


main()
