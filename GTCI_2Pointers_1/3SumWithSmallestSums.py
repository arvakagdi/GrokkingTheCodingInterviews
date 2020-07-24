'''
Triplets with smallest sums

Problem Statement #
Given an array arr of unsorted numbers and a target sum, count all triplets in it such that arr[i] + arr[j] + arr[k] < target where i, j, and k are three different indices. Write a function to return the count of such triplets.

Example 1:

Input: [-1, 0, 2, 3], target=3
Output: 2
Explanation: There are two triplets whose sum is less than the target: [-1, 0, 3], [-1, 0, 2]
Example 2:

Input: [-1, 4, 2, 1, 3], target=5
Output: 4
Explanation: There are four triplets whose sum is less than the target:
   [-1, 1, 4], [-1, 1, 3], [-1, 1, 2], [-1, 2, 3]
'''


def triplet_with_smaller_sum(arr, target):
  count = 0
  arr.sort()

  for FirstNumIndex in range(len(arr)):
      left = FirstNumIndex + 1
      right = len(arr) - 1
      diff = target - arr[FirstNumIndex]

      while left < right:
          if arr[left] + arr[right] < diff:
              count += right - left
              left += 1
          else:
              right -= 1
  return count


def main():
  print(triplet_with_smaller_sum([-1, 0, 2, 3], 3))
  print(triplet_with_smaller_sum([-1, 4, 2, 1, 3], 5))


main()


