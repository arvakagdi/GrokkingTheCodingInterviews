'''
Problem Statement #
Given a set of numbers that might contain duplicates, find all of its distinct subsets.

Example 1:

Input: [1, 3, 3]
Output: [], [1], [3], [1,3], [3,3], [1,3,3]
Example 2:

Input: [1, 5, 3, 3]
Output: [], [1], [5], [3], [1,5], [1,3], [5,3], [1,5,3], [3,3], [1,3,3], [3,3,5], [1,5,3,3] 
'''

def find_subsets(nums):
    subsets = []
    subsets.append([])
    start_index,end_index = 0,0

    for index in range(len(nums)):
        start_index = 0

        if index > 0 and nums[index] == nums[index - 1]:
             start_index = end_index + 1
        end_index = len(subsets) - 1

        for i in range(start_index,end_index+1):
            set = list(subsets[i])
            set.append(nums[index])
            subsets.append(set)
    return subsets


def main():
  print("Here is the list of subsets: " + str(find_subsets([1, 3, 3])))
  print("Here is the list of subsets: " + str(find_subsets([1, 5, 3, 3])))
main()

# Complexity O(2^N)