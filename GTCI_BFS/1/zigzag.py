'''
Problem Statement #
Given a binary tree, populate an array to represent its zigzag level order traversal. 
You should populate the values of all nodes of the first level from left to right, 
then right to left for the next level and keep alternating in the same manner for the following levels.
'''

from collections import deque

class TreeNode:
  def __init__(self, val):
    self.val = val
    self.left, self.right = None, None

def traverse(root):
    result = []

    if root is None:
        return result
    
    queue = deque()
    queue.append(root)
    sequence = 0

    while queue:
        len_list = len(queue)
        curr_list = deque()
        
        for _ in range(len_list):
            current_node = queue.popleft()
            if sequence % 2 == 0:
                curr_list.append(current_node.val)
            else:
                curr_list.appendleft(current_node.val)

            if current_node.left:
                queue.append(current_node.left)
            if current_node.right:
                queue.append(current_node.right)
        sequence += 1
        result.append(curr_list)
    return result


def main():
  root = TreeNode(12)
  root.left = TreeNode(7)
  root.right = TreeNode(1)
  root.left.left = TreeNode(9)
  root.right.left = TreeNode(10)
  root.right.right = TreeNode(5)
  root.right.left.left = TreeNode(20)
  root.right.left.right = TreeNode(17)
  print("Zigzag traversal: " + str(traverse(root)))


main()