class TreeNode:
  def __init__(self, val, left=None, right=None):
    self.val = val
    self.left = left
    self.right = right


def find_sum_of_path_numbers(root):
    return find_root_to_leaf_path_numbers(root,0)

def find_root_to_leaf_path_numbers(node, pathSum):
    if node is None:
        return 0
    
    pathSum = 10*pathSum + node.val

    if not node.right and not node.left:
        return pathSum

    return find_root_to_leaf_path_numbers(node.left, pathSum) + find_root_to_leaf_path_numbers(node.right, pathSum)

def main():
  root = TreeNode(1)
  root.left = TreeNode(0)
  root.right = TreeNode(1)
  root.left.left = TreeNode(1)
  root.right.left = TreeNode(6)
  root.right.right = TreeNode(5)
  print("Total Sum of Path Numbers: " + str(find_sum_of_path_numbers(root)))


main()
