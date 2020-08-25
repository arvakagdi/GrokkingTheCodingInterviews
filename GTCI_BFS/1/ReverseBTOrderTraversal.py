from collections import deque

class TreeNode:
  def __init__(self, val):
    self.val = val
    self.left, self.right = None, None

def traverse(root):
    result = deque()

    if root is None:
        return result

    queue = deque()
    queue.append(root)

    while queue:
        levelsize = len(queue)
        curr_nodelist = []
        for _ in range(levelsize):
            current_node = queue.popleft()
            curr_nodelist.append(current_node.val)
            if current_node.left:
                queue.append(current_node.left)
            if current_node.right:
                queue.append(current_node.right)
        
        result.appendleft(curr_nodelist)

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
