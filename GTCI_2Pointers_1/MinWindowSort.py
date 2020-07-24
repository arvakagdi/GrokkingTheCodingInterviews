'''
Minimum Window Sort (medium) #
Given an array, find the length of the smallest subarray in it which when sorted will sort the whole array.

Example 1:

Input: [1, 2, 5, 3, 7, 10, 9, 12]
Output: 5
Explanation: We need to sort only the subarray [5, 3, 7, 10, 9] to make the whole array sorted
Example 2:

Input: [1, 3, 2, 0, -1, 7, 10]
Output: 5
Explanation: We need to sort only the subarray [1, 3, 2, 0, -1] to make the whole array sorted
Example 3:

Input: [1, 2, 3]
Output: 0
Explanation: The array is already sorted
Example 4:

Input: [3, 2, 1]
Output: 3
Explanation: The whole array needs to be sorted.
'''

import math

def shortest_window_sort_mine(arr):
    win_start = math.inf
    win_end = math.inf

    for start_index in range(len(arr)):
        next_index = start_index + 1
        while next_index < len(arr):
            if arr[start_index] <= arr[next_index]:
                next_index += 1
            else:
                win_start = start_index
                break
        if win_start != math.inf:
            break

    for left_elem in range(len(arr) - 1, -1 , -1):
        curr_elem = 0
        while curr_elem < left_elem:
            if arr[curr_elem] < arr[left_elem]:
                curr_elem += 1
            else:
                win_end = left_elem
                break
        if win_end != math.inf:
            break

    if win_start == math.inf and win_end == math.inf:
        return 0
    if win_start != math.inf and win_end == math.inf:
        return len(arr) - win_start

    return win_end - win_start + 1



import math


def shortest_window_sort(arr):
    low, high = 0, len(arr) - 1

    while (low < len(arr) - 1 and arr[low] <= arr[low + 1]):
        low += 1

    if low == len(arr) - 1:
        return 0

    while (high > 0 and arr[high]  >= arr[high - 1]):
        high -= 1

    sub_min = math.inf
    sub_max = -math.inf
    for num in range (low,high+1):
        sub_max = max(sub_max, arr[num])
        sub_min = min (sub_min,arr[num])


    while low > 0 and arr[low - 1] > sub_min:
        low -= 1
    while high < len(arr) -1 and arr[high + 1] < sub_max:
        high += 1

    return high - low + 1


def main():
  print(shortest_window_sort([1, 2, 5, 3, 7, 10, 9, 12]))
  print(shortest_window_sort([1, 3, 2, 0, -1, 7, 10]))
  print(shortest_window_sort([1, 2, 3]))
  print(shortest_window_sort([3, 2, 1]))


main()
