'''
Problem Statement #
Given an array of unsorted numbers and a target number, find a triplet in the array whose sum is as close to the target number as possible, return the sum of the triplet. If there are more than one such triplet, return the sum of the triplet with the smallest sum.

Example 1:

Input: [-2, 0, 1, 2], target=2
Output: 1
Explanation: The triplet [-2, 1, 2] has the closest sum to the target.
Example 2:

Input: [-3, -1, 1, 2], target=1
Output: 0
Explanation: The triplet [-3, 1, 2] has the closest sum to the target.
Example 3:

Input: [1, 0, 1, 1], target=100
Output: 3
Explanation: The triplet [1, 1, 1] has the closest sum to the target.
'''
import math

def triplet_sum_close_to_target(arr, target_sum):
    arr.sort()
    min_diff = math.inf
    for firstnumindex in range(len(arr)):
        left = firstnumindex + 1
        right = len(arr) - 1

        while left < right:
            curr_sum = arr[firstnumindex] + arr[left] + arr[right]
            curr_diff = abs(target_sum - curr_sum)
            if curr_sum == target_sum:
                return target_sum

            min_diff = min(min_diff, curr_diff)
            if curr_sum < target_sum:
                left += 1
            else:
                right -= 1

    return target_sum - min_diff



def main():
  print(triplet_sum_close_to_target([-2, 0, 1, 2], 2))
  print(triplet_sum_close_to_target([-3, -1, 1, 2], 1))
  print(triplet_sum_close_to_target([1, 0, 1, 1], 100))
  print(triplet_sum_close_to_target([-1, 1, -2, 2], 0))

main()
