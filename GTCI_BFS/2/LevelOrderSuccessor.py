from collections import deque


class TreeNode:
  def __init__(self, val):
    self.val = val
    self.left, self.right = None, None


def find_successor(root, key):
    queue = deque()

    if root is None:
        return None
    
    queue.append(root)

    while queue:
        levlen = len(queue)

        for _ in range(levlen):

            currNode = queue.popleft()                        
            if currNode.left:
                queue.append(currNode.left)
            if currNode.right:
                queue.append(currNode.right)


            if currNode.val == key:
                if len(queue) >= 1:
                    return queue.popleft()

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
