'''
Count of Structurally Unique Binary Search Trees (hard) #


Input: 2
Output: 2
Explanation: As we saw in the previous problem, there are 2 unique BSTs storing numbers from 1-2.
Example 2:

Input: 3
Output: 5
Explanation: There will be 5 unique BSTs that can store numbers from 1 to 5.
'''

class TreeNode:
  def __init__(self, val):
    self.val = val
    self.left = None
    self.right = None

def count_trees(n):
    return count_trees_rec({},n)

def count_trees_rec(map,n):

    if n in map:
        return map[n]

    if n <= 1:
        return 1
    count = 0
    for i in range(1,n+1):
        left = count_trees(i-1)
        right = count_trees(n-i)

        count += left*right
    
    map[n] = count
    return count


def main():
  print("Total trees: " + str(count_trees(2)))
  print("Total trees: " + str(count_trees(3)))


main()
'''
The time complexity of the memoized algorithm will be O(n^2)since we are iterating from ‘1’ to ‘n’ and 
ensuring that each sub-problem is evaluated only once. 
The space complexity will be O(n) for the memoization map.
'''