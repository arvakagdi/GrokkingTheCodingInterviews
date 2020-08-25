'''
Problem Statement #
Given a binary tree where each node can only have a digit (0-9) value, each root-to-leaf path will represent a number. 
Find the total sum of all the numbers represented by all paths.
'''



class TreeNode:
  def __init__(self, val, left=None, right=None):
    self.val = val
    self.left = left
    self.right = right


def find_sum_of_path_numbers(root):
    return find_sum_root_to_leaf(root,0)

def find_sum_root_to_leaf (curr_Node, Sum):
    if curr_Node is None:
        return 0

    Sum = 10*Sum + curr_Node.val

    if not curr_Node.left and not curr_Node.right:
        return Sum

    return find_sum_root_to_leaf(curr_Node.left,Sum) + find_sum_root_to_leaf(curr_Node.right, Sum)

def main():
  root = TreeNode(1)
  root.left = TreeNode(0)
  root.right = TreeNode(1)
  root.left.left = TreeNode(1)
  root.right.left = TreeNode(6)
  root.right.right = TreeNode(5)
  print("Total Sum of Path Numbers: " + str(find_sum_of_path_numbers(root)))


main()