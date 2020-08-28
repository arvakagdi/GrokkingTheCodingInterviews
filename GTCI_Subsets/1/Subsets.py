'''
Problem Statement #
Given a set with distinct elements, find all of its distinct subsets.

Example 1:

Input: [1, 3]
Output: [], [1], [3], [1,3]
Example 2:

Input: [1, 5, 3]
Output: [], [1], [5], [3], [1,5], [1,3], [5,3], [1,5,3]

'''

def find_subsets(nums):
  subsets = []
  subsets.append([])

  for curr_num in nums:
      n = len(subsets)
      for i in range(n):
          set = list(subsets[i])
          set.append(curr_num)
          subsets.append(set)
  return subsets


def main():

  print("Here is the list of subsets: " + str(find_subsets([1, 3])))
  print("Here is the list of subsets: " + str(find_subsets([1, 5, 3])))

main()

'''
Time complexity #
Since, in each step, the number of subsets doubles as we add each element to all the existing subsets, therefore, we will have a total of O(2^N)
subsets, where ‘N’ is the total number of elements in the input set. And since we construct a new subset from an existing set, therefore,
the time complexity of the above algorithm will be O(N*2^N)

Space complexity #
All the additional space used by our algorithm is for the output list. Since we will have a total of O(2^N) subsets, 
the space complexity of our algorithm is also O(2^N).'''