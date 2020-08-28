'''
Problem Statement #
Given a set of distinct numbers, find all of its permutations.

Permutation is defined as the re-arranging of the elements of the set. For example, {1, 2, 3} has the following six permutations:

{1, 2, 3}
{1, 3, 2}
{2, 1, 3}
{2, 3, 1}
{3, 1, 2}
{3, 2, 1}
If a set has ‘n’ distinct elements it will have n!n! permutations.

Example 1:

Input: [1,3,5]
Output: [1,3,5], [1,5,3], [3,1,5], [3,5,1], [5,1,3], [5,3,1]
'''

from collections import deque
import copy

def find_permutations(nums):
  result = []

  permutations = deque()
  permutations.append([])
  numLen = len(nums)

  for curr_num in nums:
    n = len(permutations)

    for _ in range(n):
      oldPerm = permutations.popleft()

      for i in range(len(oldPerm) + 1):
        newPerm = list(oldPerm)
        newPerm.insert(i,curr_num)

        if len(newPerm) == numLen:
          result.append(newPerm)
        else:
          permutations.append(newPerm)

  return result


def generate_permutations_R(nums):
  result = []
  generate_permutations_recursive(nums, 0, [], result)
  return result

def generate_permutations_recursive(nums, index, curr_list, result):
  if index == len(nums):
    result.append(curr_list)
  else:
    for i in range(len(curr_list) + 1):
      newperm = list(curr_list)
      newperm.insert(i,nums[index])
      generate_permutations_recursive(nums,index+1,newperm,result)

def main():
  print("Here are all the permutations: " + str(generate_permutations_R([1, 3, 5])))

main()



#### 3rd Way

def permute(list):
    Permutations = []

    if len(list) == 0:
        Permutations.append([])

    else:
        firstelem = list[0]
        curr_list = permute(list[1:])

        for i in curr_list:
            for j in range(0,len(i)+1):
                elemcopy = copy.deepcopy(i)
                elemcopy.insert(j,firstelem)
                Permutations.append(elemcopy)

    return Permutations

def check_output(output, expected_output):
    """
    Return True if output and expected_output
    contains the same lists, False otherwise.

    Note that the ordering of the list is not important.

    Examples:
        check_output([ [0, 1], [1, 0] ] ], [ [1, 0], [0, 1] ]) returns True

    Args:
        output(list): list of list
        expected_output(list): list of list

    Returns:
        bool
    """
    o = copy.deepcopy(output)  # so that we don't mutate input
    e = copy.deepcopy(expected_output)  # so that we don't mutate input

    o.sort()
    e.sort()
    return o == e

print("Pass" if (check_output(permute([]), [[]])) else "Fail")
print("Pass" if (check_output(permute([0]), [[0]])) else "Fail")
print("Pass" if (check_output(permute([0, 1]), [[0, 1], [1, 0]])) else "Fail")
print("Pass" if (check_output(permute([0, 1, 2]), [[0, 1, 2], [0, 2, 1], [1, 0, 2], [1, 2, 0], [2, 0, 1], [2, 1, 0]])) else "Fail")


