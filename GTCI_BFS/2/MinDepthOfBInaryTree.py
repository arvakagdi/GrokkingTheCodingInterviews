from collections import deque

class TreeNode:
    def __init__(self,val):
        self.val = val
        self.left, self.right = None, None

def find_minimum_depth(root):
    queue = deque()

    if root is None:
        return 0

    queue.append(root)

    minDepth = 1
    while queue:
        levellen = len(queue)

        for _ in range(levellen):
            currNode = queue.popleft()

            if not currNode.left and not currNode.right:
                return minDepth
            
            if currNode.left:
                queue.append(currNode.left)
            if currNode.right:
                queue.append(currNode.right)
        minDepth += 1


def main():
    root = TreeNode(12)
    root.left = TreeNode(7)
    root.right = TreeNode(1)
    root.right.left = TreeNode(10)
    root.right.right = TreeNode(5)
    print("Tree Minimum Depth: " + str(find_minimum_depth(root)))
    root.left.left = TreeNode(9)
    root.right.left.left = TreeNode(11)
    print("Tree Minimum Depth: " + str(find_minimum_depth(root)))


main()
