'''
Structurally Unique Binary Search Trees (hard) #
Given a number ‘n’, write a function to return all structurally unique Binary Search Trees (BST) that can store values 1 to ‘n’?

Example 1:

Input: 2
Output: length of List containing root nodes of all structurally unique BSTs.
Explanation: Here are the 2 structurally unique BSTs storing all numbers from 1 to 2:
'''


class TreeNode:
  def __init__(self, val):
    self.val = val
    self.left = None
    self.right = None

def find_unique_trees(n):
    if n <= 0:
        return []
    return find_unique_trees_rec(1,n)

def find_unique_trees_rec(start,end):
    result = []

    if start > end:
        result.append(None)
        return result
    
    for i in range(start,end+1):
        leftTree = find_unique_trees_rec(start,i-1)
        rightTree = find_unique_trees_rec(i+1,end) 

        for left in leftTree:
            for right in rightTree:
                root = TreeNode(i)
                root.left = left
                root.right = right
                result.append(root)
    return result       


def main():
  print("Total trees: " + str(len(find_unique_trees(2))))
  print("Total trees: " + str(len(find_unique_trees(3))))


main()


'''
Time complexity #
The time complexity of this algorithm will be exponential and will be similar to Balanced Parentheses. 
Estimated time complexity will be O(n*2^n) but the actual time complexity ( O(4^n/\sqrt{n}) is bounded by the Catalan number.

Space complexity #
The space complexity of this algorithm will be exponential too, estimated at O(2^n) but the actual will be ( O(4^n/\sqrt{n})
'''