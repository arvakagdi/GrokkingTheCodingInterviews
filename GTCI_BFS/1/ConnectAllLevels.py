'''
Connect All Level Order Siblings (medium) #
Given a binary tree, connect each node with its level order successor. 
The last node of each level should point to the first node of the next level.
'''

from __future__ import print_function
from collections import deque


class TreeNode:
  def __init__(self, val):
    self.val = val
    self.left, self.right, self.next = None, None, None

  # tree traversal using 'next' pointer
  def print_tree(self):
    print("Traversal using 'next' pointer: ", end='')
    current = self
    while current:
      print(str(current.val) + " ", end='')
      current = current.next


def connect_all_siblings(root):
    queue = deque()
    
    if root is None:
        return None
    
    queue.append(root)
    
    prev = None
    while queue:
        levellen = len(queue)
        for _ in range(levellen):
            curr_node = queue.popleft()

            if prev is not None:
                prev.next = curr_node
            prev = curr_node

            if curr_node.left:
                queue.append(curr_node.left)
            
            if curr_node.right:
                queue.append(curr_node.right)

    return root


def main():
  root = TreeNode(12)
  root.left = TreeNode(7)
  root.right = TreeNode(1)
  root.left.left = TreeNode(9)
  root.right.left = TreeNode(10)
  root.right.right = TreeNode(5)
  connect_all_siblings(root)
  root.print_tree()


main()
