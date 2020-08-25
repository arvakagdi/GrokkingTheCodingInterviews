import math
class TreeNode:
  def __init__(self, val, left=None, right=None):
    self.val = val
    self.left = left
    self.right = right


class MaximumPathSum:
    def find_maximum_path_sum(self,root):
        self.GlobalSum = -math.inf
        self.find_max(root)
        return self.GlobalSum

    def find_max(self, node):
        if node is None:
            return 0

        leftsum = self.find_max(node.left)
        rightsum = self.find_max(node.right)

        leftsum = max(leftsum,0)
        rightsum = max(rightsum,0)

        currSum = leftsum + rightsum + node.val
        self.GlobalSum = max(currSum, self.GlobalSum)

        return max(rightsum,leftsum) + node.val

def main():
  maximumPathSum = MaximumPathSum()
  root = TreeNode(1)
  root.left = TreeNode(2)
  root.right = TreeNode(3)

  print("Maximum Path Sum: " + str(maximumPathSum.find_maximum_path_sum(root)))
  root.left.left = TreeNode(1)
  root.left.right = TreeNode(3)
  root.right.left = TreeNode(5)
  root.right.right = TreeNode(6)
  root.right.left.left = TreeNode(7)
  root.right.left.right = TreeNode(8)
  root.right.right.left = TreeNode(9)
  print("Maximum Path Sum: " + str(maximumPathSum.find_maximum_path_sum(root)))

  root = TreeNode(-1)
  root.left = TreeNode(-3)
  print("Maximum Path Sum: " + str(maximumPathSum.find_maximum_path_sum(root)))


main()