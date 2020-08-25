class TreeNode:
  def __init__(self, val, left=None, right=None):
    self.val = val
    self.left = left
    self.right = right


def find_paths(root, sum):
    allPaths = []

    find_paths_recursive(root, sum, [], allPaths)
    return allPaths

def find_paths_recursive(curr_Node,sum, curr_path, allPaths):
    if curr_Node is None:
        return
    
    curr_path.append(curr_Node.val)

    if curr_Node.val == sum and not curr_Node.left and not curr_Node.right:
        allPaths.append(list(curr_path))
    else:
        find_paths_recursive(curr_Node.left, sum - curr_Node.val, curr_path, allPaths)

        find_paths_recursive(curr_Node.right, sum - curr_Node.val, curr_path, allPaths)
    
    del curr_path[-1]


def main():

  root = TreeNode(12)
  root.left = TreeNode(7)
  root.right = TreeNode(1)
  root.left.left = TreeNode(4)
  root.right.left = TreeNode(10)
  root.right.right = TreeNode(5)
  sum = 23
  print("Tree paths with sum " + str(sum) +
        ": " + str(find_paths(root, sum)))

main()