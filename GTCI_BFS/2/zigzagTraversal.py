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
    lefttoright = True
    
    while queue:
        level_len = len(queue)
        curr_list = deque()

        for _ in range(level_len):
            curr_node = queue.popleft()

            if lefttoright:
                curr_list.append(curr_node.val)
            else:
                curr_list.appendleft(curr_node.val)

            if curr_node.left:
                queue.append(curr_node.left)
            if curr_node.right:
                queue.append(curr_node.right)
                
        result.append(curr_list)
        lefttoright = not lefttoright

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
