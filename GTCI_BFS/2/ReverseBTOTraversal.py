'''
Problem Statement #
Given a binary tree, populate an array to represent its level-by-level traversal in reverse order, 
i.e., the lowest level comes first. You should populate the values of all nodes in each level from
left to right in separate sub-arrays.
'''

from collections import deque

class TreeNode:
  def __init__(self, val):
    self.val = val
    self.left, self.right = None, None

def traverse(root):
    result = deque()
    queue = deque()
    queue.append(root)

    while queue:
        curr_len = len(queue)
        curr_list = []
        for _index in range(curr_len):
            curr_node = queue.popleft()
            curr_list.append(curr_node.val)

            if curr_node.left:
                queue.append(curr_node.left)
            if curr_node.right:
                queue.append(curr_node.right)
        result.appendleft(curr_list)
    return result

def main():
  root = TreeNode(12)
  root.left = TreeNode(7)
  root.right = TreeNode(1)
  root.left.left = TreeNode(9)
  root.right.left = TreeNode(10)
  root.right.right = TreeNode(5)
  print("Reverse level order traversal: " + str(traverse(root)))


main()
