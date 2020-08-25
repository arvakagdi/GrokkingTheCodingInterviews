'''
Problem Statement #
Find the minimum depth of a binary tree. The minimum depth is the number of nodes along the shortest path
from the root node to the nearest leaf node.
'''
from collections import deque

class TreeNode:
  def __init__(self, val):
    self.val = val
    self.left, self.right = None, None


def find_minimum_depth(root):
    if root is None:
        return 0
    
    queue = deque()
    min_depth = 1
    queue.append(root)

    while queue:
        curr_size = len(queue)

        for _ in range(curr_size):
            currentNode = queue.popleft()

            if not currentNode.left and not currentNode.right:
                return min_depth
            
            if currentNode.left:
                queue.append(currentNode.left)
            if currentNode.right:
                queue.append(currentNode.right)
        min_depth += 1

def main():
  root = TreeNode(12)
  root.left = TreeNode(7)
  root.right = TreeNode(1)
  root.right.left = TreeNode(10)
  root.right.right = TreeNode(5)
  print("Tree Minimum Depth: " + str(find_minimum_depth(root)))
  root.left.left = TreeNode(9)
  root.right.left.left = TreeNode(11)
  print("Tree Minimum Depth: " + str(find_minimum_depth(root)))


main()
