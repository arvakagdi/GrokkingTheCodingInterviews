'''
Given an array of positive numbers and a positive number ‘S’, find the length of the smallest contiguous subarray whose
sum is greater than or equal to ‘S’. Return 0, if no such subarray exists.

Example 1:

Input: [2, 1, 5, 2, 3, 2], S=7
Output: 2
Explanation: The smallest subarray with a sum great than or equal to '7' is [5, 2].
'''

import math

def smallest_subarray_with_given_sum(s, arr):
    start_index = 0    # starting point
    curr_sum = 0
    min_length = math.inf
    for index in range(len(arr)):
        curr_sum += arr[index]       # keep adding next element to the sum
        while curr_sum >= s:         # if sum reached >= target update the min length
            min_length = min (min_length, index - start_index + 1)
            curr_sum -= arr[start_index]            # keep reducing the subarray until the total is >= target
            start_index += 1                        # update the start index
    if min_length == math.inf:
        return 0
    return min_length


def main():
  print("Smallest subarray length: " + str(smallest_subarray_with_given_sum(7, [2, 1, 5, 2, 3, 2])))
  print("Smallest subarray length: " + str(smallest_subarray_with_given_sum(7, [2, 1, 5, 2, 8])))
  print("Smallest subarray length: " + str(smallest_subarray_with_given_sum(8, [3, 4, 1, 1, 6])))

main()

