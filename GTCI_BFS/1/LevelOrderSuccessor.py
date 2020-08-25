from collections import deque


class TreeNode:
  def __init__(self, val):
    self.val = val
    self.left, self.right = None, None


def find_successor(root, key):
    if root is None:
        return None

    queue = deque()
    queue.append(root)

    while queue:
        len_level = len(queue)

        for _ in range(len_level):
            curr_node = queue.popleft()

            if curr_node.left:
                queue.append(curr_node.left)
            if curr_node.right:
                queue.append(curr_node.right)
            
            if curr_node.val == key:
                if len(queue) != 0:
                    return(queue.popleft())
                else:
                    return None
    
    return None


def main():
  root = TreeNode(12)
  root.left = TreeNode(7)
  root.right = TreeNode(1)
  root.left.left = TreeNode(9)
  root.right.left = TreeNode(10)
  root.right.right = TreeNode(5)
  result = find_successor(root, 12)
  if result:
    print(result.val)
  result = find_successor(root, 9)
  if result:
    print(result.val)


main()
