'''
Right View of a Binary Tree (easy) #
Given a binary tree, return an array containing nodes in its right view. 
The right view of a binary tree is the set of nodes visible when the tree is seen from the right side.
'''


from __future__ import print_function
from collections import deque


class TreeNode:
  def __init__(self, val):
    self.val = val
    self.left, self.right = None, None


def tree_right_view(root):
    result = []

    if root is None:
        return None

    queue = deque()
    queue.append(root)

    while queue:
        levellen = len(queue)

        while levellen >= 1:
            curr_node = queue.popleft()
            if levellen == 1:   #check if it is the last node of that level, if yes it is the right most node
                result.append(curr_node) # add the node to result
            
            if curr_node.left:
                queue.append(curr_node.left)
            if curr_node.right:
                queue.append(curr_node.right)

            levellen -= 1
    return result


def main():
  root = TreeNode(12)
  root.left = TreeNode(7)
  root.right = TreeNode(1)
  root.left.left = TreeNode(9)
  root.right.left = TreeNode(10)
  root.right.right = TreeNode(5)
  root.left.left.left = TreeNode(3)
  result = tree_right_view(root)
  print("Tree right view: ")
  for node in result:
    print(str(node.val) + " ", end='')


main()







