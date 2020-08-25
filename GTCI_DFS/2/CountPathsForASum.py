'''
Problem Statement #
Given a binary tree and a number ‘S’, find all paths in the tree such that the sum of all the node values of each path equals ‘S’. 
Please note that the paths can start or end at any node but all paths must follow direction from parent to child (top to bottom).
'''

class TreeNode:
  def __init__(self, val, left=None, right=None):
    self.val = val
    self.left = left
    self.right = right


def count_paths(root, S):
    return count_paths_rec(root, S,[])


def count_paths_rec(curr_Node, S, currPath):
    if curr_Node is None:
        return 0

    currPath.append(curr_Node.val)

    pathSum, pathCount = 0,0

    for i in range((len(currPath)) - 1, -1, -1):
        pathSum += currPath[i]

        if pathSum == S:
            pathCount += 1
    
    pathCount += count_paths_rec(curr_Node.left, S, currPath)
    pathCount += count_paths_rec(curr_Node.right,S, currPath)

    del currPath[-1]

    return pathCount

def main():
  root = TreeNode(12)
  root.left = TreeNode(7)
  root.right = TreeNode(1)
  root.left.left = TreeNode(4)
  root.right.left = TreeNode(10)
  root.right.right = TreeNode(5)
  print("Tree has paths: " + str(count_paths(root, 11)))


main()
