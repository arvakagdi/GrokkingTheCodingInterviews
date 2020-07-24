'''
Problem Statement #
Given an array of unsorted numbers, find all unique triplets in it that add up to zero.

Example 1:

Input: [-3, 0, 1, 2, -1, 1, -2]
Output: [-3, 1, 2], [-2, 0, 2], [-2, 1, 1], [-1, 0, 1]
Explanation: There are four unique triplets whose sum is equal to zero.
Example 2:

Input: [-5, 2, -1, -2, 3]
Output: [[-5, 2, 3], [-2, -1, 3]]
Explanation: There are two unique triplets whose sum is equal to zero.
'''

def search_triplets(arr):
  triplets = []
  arr.sort()

  for firstnumindex in range(len(arr)):
      left = firstnumindex + 1
      right = len(arr) - 1
      diff = -(arr[firstnumindex])

      while left < right:
          curr_sum = arr[left] + arr[right]
          if curr_sum == diff:
              triplets.append([-diff, arr[left], arr[right]])
              left += 1
              right -= 1
              while left < right and arr[left] == arr[left - 1]:  #removes duplicates
                left += 1
              while left < right and arr[right] == arr[right - 1]:
                right -= 1
          elif curr_sum < diff:
              left += 1
          else:
              right -= 1
  return triplets


def main():
  print(search_triplets([-3, 0, 1, 2, -1, 1, -2]))
  print(search_triplets([-5, 2, -1, -2, 3]))


main()


# Complexity
'''
Time Complexity:
Sorting the array will take O(N * logN). The for loop will iterate through the whole array and the while loop will iterate through
rest of the arr from for loop index. So overall it is O(N^2)
Space complexity #
Ignoring the space required for the output array, the space complexity of the above algorithm will be O(N) which is required for sorting.
'''