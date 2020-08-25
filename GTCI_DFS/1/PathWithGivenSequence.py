'''
Problem Statement #
Given a binary tree and a number sequence, find if the sequence is present as a root-to-leaf path in the given tree.
'''

class TreeNode:
  def __init__(self, val, left=None, right=None):
    self.val = val
    self.left = left
    self.right = right


def find_path(root, sequence):
    if not root:
        return len(sequence) == 0

    return find_path_recursive(root, sequence, 0)


def find_path_recursive(curr_Node, sequence, seqIndex):

    if curr_Node is None:
        return False
    
    seqLen = len(sequence)

    # if the number of node we are checking is out of index or the value doesn't match the current index, return False
    if seqIndex >= seqLen or curr_Node.val != sequence[seqIndex]:
        return False

    # check if the number is same and it has no children and the index we are checking is the last index, then return true

    if curr_Node.right is None and curr_Node.left is None and seqIndex == seqLen - 1:
        return True

    return find_path_recursive(curr_Node.left,sequence,seqIndex + 1) or find_path_recursive(curr_Node.right,sequence, seqIndex+1)

def main():

  root = TreeNode(1)
  root.left = TreeNode(0)
  root.right = TreeNode(1)
  root.left.left = TreeNode(1)
  root.right.left = TreeNode(6)
  root.right.right = TreeNode(5)

  print("Tree has path sequence: " + str(find_path(root, [1, 0, 7])))
  print("Tree has path sequence: " + str(find_path(root, [1, 1, 6])))


main()



# Time and Space Complexity is O(N)