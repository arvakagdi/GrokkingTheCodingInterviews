from collections import deque

class TreeNode:
    def __init__(self,val):
        self.val = val
        self.left,self.right = None, None


def find_maximum_depth(root):
    queue = deque()

    if root is None:
        return 0

    queue.append(root)
    maxdepth  = 0

    while queue:
        levellen = len(queue)
        maxdepth += 1
        for _ in range(levellen):
            currNode = queue.popleft()

            if currNode.left:
                queue.append(currNode.left)
            if currNode.right:
                queue.append(currNode.right)
    return maxdepth


def main():
    root = TreeNode(12)
    root.left = TreeNode(7)
    root.right = TreeNode(1)
    root.right.left = TreeNode(10)
    root.right.right = TreeNode(5)
    print("Tree Maximum Depth: " + str(find_maximum_depth(root)))
    root.left.left = TreeNode(9)
    root.right.left.left = TreeNode(11)
    print("Tree Maximum Depth: " + str(find_maximum_depth(root)))


main()